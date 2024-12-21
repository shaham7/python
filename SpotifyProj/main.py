import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# I could scrape the website, but this seemed cleaner and easier
CLIENT_ID = 'daed3ec445bb4cb68139e0f57688a5a6'
CLIENT_SECRET = '54471c20b8724c5d8b7f3ebe94826ccf'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))

# Error handling because the playlist ID can change tired of getting that error 
try:
    playlist_id = '6UeSakyzhiEt4NB3UAd6NQ'  # Spotify's "Billboard Hot 100" playlist
    playlist = sp.playlist_tracks(playlist_id, limit=100)

    tracks = []
    for item in playlist['items']:
        track = item['track']
        artists = track['artists']
    
        genres = set() 
        for artist in artists:
            artist_data = sp.artist(artist['id'])
            genres.update(artist_data['genres']) 
        
        tracks.append({
            'Name': track['name'],
            'Artist': ', '.join([artist['name'] for artist in artists]),
            'Album': track['album']['name'],
            'Popularity': track['popularity'],
            'Genres': ', '.join(genres)  
        })

except spotipy.exceptions.SpotifyException as e:
    print(f"Spotify API Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")

df = pd.DataFrame(tracks)
df.to_csv('billboard_top_100_with_genres.csv', index=False)

print("Data saved to billboard_top_100_with_genres.csv")
