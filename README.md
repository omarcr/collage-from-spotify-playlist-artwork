# collage-from-spotify-playlist-artwork
create your own collage from your spotify playlist artwork in Python

![alt text](https://imgur.com/a/3d7OlX2) 

This package uses the following librares:

`PIL` https://pillow.readthedocs.io/en/3.0.x/installation.html 

`spotipy` https://spotipy.readthedocs.io/en/latest/#installation 


Tested in Python 3, might work in 2.

# Usage

You need to obtain your `client_id` and `client_secret` keys from your Spotify account. Do it here: https://developer.spotify.com/dashboard/login 

Once obtained insert the keys in the `client_credentials_manager` variable:

`client_credentials_manager = SpotifyClientCredentials(client_id='client_id',
                                                      client_secret='client_secret')`
                                                      
modify the variable `root`  to specify a path where to save the images and create the collage.

In the variable `uri_playlist` insert your Spotify playlist public URL in format `spotify:user:X:playlist:X`


