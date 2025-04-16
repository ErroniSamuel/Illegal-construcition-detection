import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Load the model
model = load_model('best_model.keras')

# Function to preprocess the image
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (64, 64))
    img = img / 255.0  # Normalize the image
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Prediction function
def predict(image_path):
    img = preprocess_image(image_path)
    raw_prediction = model.predict(img)
    print(f'Raw predictions: {raw_prediction}')
    
    # Set threshold for classification
    threshold = 0.6
    if raw_prediction[0][0] < threshold:
        predicted_class = "Luffy"
    else:
        predicted_class = "Zoro"

    print(f'Predicted class: {predicted_class}')

# Change 'tester1.jpg' to the image you want to predict
predict('../data/bruh.jpeg')
predict('../data/down.jpeg')