# SugarSage: A Comprehensive Diabetes Prediction and Information Platform

SugarSage is a dedicated web-based application combining predictive analytics and conversational intelligence to aid individuals in assessing their diabetes risk and obtaining reliable information about diabetes care. The platform integrates advanced technologies to provide an intuitive, informative, and user-friendly experience.

---

## **Key Features**

1. **Diabetes Prediction**:
   - Calculates the probability of diabetes using user-provided health data such as age, BMI, HbA1c levels, and more.
   - Outputs the results visually with dynamic animations and provides actionable recommendations when needed.
   
2. **Interactive Chatbot**:
   - Answers diabetes-related queries, including symptoms, treatments, and prevention methods.
   - Supports natural language processing (NLP) for accurate, contextual responses.
   - Includes a sentiment analysis feature to collect user feedback for continual improvement.

3. **User-Centric Design**:
   - Responsive UI built with Tailwind CSS for seamless experiences across devices.
   - Intuitive navigation for easy access to prediction and chatbot functionalities.

4. **Backend and Workflow**:
   - Built on Flask for scalable and efficient backend operations.
   - Deployed on Heroku for accessible and reliable hosting.
   - Uses robust APIs and error-handling mechanisms to ensure uptime. Users may need to retry requests if the Heroku server restarts.

---

## **Technologies Used**

### **Frontend**:
- **HTML, CSS, and JavaScript**: To structure and provide interactivity to the platform.
- **Tailwind CSS**: For a modern and responsive design.
- **Google Fonts (Inter)**: Enhances readability and aesthetics.

### **Backend**:
- **Flask**: Serves the API endpoints for prediction and chatbot queries.
- **Joblib**: For loading machine learning models and vectorizers.
- **TextBlob**: Used for sentiment analysis in feedback processing.
- **LanguageTool API**: Ensures user queries are grammatically correct for better chatbot responses.

### **Machine Learning**:
- **Multiple Regression**: Implements diabetes prediction based on health data, with coefficients derived from Excel’s Analysis ToolPak.
- **TF-IDF Vectorization and SVM Model**: Powers the chatbot’s NLP capabilities for matching user inputs to the most relevant responses.

### **Hosting**:
- **Heroku**: Enables live deployment with dynamic routing for API endpoints.
- **CORS (Cross-Origin Resource Sharing)**: Allows seamless frontend-backend communication.

---

## **How It Works**

### **Diabetes Prediction Workflow**:
1. Users input health data into the prediction form.
2. The form data is sent to the Flask backend via a POST request.
3. The backend processes the input using the trained regression model and returns the probability of diabetes.
4. The frontend dynamically displays the results with animations and prompts users for further actions.

### **Chatbot Interaction**:
1. Users type questions into the chatbot interface.
2. The input is validated and sent to the Flask API endpoint for processing.
3. Preprocessing is applied to the query, including grammar correction using LanguageTool.
4. The NLP model identifies the most appropriate response and sends it back to the frontend.
5. Users receive responses in real-time, with follow-up options and sentiment feedback collection at session end.

---

## **How to Run Locally**

### Prerequisites:
- Python 3.8+
- Node.js for potential frontend development enhancements

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/SugarSage.git
   cd SugarSage
   ```
2. Install dependencies:
   ```bash
   pip install flask joblib textblob numpy sklearn requests
   ```
3. Run the backend:
   ```bash
   python app.py
   ```
4. Open `index.html` in your browser to interact with the frontend.

---

## **Deployment Notes**

- The application is hosted on Heroku, which occasionally restarts servers. If a request fails, retry after a minute.
- Ensure environment variables like API keys (if required) are securely stored in Heroku Config Vars.

---

## **Commitment to Health**

SugarSage is more than just a project. It reflects a genuine passion for improving public health and empowering individuals with knowledge and tools to manage diabetes effectively. We aim to make medical insights accessible and actionable for everyone.

---

## **Disclaimer**

SugarSage is designed for informational purposes only and does not replace professional medical advice, diagnosis, or treatment. Users should consult a healthcare professional for any health-related concerns.

---

Thank you for choosing SugarSage! Together, we can foster awareness and proactive care for diabetes.

