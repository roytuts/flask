from flask import Flask

config = {
    "DEBUG": True  # run app in debug mode
}

app = Flask(__name__)

# Flask to use the above defined config
app.config.from_mapping(config)