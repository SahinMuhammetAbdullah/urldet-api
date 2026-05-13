# URLDet - Backend API & Analiz Motoru

![URLDet Logo](https://urldet.masahin.dev/android-icon-72x72.png)

[![MIT Lisansı](https://img.shields.io/badge/Lisans-MIT-green.svg)](LICENSE) [![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![Flask](https://img.shields.io/badge/API-Flask-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/) [![ML](https://img.shields.io/badge/ML-Random%20Forest%20%7C%20DQN-orange?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/) [![PR'lar Kabul Edilir](https://img.shields.io/badge/PR'lar-kabul%20edilir-brightgreen.svg)](./.github/CONTRIBUTING.md)

Bu depo, **URLDet** projesinin backend sunucusunu ve makine öğrenimi motorunu içermektedir. Flask tabanlı bir API olan bu sistem; bir URL alır, özellik çıkarma sürecinden geçirir ve URL'nin zararlı olup olmadığını belirlemek ile tehdit türünü sınıflandırmak için önceden eğitilmiş Makine Öğrenimi modellerini kullanır.

[**Web Sitesini Görüntüle**](https://urldet.masahin.dev/) | [**Tarayıcı Eklentisini Görüntüle**](https://chromewebstore.google.com/detail/urldet-url-g%C3%BCvenlik-anali/phjancankjcbmdjcdlipmhlnjhljakjf) | [**Read in English (İngilizce Oku)**](./README.md)

## 🔗 İlgili Depolar

| Depo | Açıklama |
|---|---|
| [**urldet-extension**](https://github.com/SahinMuhammetAbdullah/urldet-extension) | URL analizini Google arama sonuçlarına entegre eden Chrome eklentisi |
| [**urldet-web**](https://github.com/SahinMuhammetAbdullah/urldet-web) | Manuel URL analizi ve proje tanıtımı için React tabanlı web sitesi |
| [**urldet-api**](https://github.com/SahinMuhammetAbdullah/urldet-api) | ML tabanlı URL analiz motorunu çalıştıran Flask backend API'si (bu depo) |

## ⚙️ Nasıl Çalışır?

1. **API Endpoint'i:** Sunucu, analiz edilecek URL'yi içeren JSON yüküyle `POST` isteklerini kabul eden tek bir `/analyze` endpoint'i sunar.
2. **Özellik Çıkarma:** Bir URL alındığında 80'den fazla özellik çıkarılır. Bunlar; sözcüksel özellikler (URL uzunluğu, token sayıları, özel karakterler), host tabanlı özellikler (TLD riski, domain entropisi) ve içerik tabanlı özellikleri (hassas kelimelerin varlığı) kapsar.
3. **İkili Sınıflandırma:** Çıkarılan özellikler, URL'nin zararsız mı yoksa zararlı mı olduğunu belirlemek için önceden eğitilmiş **Random Forest** modeline beslenir.
4. **Çok Sınıflı Sınıflandırma:** URL zararlı olarak sınıflandırılırsa, belirli tehdit türünü (örn. oltalama, kötü amaçlı yazılım, spam, tahrip) sınıflandırmak için önceden eğitilmiş **Deep Q-Network (DQN)** modeline aktarılır.
5. **Yanıt:** API, olasılıklar ve tahmin edilen tehdit türü dahil olmak üzere eksiksiz analizi içeren bir JSON nesnesi döndürür.

## 🚀 Başlarken

Yerel bir kopyayı çalıştırmak için şu adımları izleyin.

### Gereksinimler

- Python 3.12+
- pip

### Kurulum

1. **Depoyu klonlayın:**
   ```sh
   git clone https://github.com/SahinMuhammetAbdullah/urldet-api.git
   ```
2. **Proje dizinine gidin:**
   ```sh
   cd urldet-api
   ```
3. **(Önerilen) Sanal ortam oluşturun ve etkinleştirin:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Windows'ta `venv\Scripts\activate` kullanın
   ```
4. **Gerekli paketleri yükleyin:**
   ```sh
      pip install -r requirements.txt
   ```
      > Bağımlılıkların tam listesi için [`requirements.txt`](./requirements.txt) dosyasına bakın.
5. **Modelleri yerleştirin:**
   - Önceden eğitilmiş modellerin (`rf_binary.pkl` ve `multiclass_dqn_model.zip`) `/models` dizininde bulunduğundan emin olun.
   - `tld_weights.csv` dosyasının `/pars_state` dizininde bulunduğundan emin olun.

### Sunucuyu Çalıştırma

- **Geliştirme için:**
  ```sh
  python app.py
  ```
  Sunucu `http://127.0.0.1:8155` adresinde başlayacaktır.

- **Üretim için (önerilen):**
  Gunicorn gibi bir WSGI sunucusu kullanın.
  ```sh
  gunicorn --workers 4 --bind 0.0.0.0:8155 app:app
  ```

## 🤝 Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Bu proje, makine öğrenimi, web güvenliği ve API geliştirme konularında öğrenmek için harika bir yerdir.

Davranış kuralları ve pull request gönderme süreci hakkında ayrıntılar için [`CONTRIBUTING.md`](./.github/CONTRIBUTING.md) dosyasını okuyun.

## 📜 Lisans

Bu proje MIT Lisansı kapsamında lisanslanmıştır - ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

## 📧 İletişim

Muhammet Abdullah Şahin - [GitHub Profili](https://github.com/SahinMuhammetAbdullah)

Proje Bağlantısı: [https://github.com/SahinMuhammetAbdullah/urldet-api](https://github.com/SahinMuhammetAbdullah/urldet-api)