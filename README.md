# Web Imagery

## What to use it for

Grab images from the web by their urls

Currently supports:

* direct image links that have the following extensions (jpg, jpeg, gif, png)
* Instagram
* Imgur
* Flickr
* Path

## Requirements

>> pip install -r requirements.txt

## Usage

>> from web_imagery import web_imagery as wb

>> image = wb.WebImagery()

First set the url

>> image.set_image('http://www.flickr.com/photos/ednapiranha/4437021184/')

>> True

You can get the source link

>> image.get_image()

>> 'http://farm3.static.flickr.com/2788/4437021184_848d7fa79d.jpg'

Or you can get the image tag, setting your own alt text and dimensions

>> image.get_image_as_html('cat sleeping')

>> image.width = 350

>> '&lt;img src="http://farm3.static.flickr.com/2788/4437021184_848d7fa79d.jpg" alt="cat sleeping" width="350" height="200" /&gt;'