from flask import Flask, render_template, request
from lxml import html
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        websiteAddress = str(request.form['websiteAddress'])
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
        title = title.replace("']", '')
        title = title.replace("',", '')
        title = title.replace("'", '')
        paragraphs = str(tree.xpath('//p/text()'))
        paragraphs = paragraphs.replace("['", '')
        paragraphs = paragraphs.replace("']", '')
        paragraphs = paragraphs.replace("',", '')
        paragraphs = paragraphs.replace("'", '')
        
        return render_template('evaluation.html', websiteAddress=paragraphs)