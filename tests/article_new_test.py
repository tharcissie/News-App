import unittest
from app.models import News_Article

class NewsArticleTest(unittest.TestCase):
    
    #Test the article class
    
    def setUp(self):
        
        #Setup method that will run before every test
       
        self.new_article = News_Article('a','b','c','d','efg hij klmn','www.o.com/','www.o.com/p.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
