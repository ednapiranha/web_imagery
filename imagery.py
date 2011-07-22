import urllib

from types import *
from urlparse import urlparse
from pyquery import PyQuery as pq

SERVICE_DEFAULT = 'web'
SERVICE_INSTAGRAM = 'instagram'
SERVICE_IMGUR = 'imgur'
SERVICE_TWITPIC = 'twitpic'
SERVICE_FLICKR = 'flickr'
SERVICE_PATH = 'path'

def set_natural_num(val):
    """
    if a negative number is passed in, force it to be positive. 
    e.g. -300 will return as 300
    """
    if val >= 0 and type(val) is IntType:
        return val
    else:
        val = val * -1
        return val

class WebImagery():
    
    def __init__(self):
        self.width = ''
        self.height = ''
        self.service = ''
        self.url = ''
    
    def set_dimensions(self, width=200, height=200):
        """
        set the width and height, if not provided, it defaults to 200x200
        """
        self.width = set_natural_num(width)
        self.height = set_natural_num(height)
    
    def set_image(self, url):
        """
        detect whether a url contains an image in our list of supported services
        """
        url = self.url = urlparse(url)

        if 'http' in url.scheme and self.__set_service():
            return True
        else:
            return False
    
    def get_image(self):
        """
        if this is a direct image link, just send that back
        if not, we need to scrape the image service site for the proper element that contains the direct image link
        """
        
        url = self.url
        url_path = url.scheme + "://" + url.netloc + url.path
        if self.service == SERVICE_DEFAULT:
            return url_path
        else:
            page = pq(url=url_path)

            if self.service == SERVICE_INSTAGRAM:
                return page('img.photo').attr('src')
            elif self.service == SERVICE_IMGUR:
                return page('img.photo').attr('src')
            elif self.service == SERVICE_TWITPIC:
                return page('#photo img.photo').attr('src')
            elif self.service == SERVICE_FLICKR:
                return page('#photo .photo-div img').attr('src')
            elif self.service == SERVICE_PATH:
                return page('.photo-background img.photo').attr('src')
            else:
                return ""
    
    def __set_service(self):
        """"
        if the url matches 
        """
        url = self.url

        if url.path.lower().endswith('jpg') or \
            url.path.lower().endswith('jpeg') or \
            url.path.lower().endswith('gif') or \
            url.path.lower().endswith('png'):
            
            self.service = SERVICE_DEFAULT
            return True
        elif 'instagr' in url.netloc:
            self.service = SERVICE_INSTAGRAM
            return True
        elif 'imgur' in url.netloc:
            self.service = SERVICE_IMGUR
            return True
        elif 'twitpic' in url.netloc:
            self.service = SERVICE_TWITPIC
            return True
        elif 'flickr' in url.netloc:
            self.service = SERVICE_FLICKR
            return True
        elif 'path' in url.netloc:
            self.service = SERVICE_PATH
            return True
        else:
            return False