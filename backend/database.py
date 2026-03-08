# The SQLite database functions
import sqlite3

DATABASE_PATH = '../database/search_history.db'

def init_db():
    # Creating database tables
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # The Search History table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            song_title TEXT,
            artist_name TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Favorite Songs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favourite_songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            song_title TEXT,
            artist_name TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

# Saving search history to the database
def save_search(song_title, artist_name):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO search_history (song_title, artist_name) VALUES (?, ?)', (song_title, artist_name))

    conn.commit()
    conn.close()

# Gettiing all searches 
def get_search_history():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT song_title, artist_name, timestamp FROM search_history ORDER BY timestamp DESC')
    results = cursor.fetchall()
    conn.close()
    
    history = []
    for row in results:
        history.append({
            'song': row[0],
            'artist': row[1],
            'time': row[2]
        })
    return history
    
# Saving favourite songs to the database
def add_favourite(song_title, artist_name):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO favourite_songs (song_title, artist_name) VALUES (?, ?)', (song_title, artist_name))

    conn.commit()
    conn.close()

# Getting all favourite songs
def get_favourites():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT song_title, artist_name FROM favourite_songs ORDER BY timestamp DESC')
    results = cursor.fetchall()
    conn.close()
    
    favourites = []
    for row in results:
        favourites.append({
            'song': row[0],
            'artist': row[1]
        })
    return favourites
    

if __name__ == '__main__':
    init_db()