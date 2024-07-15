import streamlit as st
import pickle
import requests
from PIL import Image
from io import BytesIO

# Load the games and similarity data
games = pickle.load(open("games_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
games_list = games['title'].values

# DuckDuckGo API details
url = "https://duckduckgo-image-search.p.rapidapi.com/search/image"
headers = {
    "x-rapidapi-key": "API KEY",
    "x-rapidapi-host": "duckduckgo-image-search.p.rapidapi.com"
}

# Function to fetch game poster from DuckDuckGo API
def fetch_game_poster(game_name):
    querystring = {"q": f"{game_name} game poster"}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    if 'results' in data and len(data['results']) > 0:
        image_url = data['results'][0]['image']
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        image = image.resize((150, 225))  # Resize the image to a consistent size (width, height)
        return image
    else:
        return Image.new('RGB', (150, 225), color = 'gray')  # Return a placeholder image if no image found

# Function to recommend games
def recommend(game):
    index = games[games['title'] == game].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_games = []
    for i in distance[1:6]:  # Skip the first game as it is the same game
        recommend_games.append(games.iloc[i[0]].title)
    return recommend_games

# Streamlit app layout
st.header("Games Recommendation System")
selectvalue = st.selectbox("Select a game from the dropdown", games_list)

if st.button("Show recommendations"):
    recommended_games = recommend(selectvalue)
    cols = st.columns(5)  # Create 5 columns for the recommended games
    for i, game in enumerate(recommended_games):
        game_poster = fetch_game_poster(game)
        with cols[i]:
            st.text(game)
            st.image(game_poster)

# Replace "YOUR_API_KEY_HERE" with your actual RapidAPI key
