import streamlit as st
from lyricsgenius import Genius

# Configura tu token de acceso de Genius aquí
genius_token = "lxQLnHm5VWku3CCkrdnpvGPNH778y4jPuGMQL7zBZr-86CjbT8xIi9vcM6XjA37n"
genius = Genius(genius_token)

st.title('Song Lyrics Finder')

# Entradas del usuario para el artista y la canción
artist_name = st.text_input('Artist Name')
song_name = st.text_input('Song Name')

# Función para buscar la canción en Genius y obtener la letra
import re

def get_lyrics(song, artist):
    song = genius.search_song(title=song, artist=artist)
    if song:
        lyrics = song.lyrics
        # Elimina el texto antes de "Lyrics"
        start_of_lyrics = lyrics.find('Lyrics')
        if start_of_lyrics != -1:
            lyrics = lyrics[start_of_lyrics + len('Lyrics'):]

        # Elimina el texto como "23Embed" del final
        lyrics = re.sub(r'\d+Embed$', '', lyrics, flags=re.MULTILINE)

        return lyrics.strip()  # Elimina espacios adicionales al principio y al final
    else:
        return "Lyrics not found."



# Mostrar la letra si el usuario ha ingresado ambos, el artista y la canción
if artist_name and song_name:
    lyrics = get_lyrics(song_name, artist_name)
    st.text_area('Lyrics', lyrics, height=300)
