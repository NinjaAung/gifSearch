from flask import Flask, render_template, request, url_for
import requests
import json

app = Flask(__name__)

# params = {
#     "q": query_term,
#     "Key": "WL6NLFPEQRYR"
# }


@app.route('/')
def index():
    """Return homepage."""
    q = request.args.get('q')
    params = { 
        "q": q, 
        "key": "UFXFWLXQEZ03", 
        "limit": 8 
        }

    response = requests.get(
    'https://api.tenor.com/v1/search', params=params)

    gif_json = response.json()
    gif_urls = gif_json['results']

    return render_template("index.html", gif_urls=gif_urls, q=q)

    # if response.status_code == 200:
    #     gifs_results = json.loads(response.content)
    #     gif_urls = gifs_results["results"]
    #     # print(gifs_results['results'])
    #     # print(gifs_results['results'][0]['media'][0]['gif']['url'])
    #     return render_template("index.html", gif_urls=gif_urls, q=q)
    # else:
    #     return "Search in valid"


    # elif request.args.get["action"] == "Random":
    #     pass

def api_choice(api):
    return f'https://api.tenor.com/v1/{api}?key=UFXFWLXQEZ03&limit=10'


@app.route('/trending')
def trending():
    response = requests.get(api_choice('trending'))
    gif_json = response.json()
    gif_urls = gif_json['results']    
    return render_template("top10.html", gif_urls=gif_urls)

    # TODO: Extract the query term from url using request.args.get()

    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'

    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    # return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
