import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect('locations.db')
cursor = conn.cursor()

# Create 'locations' table for legal locations
cursor.execute('''
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL,
        UNIQUE(latitude, longitude)  -- Prevent duplicate entries
    )
''')

# Sample legal locations
legal_locations = [
    (35.6895, 139.6917),  # Tokyo
    (40.7128, -74.0060),  # New York
    (28.7041, 77.1025),   # Delhi
    (51.5074, -0.1278)    # London
]

for location in legal_locations:
    cursor.execute('INSERT OR IGNORE INTO locations (latitude, longitude) VALUES (?, ?)', location)

# Create 'users' table for authentication
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL,     -- 'admin' or 'user'
        email TEXT              -- Admin email for alerts
    )
''')

# Insert default admin account
cursor.execute('''
    INSERT OR IGNORE INTO users (username, password, role, email) 
    VALUES ('admin', 'admin123', 'admin', '245121737303@mvsrec.edu.in')
''')

conn.commit()
conn.close()

print("✅ Database setup complete with user authentication and legal locations.")
