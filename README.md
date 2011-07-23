# Web Imagery

## What to use it for

Grab images from the web by their urls

Currently supports:

* direct image links that have the following extensions (jpg, jpeg, gif, png)
* Instagram
* Imgur
* Flickr
* Twitpic
* Path

## Requirements

>> pip install -r requirements.txt

## Usage

>> from webimagery import *

>> image = WebImagery()

First set the url

>> image.set_image('http://www.flickr.com/photos/ednapiranha/4437021184/')
>> True

You can get the source link

>> image.get_image()
>> 'http://farm3.static.flickr.com/2788/4437021184_848d7fa79d.jpg'

Or you can get the image tag, setting your own alt text and dimensions

>> image.get_image_as_html('cat sleeping')
>> image.width = 350
>> '<img src="http://farm3.static.flickr.com/2788/4437021184_848d7fa79d.jpg" alt="cat sleeping" width="350" height="200" />'