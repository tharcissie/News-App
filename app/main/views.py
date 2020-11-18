from flask import render_template,request,redirect,url_for
from app import main
from app import app
from ..request import get_sources,get_news

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and
    its data
    '''

    #get sources
    
    entertainment_ = get_sources('entertainment')
    general_ = get_sources('general')
    sports_ = get_sources('sports')
    business_ = get_sources('business')
    technology_ = get_sources('technology')
    science_ = get_sources('science')
    health_ = get_sources('health')
    print(health_)

    title = 'Home - Welcome'
    return render_template('index.html',business = business_,health=health_,science=science_,title=title,sports = sports_, technology = technology_,entertainment = entertainment_ ,general=general_)

@app.route('/news/<id>')
def news(id):
    '''
    view page function that returns both the news 
    '''
    news = get_news(id)
    print(news)
    title = 'Home - Welcome'

    return render_template('news.html', news=news, title=title)