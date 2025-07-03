# URLDet - Backend API ve Analiz Motoru

![Flask Logo](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![Python Logo](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Bu repo, **URLDet** projesinin backend sunucusunu ve makine öğrenmesi motorunu içerir. Bu, analiz edilecek bir URL'yi içeren bir JSON verisi ile `POST` isteklerini kabul eden, Flask tabanlı bir API'dir. Gelen URL'yi bir özellik çıkarma hattından geçirir ve URL'nin kötü amaçlı olup olmadığını ve tehdit türünü belirlemek için önceden eğitilmiş Makine Öğrenmesi modellerini kullanır.

[**Frontend'i (Web Sitesi) Gör**](https://urldet.masahin.dev/) | [**Tarayıcı Eklentisini Gör**](https://chrome.google.com/webstore/detail/phjancankjcbmdjcdlipmhlnjhljakjf) | [**Read in English (İngilizce Oku)**](./README.md)

---

## ⚙️ Nasıl Çalışır?

1.  **API Uç Noktası:** Sunucu, analiz edilecek URL'yi içeren bir JSON yükü ile `POST` isteklerini kabul eden tek bir `/analyze` uç noktası sunar.
2.  **Özellik Çıkarma:** Bir URL alındığında, 80'den fazla özellik çıkarılır. Bunlar arasında leksik özellikler (URL uzunluğu, token sayıları, özel karakterler), ana makine tabanlı özellikler (TLD riski, alan adı entropisi) ve içerik tabanlı özellikler (hassas kelimelerin varlığı) bulunur.
3.  **İkili Sınıflandırma:** Çıkarılan özellikler, URL'nin iyi huylu veya kötü amaçlı olma olasılığını belirlemek için önceden eğitilmiş bir **Random Forest** modeline beslenir.
4.  **Çok Sınıflı Sınıflandırma:** URL kötü amaçlı olarak sınıflandırılırsa, tehdidin belirli türünü (örneğin oltalama, kötü amaçlı yazılım, spam, tahrifat) sınıflandırmak için önceden eğitilmiş bir **Deep Q-Network (DQN)** modeline iletilir.
5.  **Yanıt:** API, olasılıklar ve tahmin edilen tehdit türü de dahil olmak üzere tam analizi içeren bir JSON nesnesi döndürür.

## 🚀 Başlarken

Projeyi yerel makinenizde çalıştırmak için bu adımları takip edin.

### Ön Gereksinimler

- Python 3.8+
- pip

### Kurulum

1. **Repoyu klonlayın:**
   ```sh
   git clone https://github.com/SahinMuhammetAbdullah/urldet-api.git
   ```
2. **Proje dizinine gidin:**
   ```sh
   cd urldet-api
   ```
3. **(Önerilen) Sanal bir ortam oluşturun ve etkinleştirin:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Windows'ta `venv\Scripts\activate` kullanın
   ```
4. **Gerekli paketleri kurun:**
   ```sh
   pip install -r requirements.txt
   ```
5. **Modelleri yerleştirin:**
   - Önceden eğitilmiş modellerin (`rf_binary.pkl` ve `multiclass_dqn_model.zip`) `/models` dizininde olduğundan emin olun.
   - `tld_weights.csv` dosyasının `/pars_state` dizininde olduğundan emin olun.

### Sunucuyu Çalıştırma

- **Geliştirme için:**
  ```sh
  python app.py
  ```
  Sunucu `http://127.0.0.1:8155` adresinde başlayacaktır.

- **Production için (önerilen):**
  Gunicorn gibi bir WSGI sunucusu kullanın.
  ```sh
  gunicorn --workers 4 --bind 0.0.0.0:8155 app:app
  ```

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Bu proje, makine öğrenmesi, web güvenliği ve API geliştirme konularında bilgi edinmek için harika bir yerdir.

Davranış kurallarımız ve pull request gönderme süreci hakkında detaylı bilgi için lütfen [`CONTRIBUTING.md`](./.github/CONTRIBUTING.md) dosyasına bakın.

## 📜 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📧 İletişim

Muhammet Abdullah Şahin - [GitHub Profili](https://github.com/SahinMuhammetAbdullah)

Proje Linki: [https://github.com/SahinMuhammetAbdullah/urldet-api](https://github.com/SahinMuhammetAbdullah/urldet-api)
