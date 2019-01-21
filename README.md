# Create your own collage from a spotify playlist artwork!

Example:

![Screenshot](collage6.jpg)

This package was created in Python and uses the following librares:

`PIL` https://pillow.readthedocs.io/en/3.0.x/installation.html 

`spotipy` https://spotipy.readthedocs.io/en/latest/#installation 


Tested in Python 3 and highly likely to be compatible with previous version.
# Usage

You need to obtain your `client_id` and `client_secret` keys from your Spotify account. Do it here: https://developer.spotify.com/dashboard/login 

Once obtained insert the keys in the `client_credentials_manager` variable:

`client_credentials_manager = SpotifyClientCredentials(client_id='client_id',
                                                      client_secret='client_secret')`
                                                      
modify the variable `root`  to specify a path where to save the images and create the collage.

In the variable `uri_playlist` insert your Spotify playlist public URI in format `spotify:user:X:playlist:X` 

Example URI to generate the header of the file: `spotify:user:pni7wap5hz63vkm7171v8ki4t:playlist:5IPFs3X63PmgGnfjqAtO2e`

Have fun :)

Made with :heart: at [MIT](http://web.mit.edu/)
