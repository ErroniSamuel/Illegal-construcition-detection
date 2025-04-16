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

3. **Important**: You need to obtain the trained model file `best_model.keras` (295MB) separately and place it in the root directory. Contact the repository owner for access to this file.

4. Initialize the database
   ```
   python create_db.py
   ```

5. Run the application
   ```
   python app.py
   ```

6. Access the application at http://localhost:5000

## Model File

The trained model file (`best_model.keras`, ~295MB) is not included in this repository due to GitHub's file size limitations. This file is required for the application to function properly.

Options to obtain the model file:
- Contact the repository owner for direct access
- Train your own model using the `train_model.py` script with an appropriate dataset of satellite images
- Download from a cloud storage link (if provided) 