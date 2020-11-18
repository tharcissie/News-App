from app import app
import urllib.request,json
from .models import Source, News

#getting api key
api_key = None

#getting news base url
source_url = None
news_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key=app.config['NEWS_API_KEY']
    source_url=app.config['SOURCE_API_BASE_URL']
    news_url=app.config['NEWS_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets json response to our url request
    '''
    get_sources_url = source_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results

def process_sources(sources_list):
    '''
    function that processes the news results and transform them to a list of objects
    Args:
        sources_list: A list of dictionaries that contain news details
    Returns:
        sources_results: Alist of news source objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
       

        if id:
            sources_object = newssource(id,name,description,url,category)
            sources_results.append(sources_object)
    return sources_results

def get_news(id):
    '''
    Function that gets the json response to url request
    '''
    get_news_url = news_url.format(id,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news(news_results_list)

    return news_results

def process_news(news_list):
    '''
    process the dictionary and output a list of objects
    '''
    news_results = []
    source_dictionary = {}
    for result in news_list:
        source_id = result ['source']
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        id = source_dictionary['id']
        name = source_dictionary['name']

        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        
        if urlToImage:
            print (id)
            news_object = newsarticle(id,name,author,title,description,url,urlToImage)
            news_results.append(article_object)

    return news_results