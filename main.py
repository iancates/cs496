from flask import Flask
import json
from google.appengine.api import urlfetch
app = Flask(__name__)
app.config['DEBUG'] = True




@app.route('/')
def hello():
    url = 'http://www.timeapi.org/pdt/now?format=%25a%20%25b%20%25d%20%25I:%25M:%25S%20%25Z%20%25Y'
    #url = 'http://www.google.com/humans.txt'
    result = urlfetch.fetch(url)
    return result.content



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


