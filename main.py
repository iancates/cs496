from flask import Flask
import json
from google.appengine.api import urlfetch
app = Flask(__name__)
app.config['DEBUG'] = True




@app.route('/')
def hello():

    return "Test"

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
