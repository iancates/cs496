from flask import Flask
import json
from google.appengine.api import urlfetch
app = Flask(__name__)
app.config['DEBUG'] = True




@app.route('/')
def hello():
   """
    Return the current time and weather by making two separate requests to:
    (1)timeapi.org
    (2)openweathermap.org
    """
    # first request = time
    time_url = "http://www.timeapi.org/pdt/now?\a \b \d \I:\M:\S \Z \Y"
    current_time = urlfetch.fetch(time_url).content
    return "Test"

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
