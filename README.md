# URLDet - Backend API & Analysis Engine

![URLDet Logo](https://urldet.masahin.dev/android-icon-72x72.png)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/API-Flask-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![ML](https://img.shields.io/badge/ML-Random%20Forest%20%7C%20DQN-orange?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./.github/CONTRIBUTING.md)

This repository contains the backend server and machine learning engine for the **URLDet** project. It's a Flask-based API that receives a URL, processes it through a feature extraction pipeline, and uses pre-trained Machine Learning models to determine if the URL is malicious and to classify the threat type.

[**See the Frontend (Website)**](https://urldet.masahin.dev/) | [**See the Browser Extension**](https://chromewebstore.google.com/detail/urldet-url-g%C3%BCvenlik-anali/phjancankjcbmdjcdlipmhlnjhljakjf) | [**Read in Turkish (Türkçe Oku)**](./README.tr.md)

## 🔗 Related Repositories

| Repository                                                                        | Description                                                              |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| [**urldet-extension**](https://github.com/SahinMuhammetAbdullah/urldet-extension) | Chrome extension that integrates URL analysis into Google search results |
| [**urldet-web**](https://github.com/SahinMuhammetAbdullah/urldet-web)             | React-based website for manual URL analysis and project showcase         |
| [**urldet-api**](https://github.com/SahinMuhammetAbdullah/urldet-api)             | Flask backend API powering the ML-based URL analysis engine (this repo)  |

## ⚙️ How It Works

1. **API Endpoint:** The server exposes a single endpoint, `/analyze`, which accepts `POST` requests with a JSON payload containing the URL to be analyzed.
2. **Feature Extraction:** Upon receiving a URL, a series of over 80 features are extracted. These include lexical features (URL length, token counts, special characters), host-based features (TLD risk, domain entropy), and content-based features (presence of sensitive words).
3. **Binary Classification:** The extracted features are fed into a pre-trained **Random Forest** model to determine the probability of the URL being benign or malicious.
4. **Multi-Class Classification:** If the URL is classified as malicious, it is then passed to a pre-trained **Deep Q-Network (DQN)** model to classify the specific type of threat (e.g., phishing, malware, spam, defacement).
5. **Response:** The API returns a JSON object with the complete analysis, including probabilities and the predicted threat type.

## 🚀 Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- Python 3.12+
- pip

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/SahinMuhammetAbdullah/urldet-api.git
   ```
2. **Navigate to the project directory:**
   ```sh
   cd urldet-api
   ```
3. **(Recommended) Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. **Install the required packages:**
   ```sh
      pip install -r requirements.txt
   ```
      > See [`requirements.txt`](./requirements.txt) for the full list of dependencies.
5. **Place the models:**
   - Ensure the pre-trained models (`rf_binary.pkl` and `multiclass_dqn_model.zip`) are inside the `/models` directory.
   - Ensure the `tld_weights.csv` file is inside the `/pars_state` directory.

### Running the Server

- **For development:**
  ```sh
  python app.py
  ```
  The server will start on `http://127.0.0.1:8155`.

- **For production (recommended):**
  Use a WSGI server like Gunicorn.
  ```sh
  gunicorn --workers 4 --bind 0.0.0.0:8155 app:app
  ```

## 🤝 Contributing

Contributions are welcome! This project is a great place to learn about machine learning, web security, and API development.

Please read [`CONTRIBUTING.md`](./.github/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Muhammet Abdullah Şahin - [GitHub Profile](https://github.com/SahinMuhammetAbdullah)
