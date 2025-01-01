from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
from textblob import TextBlob
from saveModel import preprocess_text  # Reuse preprocessing from saveModel.py
from predictions import predict_diabetes_probability  # Import prediction logic
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Function to use LanguageTool API for grammar checking and return corrected text
def check_grammar_and_correct(text):
    url = "https://api.languagetool.org/v2/check"
    
    # Define the parameters
    params = {
        'text': text,
        'language': 'en-US',  # Language you want to check
    }
    
    # Make the request to the LanguageTool API
    response = requests.post(url, data=params)
    
    # If the request was successful (status code 200)
    if response.status_code == 200:
        result = response.json()
        errors = result.get('matches', [])
        
        # Start with the original text
        corrected_text = text
        
        # Apply each correction to the original text
        for error in errors:
            # Extract the start and end position of the error in the text
            start = error['offset']
            end = start + error['length']
            replacement = error['replacements'][0]['value'] if error['replacements'] else ""
            
            # Replace the error in the text with the suggested replacement
            corrected_text = corrected_text[:start] + replacement + corrected_text[end:]
        
        return corrected_text
    else:
        print(f"Error: {response.status_code}")
        return text  # Return original text if there's an error

app = Flask(__name__)
CORS(app)

from flask import abort

@app.route('/')
def index():
    abort(404)  # Returns a 404 error for the root route


# Load saved model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
X_train_vectors = joblib.load('xtrainvectors.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    probability = predict_diabetes_probability(
        gender=data['gender'],
        age=data['age'],
        hypertension=data['hypertension'],
        heart_disease=data['heart_disease'],
        smoking_history=data['smoking_history'],
        bmi=data['bmi'],
        HbA1c_level=data['HbA1c_level'],
        blood_glucose_level=data['blood_glucose_level']
    )
    return jsonify({'probability': f"{probability:.2%}"})

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json['user_input']
    user_input = check_grammar_and_correct(user_input)
    preprocessed_input = preprocess_text(user_input)
    input_vector = vectorizer.transform([preprocessed_input])
    predicted_response = model.predict(input_vector)[0]

    # Calculate cosine similarity for confidence level
    similarities = cosine_similarity(input_vector, X_train_vectors)
    max_similarity = similarities.max()
    confidence_level = max_similarity.item()

    # Check confidence level and determine response
    if confidence_level < 0.5:
        response = "I’m sorry, I couldn't find a clear answer. Could you please provide more details or clarify your question? I’ll do my best to assist you!"
    else:
        response = predicted_response  # Predict the response

    return jsonify({'response': response})

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    # Get the user's feedback from the POST request
    feedback = request.json.get('feedback', '')

    if not feedback:
        return jsonify({'error': 'Feedback cannot be empty'}), 400

    # Perform sentiment analysis
    sentiment = TextBlob(feedback).sentiment
    polarity = sentiment.polarity

    if polarity > 0:
        message = "Thank you! I'm glad you found the conversation helpful."
    elif polarity < 0:
        message = "I'm sorry the experience wasn't satisfactory. Please share suggestions for improvement."
    else:
        message = "Thank you for your feedback! I appreciate your input."

    return jsonify({
        'polarity': polarity,
        'message': message
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
