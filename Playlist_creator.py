## 1. SET UP

# Import modules
import spotipy
import os

#  Spotify Authentication
from spotipy.oauth2 import SpotifyOAuth
os.environ['SPOTIPY_CLIENT_ID'] = '13039085c25042118376c79a2b0640ff'
os.environ['SPOTIPY_CLIENT_SECRET'] = '0f580e442b2c4d1bb3177c8578eb74b4'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://localhost:8888/callback'

username = 'maria.kume'
scope = 'playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

## 2. PLAYLIST GENERATOR

print('Welcome to the playlist generator app')

# Create new (empty) playlist
playlist_name = input('Enter a playlist name: - ')
playlist_description = input('Enter a playlist description: - ')
new_playlist = sp.user_playlist_create(user=username, name=playlist_name, description=playlist_description, public=True)

# Search for songs
list_of_songs = []
query = input('Choose your parameters: keyword, year, or genre: -' )
number = input('How many songs do you want to add? - ')
results = sp.search(q=query, limit=number, type='track')
for result in results['tracks']['items']:
  list_of_songs.append(result['uri'])

# Add songs to playlist
preplaylist = sp.user_playlists(user=username)
playlist = preplaylist['items'][0]['id']
sp.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=list_of_songs)

