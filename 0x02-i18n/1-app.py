#!/usr/bin/env python3
"""Setup a basic Flask app"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


# Configure Babel
babel = Babel(app)


class Config:
    """Configuration class for the Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """returns index.html"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
