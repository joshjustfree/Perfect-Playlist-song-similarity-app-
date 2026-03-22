// Displaying the results of the similarity search

// Get the search results
const results = JSON.parse(sessionStorage.getItem('searchResult'));

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
        </div>
    `;
}