from flask import Flask, render_template, request, json
from lxml import html
import requests
import http.client
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    conservativeNewsSources = ['foxnews.com', 'newyorkpost', 'dailymail.com', 'infowars.com', 'forbes.com', 'nationalreview.com', 'wnd.com', 'townhall.com', 'breitbart.com']
    liberalNewsSources = ['abcnews.go.com', 'usatoday.com', 'latimes.com', 'wsj', 'politico.com', 'telemundo.com', 'bloomberg.com', 'wp.com', 'nyt.com', 'theatlantic.com', 'wired.com', 'news.vice.com', 'cbsnews.com', 'msnbc.com', 'bbcnews.com', 'time.com', 'nbcnews.com']
    centristNewsSources = ['c-span', 'apnews.com', 'upi', 'thehill.com', 'npr.org', 'reuters.com', 'militarytimes.com']
    
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        websiteAddress = str(request.form['websiteAddress'])
        topic = str(request.form['topic'])
        websiteLean = 'unknown'
        if any(x in websiteAddress.lower() for x in conservativeNewsSources):
            websiteLean = 'conservative'
        elif any(x in websiteAddress.lower() for x in liberalNewsSources):
            websiteLean = 'liberal'
        elif any(x in websiteAddress.lower() for x in centristNewsSources):
            websiteLean = 'centrist'     
        else:
            websiteLean = 'other'

        if websiteAddress[0:7] == 'http://':
            page = requests.get(websiteAddress)
        elif websiteAddress[0:8] == 'https://':
            page = requests.get(websiteAddress)
        else: 
            websiteAddress = 'http://' + websiteAddress
            page = requests.get(websiteAddress)
        tree = html.fromstring(page.content)
        title = str(tree.xpath('//title/text()'))
        title = title.replace("['", '')
        title = title.replace('["', '')
        title = title.replace("']", '')
        title = title.replace('"]', '')
        title = title.replace("',", '')
        title = title.replace("'", '')
        title = title.replace(' ', '%20')
        title = title.replace('|', '%20')

        return render_template('evaluation.html', topic=topic, websiteLean=websiteLean, title=title, websiteAddress=websiteAddress)