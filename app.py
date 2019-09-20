from flask import Flask, render_template, request, url_for
import requests
import json

app = Flask(__name__)


def api_choice(api):
    '''
    A function that simplifys api choice for other functions.
    Args:
        api (string): a string literal that specify what the user requests, Random, Trending, ETC
    Returns: 
        string:r returns link with the give Args 
    '''
    return f'https://api.tenor.com/v1/{api}?key=UFXFWLXQEZ03&limit=12'


@app.route('/')
def index():
    '''
    Return homepage

    A function that returns User to the homepage and parses random gifs
    Returns: 
        rendur_template: renders index.html for the Flask framework
        params: paramaters in the api that query the results in the html

    '''
    q = request.args.get('q')
    params = { 
        "q": q, 
        "key": "UFXFWLXQEZ03", 
        "limit": 12
        }

    response = requests.get(
    'https://api.tenor.com/v1/search', params=params)

    gif_json = response.json()
    gif_urls = gif_json['results']

    return render_template("index.html", gif_urls=gif_urls, q=q)



# Begginign ouput is already random just hit refresh
@app.route('/random')
def random():
    '''
    A function that renders the output.html and spits out random gifs for the page.
        Uses: api_choices function: to parse random
    Returns: 
           render_template: renders output.html and parses in html file for random
           gif_url: json library of the gif dictionary 
    '''
    response = request.get(api_choice('trending'))
    gif_json = response.json()
    gif_urls = gif_json['results']
    return render_template("output.html", gif_urls=gif_urls)


@app.route('/trending')
def trending():
    '''
    A function that renders the output.html and spits out trending gifs for the page.
        Uses: api_choices function: to parse trending
    Returns: 
           render_template: renders output.html and parses in html file for trending page
           gif_url: json library of the gif dictionary 
    '''
    response = requests.get(api_choice('trending'))
    gif_json = response.json()
    gif_urls = gif_json['results']    
    return render_template("output.html", gif_urls=gif_urls)


if __name__ == '__main__':
    app.run(debug=True)
