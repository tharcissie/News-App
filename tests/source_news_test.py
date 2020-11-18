import unittest
from app.models import News_Source

class NewsSourceTest(unittest.TestCase):
    
    #Test  news source class
    
    def setUp(self):
        
        #set up method that will run before every test
        
        self.new_news = News_Source('a','b','www.d.com',"e")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':