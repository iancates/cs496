from flask import Flask
import json
from google.appengine.api import urlfetch
app = Flask(__name__)
app.config['DEBUG'] = True




@app.route('/')
def hello():
  time_url = "http://www.timeapi.org/pdt/now?\a \b \d \I:\M:\S \Z \Y"
  current_time = urlfetch.fetch(time_url).content
  return "test {0}".format(current_time)
  

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
