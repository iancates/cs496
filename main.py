from flask import Flask
import json
from google.appengine.api import urlfetch
app = Flask(__name__)
app.config['DEBUG'] = True




@app.route('/')
def hello():
   url = "http://api.openweathermap.org/data/2.5/weather?zip=83843,us&appid=a0b1ce364984d3df0147915a50d2ce7d"
    weatherFetch = urlfetch.fetch(url).content
    weather = json.loads(weatherFetch)
    temp = weather["main"]["temp"]
    
    return "The current temperature is {0}".format(temp) 

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
