// Management of the favurites page for the frontend

const API_URL = 'http://127.0.0.1:5000';

// Get the favourites list element
const favouritesList = document.getElementById('favouritesList');

// Load the favourites from the backend
fetch(`${API_URL}/api/favourites`)
    .then(response => response.json())
    .then(data => {
        const favourites = data.favourites;

        // If there are no favourites, display the empty state
        if (favourites.length === 0) {
            favouritesList.innerHTML = `
                <div class="empty-state">
                    <p>No Favourites Yet</p>
                    <a href="index.html">Search for a song</a>
                </div>
            `;
            return;
        
        }

        // If there are, display the favourite items
        for (let i=0; i < favourites.length; i++) {
            const item = favourites[i];
            
            favouritesList.innerHTML += `
                <div class="list-item">
                    <div class="list-item-info">
                        <h3>${item.song}</h3>
                        <p class="artist">${item.artist}</p>
                    </div>
                </div>
            `;
        }
    })

    .catch(error => {
        favouritesList.innerHTML = '<p class="error-message">Failed to load favourites. Please try again later.</p>';
        console.error('Error fetching favourites:', error);
    });