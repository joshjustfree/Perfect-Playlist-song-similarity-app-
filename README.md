# Perfect Playlist (Song Similarity App)

This is a web application that finds simiilar songs based on the audio features like the tempo, valence, danceability, energy and key.

## Tech Stack

- **Frontend**: HTML, CSS, JAVASCRIPT
- **Backend**: Python, Flask
- **Database**: SQLite
- **Algorithm**: Cosine Similarity (scikit-learn)
- **Dataset**: Spotify Audio Features Dataset (Kaggle)

## Features

- Search for songs by title and artist
- Get recommendations for similar songs
- View search history
- Saves songs to your favourites list

## Setup & Installation Instructions

To use the app, make sure the followng are installed on your device:

- Python 3
- Visual Studio Code (VS code)
- Live Server extention in VS code (Install from VS code extensions tab)
- Git

### Step 1: Clone the repository

Open VS code, and in the intergrated terminal run the following:

```bash

git clone https://github.com/joshjustfree/Perfect-Playlist-song-similarity-app-.git
cd Perfect-Playlist-song-similarity-app-
```

### Step 2: Set Up the Python Virtual Environment

- Run this in the terminal to navigate to the backend folder:

```bash
cd backend
```

Since the spotify dataset is already included in the repository, there is no need to download it separately.
But if it is not included:

1. Go to "kaggle.com" and download the "Spotify-Data 1921-2020" CSV file.
2. Rename it to `spotify_data.csv`.
3. Place it inside the `bcakend/data/` folder.

- Create and activate a virtual environment by running the following in the terminal:

```bash
python3 -m venv venv

# To activate on Mac/Linux
source venv/bin/activate

# To activate on Windows
venv/Scripts/activate
```

You should now see `(venv)` at the beginning of the terminal prompt

- Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Database

- While still in the backend folder with `(venv)` activated, run:

```bash
python3 database.py
```

You should see this in the terminal:
`Database initialized successfully.`

### Step 4: Start the Flask Backend Server

```bash
python3 app.py
```

You should see this in the terminal:

```bash
Database initialized successfully.
Starting up th flask 'server'...
 * Running on http://127.0.0.1:5000
 ...
```

The backend server must remain running, so keep this terminal open.

### Step 5: Run the Frontend With Live Server

1. Open a new terminal in VS code
2. In the VS code file explorer, right click on `frontend/index.html`
3. Click "Open with Live Server"
4. The web app will open in your local browser at:
   `http://127.0.0.1:5500/frontend/index.html`

### Step 6: YOU CAN NOW USE THE APP!!

# TEST CASES

## Landing Page

- **Test Case 1**: Open the web app - The landing page appears with a white backgrounnd and a search bar with two input fields.
- **Test Case 2**: Click the "Search" button with both fields empty - An error message will appear asking you to fill in the empty fields.
- **Test Case 3**: Click the "Search" button with only the "Song Title" field in - An error messagae will apper asking you to fill in the "Artist Name" field.
- **Test Case 4**: Click the "Search History" link - You will be redirected to the search history page.
- **Test Case 5**: Click the "Favourites" link - You will be redirected to the favourites page.

## Favourites Page

- **Test Case 1**: Go to the favourites page without adding any songs - The message "No favourtes yet" will appear with a link to the search page.
- **Test Case 2**: Add a song to favourites, then go to the favourites page - The song appears in the favourites list with its name and artist.
- **Test Case 3**: Try addiing the same song to favourites twice - The song only appears once in the favourites list.
- **Test Case 4**: Click the "←Back" link - You will be redirected back to the landing page.
