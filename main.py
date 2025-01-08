import requests
import streamlit as st

def search_lyrics(artist, music):
    endpoint = f"https://api.lyrics.ovh/v1/{artist}/{music}"
    response = requests.get(endpoint)
    data = response.json()["lyrics"] if response.status_code == 200 else "Lyrics not found"
    return data

st.image("https://imgur.com/SmktDIH")
st.title("Lyrics Finder")

artist = st.text_input("Artist", key="artist")
music = st.text_input("Music", key="music")
search = st.button("Search")

if search:
    lyrics = search_lyrics(artist, music)
    st.write(lyrics)