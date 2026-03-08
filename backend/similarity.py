# Cosine similarity calculation module
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset once when the module is imported
df = pd.read_csv('data/spotify_data.csv')

# Use these 5 features for similarity calculation
FEATURES = ['danceability', 'energy', 'key', 'tempo', 'valence']

# Find the song in the dataset that matches the given song name
def search_song(title, artist):
    result = df[
        (df['name'].str.lower().str.contains(title.lower(), na=False)) &
        (df['artists'].str.lower().str.contains(artist.lower(), na=False))
    ]
    
    if len(result) == 0:
        return None
    return result.iloc[0].to_dict()

# Find similar songs using the 5 attributes
def find_similar(song_data, count=5):

    # Use the song's details to exclude it from the results
    original_song_name = song_data['name']
    original_song_artist = song_data['artists']

    # Get the features of the input song as a list
    song_features = [[
        song_data['danceability'],
        song_data['energy'],
        song_data['key'],
        song_data['tempo'],
        song_data['valence']
    ]]

    # Get the features of all songs
    all_features = df[FEATURES].values

    # Calculate cosine similarity between the input song and all songs in the dataset
    similarities = cosine_similarity(song_features, all_features)[0]

    # Add similarity scores to the dataframe for reference
    df_copy = df.copy()
    df_copy['similarity'] = similarities

    # Remove the input song from the results using both name and artist
    df_copy = df_copy[
        ~((df_copy['name'] == original_song_name) & 
          (df_copy['artists'] == original_song_artist))
    ]

    # Removing duplicate songs from the results (same name and artist)
    df_copy = df_copy.drop_duplicates(subset=['name', 'artists'], keep='first')

    # Sort the similarities and get the top results
    df_copy = df_copy.sort_values('similarity', ascending=False).head(count) 

    # Converting the list of dictionaries
    results = []
    for _, row in df_copy.iterrows():
        song = row.to_dict()
        song['similarity'] = round(song['similarity'] * 100, 1) # Convert to percentage
        results.append(song)
    return results


# Testing the functionalities (I will be remove it before final submission)
if __name__ == "__main__":
    print(f"Dataset loaded with {len(df)} songs.")
    print(f"Columns: {df.columns.tolist()}")

    #try searching for a song
    song = search_song("Shape of You", "Ed Sheeran")
    if song:
        print(f"Found song: {song['name']} by {song['artists']}")
        print("\nSimilar songs:")
        similar_songs = find_similar(song, 5)
        for s in similar_songs:
            print(f"  {s['name']} by {s['artists']} ({s['similarity' ]}% similar)")
    else:
        print("\nSong not found.")