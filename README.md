# Create your own collage from a Spotify playlist artwork!

Example:

![Screenshot](collage6.jpg)

This package was created in Python and uses the following libraries:

`PIL` https://pillow.readthedocs.io/en/3.0.x/installation.html 

`spotipy` https://spotipy.readthedocs.io/en/latest/#installation 


Tested in Python 3 and highly likely to be compatible with previous versions.
# Usage

You need to obtain your `client_id` and `client_secret` keys from your Spotify account. Do it here: https://developer.spotify.com/dashboard/login 

Once the keys are obtained, insert them in the `client_credentials_manager` variable:

`client_credentials_manager = SpotifyClientCredentials(client_id='client_id',
                                                      client_secret='client_secret')`
                                              
In the variable `uri_playlist` insert your Spotify playlist public URI in format `spotify:user:X:playlist:X` 

Example URI used to generate the header here: `spotify:user:pni7wap5hz63vkm7171v8ki4t:playlist:5IPFs3X63PmgGnfjqAtO2e`

Finally,  modify the variable `root`  to specify a path where to save the artwork images and to save the collage.

Have fun :)

credits to Delimitry for collage routine:
https://github.com/delimitry/collage_maker

Made with :heart: at [MIT](http://web.mit.edu/)

Feedback? contact me at [@konet](https://twitter.com/konet)
