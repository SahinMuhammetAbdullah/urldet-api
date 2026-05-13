import pandas as pd
import joblib
from stable_baselines3 import DQN
from pars_state.pars import get_url_features
import numpy as np
import time

class URLAnalyzer:
    def __init__(self, rf_model_path, dqn_model_path):
        self.rf_model = joblib.load(rf_model_path)
        self.dqn_model = DQN.load(dqn_model_path)
        
    def analyze_url(self, url):
        try:
            t_start = time.perf_counter()

            # Feature extraction
            t0 = time.perf_counter()
            features = get_url_features(url, 0)
            features_df = pd.DataFrame([features])
            features_df = features_df.drop(columns=['URL_Type_obf_Type']).select_dtypes(include=[np.number])
            t1 = time.perf_counter()
            feature_extraction_ms = round((t1 - t0) * 1000, 2)

            # Random Forest inference
            t0 = time.perf_counter()
            rf_prediction_proba = self.rf_model.predict_proba(features_df)[0]
            is_malicious = rf_prediction_proba[1] > 0.5
            t1 = time.perf_counter()
            rf_inference_ms = round((t1 - t0) * 1000, 2)

            result = {
                "url": url,
                "is_malicious": bool(is_malicious),
                "benign_probability": float(rf_prediction_proba[0]),
                "malicious_probability": float(rf_prediction_proba[1])
            }

            # DQN inference (sadece zararlıysa)
            dqn_inference_ms = 0.0
            if is_malicious:
                t0 = time.perf_counter()
                features_array = features_df.values.astype('float32')
                dqn_action, _ = self.dqn_model.predict(features_array)
                t1 = time.perf_counter()
                dqn_inference_ms = round((t1 - t0) * 1000, 2)

                malware_types = {
                    0: "Defacement",
                    1: "malware",
                    2: "phishing",
                    3: "spam"
                }
                result["malware_type"] = malware_types[int(dqn_action)]

            t_end = time.perf_counter()
            api_processing_ms = round((t_end - t_start) * 1000, 2)

            # Zamanlama bilgilerini ekle
            result["timing"] = {
                "feature_extraction_ms": feature_extraction_ms,
                "rf_inference_ms": rf_inference_ms,
                "dqn_inference_ms": dqn_inference_ms,
                "api_processing_ms": api_processing_ms
            }

            return result
            
        except Exception as e:
            return {
                "error": f"URL analiz edilirken hata oluştu: {str(e)}",
                "url": url,
                "is_malicious": None
            }