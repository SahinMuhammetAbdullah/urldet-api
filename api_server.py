from flask import Flask, request, jsonify
from flask_cors import CORS
from urlAnalysis.analysis import URLAnalyzer

app = Flask(__name__)

# Yalnızca kendi web siteniz ve Chrome eklentinize izin verin
ALLOWED_ORIGINS = [
    "https://urldet.masahin.dev",
    "https://api.urldet.masahin.dev",
    "https://masahin.dev",
    "https://www.masahin.dev",
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
        return
    
    # Origin veya Referer başlığını kontrol et
    origin = request.headers.get("Origin") or request.headers.get("Referer", "")
    
    # Gelen istek izinli kaynaklardan biriyle eşleşiyor mu?
    is_allowed = any(origin.startswith(allowed) for allowed in ALLOWED_ORIGINS)
    
    # Tarayıcı dışı rastgele istekleri (Postman, botlar vb.) engelle
    if not is_allowed:
        return jsonify({"error": "Unauthorized access"}), 403

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json(silent=True)
        if not data or not data.get("url"):
            return jsonify({"error": "No URL provided"}), 400

        result = analyzer.analyze_url(data["url"])
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8155)