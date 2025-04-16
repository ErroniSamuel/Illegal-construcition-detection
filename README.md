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

4. Run the application
   ```
   python app.py
   ```

5. Access the application at http://localhost:5000

## Note on Large Files

This repository uses Git Large File Storage (LFS) to handle the large model file. If you're cloning this repository, make sure you have Git LFS installed on your system:

```
git lfs install
```

Then you can clone the repository normally and Git LFS will automatically handle downloading the large files. 