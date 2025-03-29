# SugarSage

SugarSage is a full-stack web application designed to provide real-time diabetes risk prediction and an AI-powered chatbot for answering diabetes-related queries. The project leverages machine learning, natural language processing (NLP), and web technologies to create an intuitive and data-driven platform for health insights.

## 🔥 Key Features

- **Diabetes Prediction Model**: Built using regression analysis on Kaggle diabetes datasets, leveraging Scikit-Learn for predictive modeling.
- **AI Chatbot**: Utilizes TF-IDF vectorization and an SVM classifier to provide intelligent responses with 96% accuracy.
- **RESTful API**: Facilitates seamless interaction between the front-end and back-end components.
- **Responsive UI**: Designed with Tailwind CSS for a modern and user-friendly experience.
- **Deployment on Heroku**: Ensures accessibility and scalability for users.

## 📌 Tech Stack

- **Backend**: Flask (Python), Scikit-Learn, Pandas
- **Frontend**: Tailwind CSS, JavaScript
- **Machine Learning**: Regression Analysis, TF-IDF, SVM
- **Dataset**: [Kaggle Diabetes Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) for training the prediction model
- **Deployment**: Heroku
- **API Development**: RESTful architecture

## 🚀 Installation & Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/abdullahlali/SugarSage.git
   cd SugarSage
   ```

2. **Create a Virtual Environment (Recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```sh
   flask run
   ```
   The app will be accessible at `http://127.0.0.1:5000/`.

## 🤝 Contributing

If you'd like to contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Commit changes: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature-branch`
5. Open a Pull Request.

## 📜 License

This project is licensed under the MIT License.

## 📬 Contact

For inquiries or contributions, feel free to reach out:
[GitHub Profile](https://github.com/abdullahlali)

