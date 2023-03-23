import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re
import pyttsx3

def hablar(mensaje):
    #Encender la voz
    engine = pyttsx3.init()

    #Hablar
    engine.say(mensaje)
    engine.runAndWait()
    
#credenciales de spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='04a53104dcd24b90b51bd32d9335507a', client_secret='a91f56677b6a4c96ba4c816d3171369d', redirect_uri='http://localhost:8000/', scope=['user-library-modify', 'user-library-read', 'app-remote-control', 'streaming']))

def spotify(song_name):
    try:
        if "reproducir" in song_name:
            song_name = song_name.replace("reproducir","")
            song_name = song_name.replace("la canción","")
            #Convirtiendo el numero en una
            results = sp.search(q=song_name, type='track')
            track = results['tracks']['items'][0]
            nombre = track["name"]
            autor = track["artists"][0]["name"]
            track_uri = track['uri']
            sp.start_playback(uris=[track_uri])
            hablar(f"Reproduciendo: {nombre} de {autor}")
    except spotipy.exceptions.SpotifyException as e:
        if e.http_status == 404 and e.reason == 'NO_ACTIVE_DEVICE':
            print("No se ha encontrado un dispositivo activo. Por favor, asegúrese de tener un dispositivo de reproducción de Spotify activo.")
    except IndexError:
        print("No se encontro la cancion")
    if "reproducir" in song_name:
        song_name = song_name.replace("reproducir","")
        song_name = song_name.replace("la canción","")
        #Convirtiendo el numero en una
        results = sp.search(q=song_name, type='track')
        track = results['tracks']['items'][0]
        nombre = track["name"]
        autor = track["artists"][0]["name"]
        track_uri = track['uri']
        sp.start_playback(uris=[track_uri])
        hablar(f"Reproduciendo: {nombre} de {autor}")
    elif "pausame" in song_name:
        sp.pause_playback()
        hablar("pausando musica")   
    elif "seguir" in song_name:
        sp.start_playback()
    elif "volumen" in song_name:
        song_name = song_name.replace("poneme el volumen de la cancion al", "")
        match = re.search(r'\d+', song_name)
        if match:
            # Ajustar el volumen de Spotify al número especificado
            volumen = int(match.group())
            sp.volume(volumen)
            hablar("El volumen se ajustó a " + str(volumen) + "%")
        else:
            print("No entendí el volumen deseado.")