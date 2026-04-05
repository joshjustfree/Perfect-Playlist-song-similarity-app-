// Displaying the results of the similarity search

// Get the search results
const results = JSON.parse(sessionStorage.getItem('searchResult'));
const API_URL = 'http://127.0.0.1:5000';

// If there are no results, just go back to the search page
if (!results) {
    window.location.href = 'index.html';
}


// Get the similar songs
const similarSongs = results.similar_songs;
const songsList = document.getElementById('songsList');


// Display the similar songs
for (let i = 0; i < similarSongs.length; i++) {
    const song = similarSongs[i];

    // Create a card for each of the songs
    songsList.innerHTML += `
        <div class="song-card">
            <h3>${song.name}</h3>
            <p>${song.artists}</p>
            <button class="add-fav-btn" onclick="addToFavourites('${song.name.replace(/'/g, "\\'")}', '${song.artists.replace(/'/g, "\\'")}', event)">Add to Favourites</button>
        </div>
    `;
}

// The function to add a song to the favourites list when the user clicks a button
function addToFavourites(songName, artistName, event) {
    const button = event.target;

    // Send it to the backend to add it to the favourites
    fetch(`${API_URL}/api/favourites`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title: songName, artist: artistName })
    })
    .then(response => response.json())
    .then(data => {
        
        // Change the button to indicate that the song has been added to favourites
        button.textContent = 'Song Added!';
        button.disabled = true;
        button.classList.add('added');
    })
    .catch(error => {
        console.error('Error adding to favourites:', error);
    });
}