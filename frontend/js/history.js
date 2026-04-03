// History management for the frontend

const API_URL = 'http://127.0.0.1:5000';

// Get the history list element
const historyList = document.getElementById('historyList');

// Load the search history from the backend
fetch(`${API_URL}/api/history`)
    .then(response => response.json())
    .then(data => {
        const history = data.history;

        // If there is no history, display the empty state
        if (history.length === 0) {
            historyList.innerHTML = `
                <div class="empty-state">
                    <p>No Search History Yet</p>
                    <a href="index.html">Search for a song</a>
                </div>
            `;
            return;
        
        }
        
        // If there is, display the history items
        for (let i=0; i < history.length; i++) {
            const item = history[i];

            historyList.innerHTML += `
                <div class="list-item">
                    <div class="list-item-info">
                        <h3>${item.song}</h3>
                        <p class="artist">${item.artist}</p>
                        <p class="time">${item.time}</p>
                    </div>          
                </div>
            `;
        }
    })

    .catch(error => {
        historyList.innerHTML = '<p class="error-message">Failed to load search history. Please try again later.</p>';
        console.error('Error fetching history:', error);
    });