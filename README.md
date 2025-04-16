# Illegal Building Detection

A Flask web application that detects illegal buildings using satellite imagery and machine learning.

## Features

- Upload satellite images for analysis
- Location-based illegal building detection
- Email alerts for administrators when illegal buildings are detected
- User authentication system

## Project Structure

- `app.py`: Main Flask application
- `create_db.py`: Script to create the SQLite database
- `predict.py`: Model prediction functionality
- `check_location.py`: Utilities for checking if a location is legal for construction
- `templates/`: HTML templates for the web interface
- `static/`: CSS files for styling
- `best_model.keras`: Pre-trained model for building detection (stored using Git LFS)
- `imgs/`: Contains training and testing images for the model
  - `imgs/train/building/`: Training images of buildings
  - `imgs/train/background/`: Training images of background (non-buildings)
  - `imgs/test/building/`: Testing images of buildings
  - `imgs/test/background/`: Testing images of background (non-buildings)
- `uploads/`: Directory where user-uploaded images are stored

## Setup Instructions

1. Clone this repository
   ```
   git clone https://github.com/ErroniSamuel/Illegal-construcition-detection.git
   cd Illegal-construcition-detection
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Initialize the database
   ```
   python create_db.py
   ```

4. Configure email notifications and app secrets
   - Open `app.py` and set the following:
     - Line 10: Set your own secret key for the Flask application
     - Line 17: Add your Gmail address for sending alerts
     - Line 18: Add your 16-digit Google app password (see instructions below)
     - Line 44: Update the admin email address that will receive alerts
     - Line 51: Update the sender email to match your Gmail address

   ### Creating a Google App Password
   1. Go to your Google Account settings: https://myaccount.google.com/
   2. Select "Security" from the left navigation panel
   3. Under "Signing in to Google", select "2-Step Verification" and verify your identity
   4. At the bottom of the page, select "App passwords"
   5. Click "Select app" and choose "Other (Custom name)"
   6. Enter "flask app" as the name
   7. Click "Generate"
   8. Google will display a 16-digit password - copy this password
   9. Paste this password in app.py line 18 as your MAIL_PASSWORD value
   10. Note: Store this password securely as Google will only show it once

5. Run the application
   ```
   python app.py
   ```

6. Access the application at http://localhost:5000

## Training Your Own Model

The repository includes training and testing images in the `imgs/` directory. If you want to train your own model:

1. Make sure you have all the dependencies installed
2. Run the training script:
   ```
   python train_model.py
   ```

This will create a new model file that you can use instead of the provided `best_model.keras`. 