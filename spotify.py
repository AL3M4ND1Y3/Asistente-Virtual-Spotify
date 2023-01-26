import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='04a53104dcd24b90b51bd32d9335507a', client_secret='a91f56677b6a4c96ba4c816d3171369d', redirect_uri='http://localhost:8000/', scope=['user-library-modify', 'user-library-read', 'app-remote-control', 'streaming']))

def play_song(song_name):
    results = sp.search(q=song_name, type='track')
    track = results['tracks']['items'][0]
    track_uri = track['uri']
    sp.start_playback(uris=[track_uri])