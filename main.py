from flask import Flask
import datetime
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


current_time = datetime.datetime.now().time()
current_time.isoformat()
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return current_time


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
