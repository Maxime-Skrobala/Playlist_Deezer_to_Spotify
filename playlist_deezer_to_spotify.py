import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import deezer
import time


os.environ['SPOTIPY_CLIENT_ID'] = input("SPOTIPY_CLIENT_ID : ")
os.environ['SPOTIPY_CLIENT_SECRET']=input("SPOTIPY_CLIENT_SECRET : ")
os.environ['SPOTIPY_REDIRECT_URI']='https://google.com/'
user_id=input("SPOTIFY_USER_ID : ")
deezer_id=input("DEEZER_ID : ")

client = deezer.Client()
user = client.get_user(deezer_id)

playlist_user = user.get_playlists()
liste_play = []
liste_playlist = []
i=0

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


for playlist in playlist_user:
    liste_playlist.append(playlist.title)
    liste_track=[]
    i=i+1
    print(i)
    print(playlist.title)
    
    tracks_play = playlist.get_tracks()
    sp_playlist= sp.user_playlist_create(user=user_id,name=playlist.title,public=True,collaborative=False, description="")
    
    for tracks in tracks_play:
        try:
            track_artist=(tracks.get_artist()).name
            result = sp.search(tracks.title + " " + track_artist,limit=1)
            track_id = result["tracks"]["items"][0]["id"]
            sp.user_playlist_add_tracks(user=user_id, playlist_id=sp_playlist["id"], tracks=[track_id], position=None)
            liste_track.append(tracks.title)
        except:
            print("ERROR missing track " + tracks.title)
    liste_play.append(liste_track)

