from flask import Flask, request, render_template, flash
from flask_mail import Mail, Message
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import sqlite3
import os
import requests  # For downloading satellite images

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with your own secret key

# Flask Mail Configuration for Email Alerts
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = ''  # Add your email address here
app.config['MAIL_PASSWORD'] = ''  # Add your 16-digit Google app password here
mail = Mail(app)

# Load the trained model
model = load_model('best_model.keras')

# Ensure the 'uploads' folder exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -------------------- Helper Functions --------------------

def process_image(image_path):
    img = load_img(image_path, target_size=(128, 128))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def location_exists(latitude, longitude):
    conn = sqlite3.connect('locations.db')
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM locations WHERE latitude = ? AND longitude = ?', (latitude, longitude))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def send_admin_alert(location):
    admin_emails = ['your_admin_email@example.com']  # Replace with your admin email

    subject = "🚨 Illegal Building Detected!"
    body = f"An illegal building was detected at location: {location}."

    for admin_email in admin_emails:
        try:
            msg = Message(subject, sender='your_email@example.com', recipients=[admin_email])
            msg.body = body
            mail.send(msg)
            print(f"✅ Admin alert sent successfully to {admin_email}.")
        except Exception as e:
            print(f"❌ Failed to send admin alert to {admin_email}: {e}")

# -------------------- Main Application Route --------------------

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        satellite_img_url = request.form.get('satelliteImage')

        # Prioritize uploaded image; fallback to downloaded satellite image
        if file and file.filename != '':
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
        elif satellite_img_url:
            # Download satellite image and save it
            filepath = os.path.join(UPLOAD_FOLDER, 'satellite_image.png')
            try:
                response = requests.get(satellite_img_url)
                with open(filepath, 'wb') as f:
                    f.write(response.content)
            except Exception as e:
                flash('❌ Failed to download satellite image. Try again.', 'danger')
                return render_template('index.html')
        else:
            flash('❌ Please upload an image or select a map location.', 'danger')
            return render_template('index.html')

        # Process image
        try:
            processed_img = process_image(filepath)
        except Exception as e:
            flash('❌ Error processing image. Please try again.', 'danger')
            return render_template('index.html')

        # Prediction Logic
        prediction = model.predict(processed_img)[0][0]

        if prediction < 0.5:
            predicted_class = 'background'
            confidence = (1 - prediction) * 100
            if location_exists(float(request.form['latitude']), float(request.form['longitude'])):
                message = "No building detected and it's not illegal to build."
                bg_class = "legal-bg"
            else:
                message = "No building detected and it is illegal to build here."
                bg_class = "warning-bg"  # Yellow Background for illegal empty locations
        else:
            predicted_class = 'building'
            confidence = prediction * 100
            if location_exists(float(request.form['latitude']), float(request.form['longitude'])):
                message = "Building detected and is not illegal."
                bg_class = "legal-bg"
            else:
                message = "Building detected and is at an illegal place."
                bg_class = "illegal-bg"
                send_admin_alert(f"Latitude: {request.form['latitude']}, Longitude: {request.form['longitude']}")

        return render_template('result.html', 
                               prediction=predicted_class, 
                               confidence=confidence, 
                               message=message,
                               bg_class=bg_class)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

