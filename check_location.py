import sqlite3
from geopy.distance import geodesic  # Library for distance calculation

def check_location(user_lat, user_lon, tolerance=50):  # 50 meters tolerance
    conn = sqlite3.connect('locations.db')
    cursor = conn.cursor()

    # Fetch stored legal locations
    cursor.execute('SELECT latitude, longitude FROM locations')
    locations = cursor.fetchall()
    
    conn.close()

    # Compare distance of user input with legal locations
    for loc in locations:
        legal_lat, legal_lon = loc
        distance = geodesic((user_lat, user_lon), (legal_lat, legal_lon)).meters
        if distance <= tolerance:
            return True  # ✅ Location is legal
    
    return False  # ❌ Location is illegal

# Example usage - User inputs latitude and longitude
user_lat = float(input("Enter latitude: "))
user_lon = float(input("Enter longitude: "))

if check_location(user_lat, user_lon):
    print("✅ The location is legal.")
else:
    print("❌ The location is illegal.")
