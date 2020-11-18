class News_Source:
    
    #newssource class to define news objects
    
    def __init__(self,id,name,url,category):
        self.id = id
        self.name = name
        self.url = url
        self.category = category
        

class News_Article:
    
    #newsarticle class to define article objects
    
    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        