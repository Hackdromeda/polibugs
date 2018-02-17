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
        if websiteAddress[0:8] == 'http://' or websiteAddress[0:9] == 'https://':
            page = requests.get(websiteAddress)
            tree = html.fromstring(page.content)
            return render_template('index.html', websiteAddress=websiteAddress)