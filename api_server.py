import hashlib
import json
import redis
from flask import Flask, request, jsonify
from flask_cors import CORS
from urlAnalysis.analysis import URLAnalyzer

app = Flask(__name__)

# Redis bağlantısı (Localhost)
r = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

# Yalnızca kendi web siteniz ve Chrome eklentinize izin verin
ALLOWED_ORIGINS = [
    "https://urldet.masahin.dev",
    "https://masahin.dev",
    "https://www.masahin.dev",
    "https://api.urldet.masahin.dev",
    "chrome-extension://phjancankjcbmdjcdlipmhlnjhljakjf"
]

CORS(app, origins=ALLOWED_ORIGINS, supports_credentials=True)

# URLAnalyzer ve modelleri yükle
analyzer = URLAnalyzer(
    rf_model_path="models/rf_binary.pkl",
    dqn_model_path="models/multiclass_dqn_model"
)

@app.before_request
def validate_origin():
    # CORS preflight (OPTIONS) isteklerine izin ver
    if request.method == "OPTIONS":
        return None
    
    # Origin veya Referer başlığını al
    origin = request.headers.get("Origin") or request.headers.get("Referer", "")
    
    # Doğrudan eklentiden veya güvenli kaynaklardan gelen istekleri kontrol et
    if origin:
        is_allowed = any(origin.startswith(allowed) for allowed in ALLOWED_ORIGINS)
        if not is_allowed:
            return jsonify({"error": "Unauthorized origin"}), 403

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json(silent=True)
        if not data or not data.get("url"):
            return jsonify({"error": "No URL provided"}), 400

        target_url = data["url"].strip()

        # 1. URL Hash kontrolü (Redis Cache)
        url_hash = hashlib.sha256(target_url.encode()).hexdigest()
        cache_key = f"urldet:{url_hash}"

        try:
            cached_result = r.get(cache_key)
            if cached_result:
                res = json.loads(cached_result)
                res["cached"] = True
                return jsonify(res)
        except Exception:
            pass  # Redis geçici olarak erişilemezse analize devam et

        # 2. ML Feature Extraction ve Model Analizi
        result = analyzer.analyze_url(target_url)

        # 3. Sonucu 2 saat (7200 sn) önbelleğe al
        try:
            r.setex(cache_key, 7200, json.dumps(result))
        except Exception:
            pass

        result["cached"] = False
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8155)