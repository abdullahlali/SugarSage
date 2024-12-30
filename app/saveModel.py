import joblib
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from textblob import TextBlob


import nltk
nltk.data.path.append('./nltk_data')  # Add path to local nltk_data



# Download all requirements only once
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


dataset = joblib.load('dataset.pkl')

# Preprocessing Function
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(tokens)

# Save the trained model and vectorizer
def save_model():
    # Preprocess and train the model
    preprocessed_dataset = [(preprocess_text(question), response) for question, response in dataset]
    X_train = [question for question, _ in preprocessed_dataset]
    y_train = [response for _, response in preprocessed_dataset]

    vectorizer = TfidfVectorizer()
    X_train_vectors = vectorizer.fit_transform(X_train)

    model = SVC(probability=True)
    model.fit(X_train_vectors, y_train)

    # Save the model and vectorizer
    joblib.dump(X_train_vectors, 'xtrainvectors.pkl')
    joblib.dump(model, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
    print("Model and vectorizer saved!")


# save_model()
