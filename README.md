# Playlist Deezer to Spotify
Conevert deezer playlist into spotify playlist

## Installation

```bash
pip install spotipy
```

```bash
pip install deezer-python
```
## Get your Deezer id

Go to https://www.deezer.com click on the top rigth profile picture and your profile,
the Deezer ID is the last 10 digits of the url.

![My Remote Image](https://github.com/Maxime-Skrobala/Playlist_Deezer_to_Spotify/blob/main/image_repo/deezer_id.png)

## Get your Spotify id

Go to https://open.spotify.com/ click on the top rigth profile picture and your profile,
the Spotify ID is the last part of the url. 
![My Remote Image](https://github.com/Maxime-Skrobala/Playlist_Deezer_to_Spotify/blob/main/image_repo/spotify_id.png)

## Get your Spotify Token

Go to https://developer.spotify.com/ login and go to dashboard.
Create a new app, app name, and description can be anything and put https://google.com/ for the Redirect URI.
Then go to settings, basic information, view client secret there is your two token 
![My_Remote_Image](https://github.com/Maxime-Skrobala/Playlist_Deezer_to_Spotify/blob/main/image_repo/API_Spotify_token_blur.png)

## Execution
Execute playlist_deezer_to_spotify.py with an IDLE and add the asked elements
## Error
If you get 
```bash
error: invalid_grant, error_description: Refresh token revoked
```
This means you've already run the program and logged in, but it's been over an hour. So go to the folder where you ran it and delete the hidden .cache file. You'll then be able to log in again.
