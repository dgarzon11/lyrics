import streamlit as st
from lyricsgenius import Genius

# Configure your Genius access token here
genius_token = "YOUR_GENIUS_TOKEN"
genius = Genius(genius_token)

st.title('Song Lyrics Finder')

# User inputs for artist and song name
artist_name = st.text_input('Artist Name')
song_name = st.text_input('Song Name')

# Function to search for the song on Genius and retrieve lyrics
import re

def get_lyrics(song, artist):
    song = genius.search_song(title=song, artist=artist)
    if song:
        lyrics = song.lyrics
        # Remove text before "Lyrics"
        start_of_lyrics = lyrics.find('Lyrics')
        if start_of_lyrics != -1:
            lyrics = lyrics[start_of_lyrics + len('Lyrics'):]

        # Remove text like "23Embed" at the end
        lyrics = re.sub(r'\d+Embed$', '', lyrics, flags=re.MULTILINE)

        return lyrics.strip()  # Remove extra spaces at the beginning and end
    else:
        return "Lyrics not found."

# Display lyrics if both artist and song are entered by the user
if artist_name and song_name:
    lyrics = get_lyrics(song_name, artist_name)
    st.text_area('Lyrics', lyrics, height=300)
