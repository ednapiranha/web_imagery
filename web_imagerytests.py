import unittest
from web_imagery import *

class WebImageryTestCase(unittest.TestCase):
    def setUp(self):
        self.image = WebImagery()
        
    def tearDown(self):
        self.image = None
    
    def testWidthOrHeightIsPositive(self):
        """
        verify that setting dimensions always returns positive integers
        """
        self.image.set_dimensions(-100, -300)
        self.assertEqual(self.image.width, 100)
        self.assertEqual(self.image.height, 300)
        
    def testImageIsValid(self):
        """
        verify image is valid
        """
        self.assertEqual(self.image.set_image('http://www.flickr.com/photos/ednapiranha/4437021184/'), True)
        
    def testImageIsInvalid(self):
        """
        verify image is invalid
        """
        self.assertEqual(self.image.set_image('http://www.google.com'), False)
    
    def testImageSourceFound(self):
        """
        verify the source is found for one of the services
        """
        self.image.set_image('http://www.flickr.com/photos/ednapiranha/4437021184/')
        self.assertEqual(self.image.get_image(), "http://farm3.static.flickr.com/2788/4437021184_848d7fa79d.jpg")
    
    def testImageHtmlGenerated(self):
        """
        verify the html version of the image is returned
        """
        self.image.set_image('http://www.flickr.com/photos/ednapiranha/4437021184/')
        self.assertEqual(self.image.get_image_as_html('alt_text'), '<img src="http://farm3.static.flickr.com/2788/4437021184_848d7fa79d.jpg" alt="alt_text" width="200" height="200" />')

if __name__ == '__main__':
    unittest.main()