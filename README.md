Games Recommendation System

This project is a web application built with Streamlit that recommends games based on a selected game. The application also fetches and displays game posters using the DuckDuckGo Image Search API.

## Features

- Select a game from a dropdown list.
- Display recommended games.
- Fetch and display posters for recommended games.

## Requirements

- Python 3.6+
- Streamlit
- Requests
- Pillow

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/bharathwaaj18/games-recommendation-system.git
   cd games-recommendation-system
   ```

2. Install the required packages:

   ```bash
   pip install streamlit requests pillow
   ```

3. Obtain a RapidAPI key for the DuckDuckGo Image Search API:

   - Sign up on [RapidAPI](https://rapidapi.com/).
   - Subscribe to the DuckDuckGo Image Search API.
   - Get your API key.

4. Update the code with your RapidAPI key:

   Replace `"YOUR_API_KEY_HERE"` in the code with your actual RapidAPI key.

5. Prepare the data files:

   - Ensure you have `games_list.pkl` and `similarity.pkl` in the project directory.

## Running the Application

To run the Streamlit application, use the following command:

```bash
streamlit run app.py
```

Replace `app.py` with the filename of your Streamlit application script.

## Code Explanation

The application consists of the following main parts:

1. **Loading Data**: Games and similarity data are loaded using `pickle`.
2. **API Details**: DuckDuckGo Image Search API details are set up with headers and query parameters.
3. **Fetch Game Poster**: The `fetch_game_poster` function fetches the game poster using the API and resizes it.
4. **Recommend Games**: The `recommend` function returns a list of recommended games based on the selected game.
5. **Streamlit Layout**: The Streamlit app layout displays the selected game, recommended games, and their posters in a row.

## Example Usage

1. Select a game from the dropdown list.
2. Click the "Show recommendations" button.
3. View the recommended games and their posters displayed in a row.
