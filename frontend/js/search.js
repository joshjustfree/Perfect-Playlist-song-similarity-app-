// Search functionality for the frontend

// The URL of the backend search API
const API_URL = 'http://127.0.0.1:5000';

// Get the input values
const searchForm = document.getElementById('searchForm');
const errorMessage = document.getElementById('errorMessage');
const transitionOverlay = document.getElementById('transitionOverlay');

// Listen for the form submission and prevent the default form submission behaviour 
searchForm.addEventListener('submit', async (event) => { 
    event.preventDefault(); 

    // Get the title and artist values from the form
    const title = document.getElementById('songTitle').value.trim();
    const artist = document.getElementById('artistName').value.trim();

    // Clear any previous error messages
    errorMessage.textContent = '';

    // Check if both fields are filled
    if (!title || !artist) {
        errorMessage.textContent = 'Please enter both song title and artist name.';
        return;
    }

    try {
        // Show the transition overlay
        transitionOverlay.classList.add('active');

        // Send the search request to the backend via a POST request
        const response = await fetch(`${API_URL}/api/search`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title, artist })
        });

        // Get the response data
        const data = await response.json();

        // Throw an erro if one occures
        if (!response.ok) {
            throw new Error(data.error || 'An error occurred while searching for the song.');
        }

        // Save the search result in the session storage
        sessionStorage.setItem('searchResult', JSON.stringify(data));

        // Wait for a 5 seconds before redirecting to the result page
        setTimeout(() => {
            window.location.href = 'result.html';  // Redirect the user to the result page
        }, 500);

    } catch (error) {
        // If an error occurs, hide the transition overlay and display the error message
        transitionOverlay.classList.remove('active');
        errorMessage.textContent = error.message;
    }
});