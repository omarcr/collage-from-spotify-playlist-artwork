from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import os
import re

def make_collage(images, filename, width, init_height):
    """
    Make a collage image with a width equal to `width` from `images` and save to `filename`.
    """
    if not images:
        print('No images for collage found!')
        return False

    margin_size = 2
    # run until a suitable arrangement of images is found
    while True:
        # copy images to images_list
        images_list = images[:]
        coefs_lines = []
        images_line = []
        x = 0
        while images_list:
            # get first image and resize to `init_height`
            img_path = images_list.pop(0)
            img = Image.open(img_path)
            img.thumbnail((width, init_height))
            # when `x` will go beyond the `width`, start the next line
            if x > width:
                coefs_lines.append((float(x) / width, images_line))
                images_line = []
                x = 0
            x += img.size[0] + margin_size
            images_line.append(img_path)
        # finally add the last line with images
        coefs_lines.append((float(x) / width, images_line))

        # compact the lines, by reducing the `init_height`, if any with one or less images
        if len(coefs_lines) <= 1:
            break
        if any(map(lambda c: len(c[1]) <= 1, coefs_lines)):
            # reduce `init_height`
            init_height -= 10
        else:
            break

    # get output height
    out_height = 0
    for coef, imgs_line in coefs_lines:
        if imgs_line:
            out_height += int(init_height / coef) + margin_size
    if not out_height:
        print('Height of collage could not be 0!')
        return False

    collage_image = Image.new('RGB', (width, int(out_height)), (35, 35, 35))
    # put images to the collage
    y = 0
    for coef, imgs_line in coefs_lines:
        if imgs_line:
            x = 0
            for img_path in imgs_line:
                img = Image.open(img_path)
                # if need to enlarge an image - use `resize`, otherwise use `thumbnail`, it's faster
                k = (init_height / coef) / img.size[1]
                if k > 1:
                    img = img.resize((int(img.size[0] * k), int(img.size[1] * k)), Image.ANTIALIAS)
                else:
                    img.thumbnail((int(width / coef), int(init_height / coef)), Image.ANTIALIAS)
                if collage_image:
                    collage_image.paste(img, (int(x), int(y)))
                x += img.size[0] + margin_size
            y += int(init_height / coef) + margin_size
    collage_image.save(filename)
    return True

root = 'path/'

client_credentials_manager = SpotifyClientCredentials(client_id='client_id',
                                                      client_secret='client_secret')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

if not os.path.exists(root):
    os.makedirs(root)

uri_playlist = 'uri'

#format of uri: spotify:user:X:playlist:X
#Example: my top 100 2018 :) spotify:user:pni7wap5hz63vkm7171v8ki4t:playlist:5IPFs3X63PmgGnfjqAtO2e

username = uri_playlist.split(':')[2]
playlist_id = uri_playlist.split(':')[4]

results = sp.user_playlist_tracks(username, playlist_id)
items = results['items']


for item in items:
    url = item['track']['album']['images'][0]['url']
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    name = re.sub('\W+','', item['track']['album']['name'])
    #img.save(root + name + '.bmp')
    img.save(root + name + '.jpg', "JPEG", quality=80, optimize=True, progressive=True)


files = [os.path.join(root, fn) for fn in os.listdir(root)]
images = [fn for fn in files if os.path.splitext(fn)[1].lower() in ('.jpg')]
res = make_collage(images, root + '0_collage.jpg', 7000, 640)

