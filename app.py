"""Take a biorxiv identifier and resolves the link to the pdf
"""

import flask
from flask import Flask

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def test_parse_page():
    pass

def parse_page(html):
    soup = BeautifulSoup(html, "lxml")

    a = soup.find_all("a", {"class": "article-dl-pdf-link"})[0]
    url = a.attrs['href']
    
    return 'https://www.biorxiv.org' + url

@app.route('/<string:paper_id>')
def pages(paper_id):
    """Take the paper_id and returns the pdf url
    """
    url = "https://www.biorxiv.org/content/10.1101/{}".format(paper_id)
    r = requests.get(url)
    try:
        url = parse_page(r.text)
        return flask.redirect(url)
    except:
        return flask.abort(400)

if __name__ == "__main__":
    app.run(debug=True, threaded=True, use_reloader=False)
