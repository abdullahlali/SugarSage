import numpy as np


# Sigmoid function ensures valid probabilities
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def predict_diabetes_probability(gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level):
    # Coefficients from my linear regression table
    
    # Y=−0.8623+0.0141⋅(gender)+0.00138⋅(age)+0.0952⋅(hypertension)+0.1174⋅(heart disease)−0.0027⋅(smoking history)+0.00419⋅(bmi)+0.0812⋅(HbA1c level)+0.00227⋅(blood glucose level)
    # Where:
    # gender: Female = 0, Male = 1
    # hypertension and heart disease: No = 0, Yes = 1
    # smoking history: Never = 0, Former = 1, Not Current = 2, Current = 3, No Info = 4
    # age, bmi, HbA1c level, and blood glucose level: Continuous numeric values.

    intercept = -0.8623
    coef_gender = 0.0141
    coef_age = 0.00138
    coef_hypertension = 0.0952
    coef_heart_disease = 0.1174
    coef_smoking_history = -0.0027
    coef_bmi = 0.00419
    coef_HbA1c_level = 0.0812
    coef_blood_glucose = 0.00227
    
    # Linear regression output (z)
    z = (intercept
         + coef_gender * gender
         + coef_age * age
         + coef_hypertension * hypertension
         + coef_heart_disease * heart_disease
         + coef_smoking_history * smoking_history
         + coef_bmi * bmi
         + coef_HbA1c_level * HbA1c_level
         + coef_blood_glucose * blood_glucose_level)
    
    # Convert to probability using sigmoid
    probability = sigmoid(z)
    return probability
    