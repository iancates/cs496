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
    time_url = "http://www.timeapi.org/pdt/now?\\a%20\\b%20\\d%20\\I:\\M:\\S%20\\Y"
    current_time = urlfetch.fetch(time_url).content
    # second request = weather
    weather_url = "http://api.openweathermap.org/data/2.5/weather?zip=83843,us&appid=a0b1ce364984d3df0147915a50d2ce7d"
    weather = urlfetch.fetch(weather_url).content
    json_weather = json.loads(weather)  # convert string to json dict so we can parse it
    current_temp = json_weather["main"]["temp"]
    return "Greetings from Moscow, ID. It is currently {0}, and the temperature is approximately {1} Kelvin.".format(current_time, current_temp)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
