# The main Flask application 

from flask import Flask, jsonify, request
from flask_cors import CORS

import similarity
import database

# To allow the frontend to make requests to the backend by enabling CORS (Cross-Origin Resource Sharing)
app = Flask(__name__)
CORS(app)

# Initializing the database connection
database.init_db()

# Defining the route for the home page, which will return a welcome message when it is accessed
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Similarity API!"})

# Defining the route for searching songs, which will accept POST requests with JSON data that contains the song's title and artist(s)
@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    title = data.get('title', '')
    artist = data.get('artist', '')

    if not title or not artist:
        return jsonify({"error": "Please provide both the 'title' and 'artist'."}), 400
    
    # Searching for the song in the dataset using the search_song function from the similarity calculation module
    song = similarity.search_song(title, artist)
    if not song:
        return jsonify({"error": "Song not found."}), 404
    
    # Find the similar songs using the find_similar function from the similarity calculation module
    similar_songs = similarity.find_similar(song, count=5)

    # Save the search to the search history in the database
    database.save_search(title, artist)

    # Filter the similar songs to only include the relevant details (name, artists, and the 5 attributes) for the frontend
    filter_similar_songs = []
    for s in similar_songs:
        filter_similar_songs.append({
            'name': s['name'],
            'artists': s['artists'],
            'danceability': s['danceability'],
            'energy': s['energy'],
            'key': s['key'],
            'tempo': s['tempo'],
            'valence': s['valence']
        })
    
    # Returning the original song's details along with the list of similar songs as a JSON response to the frontend
    return jsonify({
        'original_song': {
            'name': song['name'],
            'artists': song['artists'],
            'danceability': song['danceability'],
            'energy': song['energy'],
            'key': song['key'],
            'tempo': song['tempo'],
            'valence': song['valence']
        },
        'similar_songs': filter_similar_songs
    })

# Defining the route for retrieving the search history, which will return a JSON response containing the search history that's stored in the database
@app.route('/api/history', methods=['GET'])
def get_history():
    history = database.get_search_history()
    return jsonify({"history": history})

# Defining the route for retrieving the list of favourite songs, which will return a JSON response containing the list of favourite songs that's stored in the database
@app.route('/api/favourites', methods=['GET'])
def get_favourites():
    favourites = database.get_favourites()
    return jsonify({"favourites": favourites})

# Defining the route for adding a song to the list of favourite songs, which will accept POST requests with JSON data that contains the song's title and artist(s)
@app.route('/api/favourites', methods=['POST'])
def add_favourite():
    data = request.json
    title = data.get('title', '')
    artist = data.get('artist', '')

    if not title or not artist:
        return jsonify({"error": "Please provide both the 'title' and 'artist'."}), 400
    
    database.add_favourite(title, artist)
    return jsonify({"message": "Song added to favourites!"}), 201

if __name__ == '__main__':
    print("Starting up the Flask 'server'...")
    app.run(debug=True, port=5000)