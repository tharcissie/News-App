class Source:
    '''
    source of news
    '''
    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        

class News:
    '''
    class for news from source
    '''
    def __init__(self,id,name,author,title,description,url,urlToImage,):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage