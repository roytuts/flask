from flask import Flask
from flask_caching import Cache

config = {
    "DEBUG": True,  # run app in debug mode
    "CACHE_TYPE": "SimpleCache",  # caching type
    "CACHE_DEFAULT_TIMEOUT": 300 # default Cache Timeout
}

app = Flask(__name__)

# Flask to use the above defined config
app.config.from_mapping(config)

cache = Cache(app)