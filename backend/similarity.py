# Cosine similarity calculation module
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset once when the module is imported
df = pd.read_csv('data/spotify_data.csv')

# Use these 4 features for similarity calculation
FEATURES = ['danceability', 'energy', 'tempo', 'valence']

# Find the song in the dataset that matches the given song name
def search_song(title, artist):
    result = df[
        (df['name'].str.lower().str.contains(title.lower(), na=False)) &
        (df['artists'].str.lower().str.contains(artist.lower(), na=False))
    ]
    
    if len(result) == 0:
        return None
    return result.iloc[0].to_dict()

# Find similar songs using the 4 attributes
def find_similar(song_data, count=10):

    # Use the song's details to exclude it from the results
    original_song_name = song_data['name']
    original_song_artist = song_data['artists']

    # Get the features of the input song as a list
    song_features = [[
        song_data['danceability'],
        song_data['energy'],
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

    # Separating songs by the same artist and those with different artists
    same_artist = df_copy[df_copy['artists'] == original_song_artist]
    different_artist = df_copy[df_copy['artists'] != original_song_artist]

    # Only include the artist song if it is actually similar (95% or higher)
    same_artist = same_artist[same_artist['similarity'] >= 0.95]

    # Sorting the songs by similarity for both the same artist and different artists
    same_artist = same_artist.sort_values('similarity', ascending=False)
    different_artist = different_artist.sort_values('similarity', ascending=False)

    # Get the top results for songs by the same artist
    same_artist_results = same_artist.head(count)

    # If there are not enough similar songs by the same artist, then add songs from different artists
    remaining_left = count - len(same_artist_results)
    different_artist_results = different_artist.head(remaining_left)
    
    # Combine the results and prioritise songs by the same artist first
    final_results = pd.concat([same_artist_results, different_artist_results])

    # Convert the results to a list of dictionaries and round the similarity score to a percentage
    results = []
    for _, row in final_results.iterrows():
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
        similar_songs = find_similar(song, 10)
        for s in similar_songs:
            print(f"  {s['name']} by {s['artists']} ({s['similarity' ]}% similar)")
    else:
        print("\nSong not found.")