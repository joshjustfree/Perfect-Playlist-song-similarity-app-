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

The backend server must remain running, so keep this terminal open

### Step 5: Run the Frontend With Live Server

1. Open a new terminal in VS code
2. In the VS code file explorer, right click on `frontend/index.html`
3. Click "Open with Live Server"
4. The web app will open in your local browser at:
   `http://127.0.0.1:5500/frontend/index.html`

## YOU CAN NOW USE THE APP!!
