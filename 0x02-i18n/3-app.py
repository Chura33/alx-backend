#!/usr/bin/env python3
"""Setup a basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

# Configure Babel
babel = Babel(app)


class Config:
    """Configuration class for the Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Determine the best match for the user's preferred language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Return custom messages
    according to language
    """
    return render_template(
        '3-index.html',
        title=_('home_title'),
        greeting=_('home_header')
    )


# _ function documentation
_.__doc__ = """
Translate a message.

This function is used for marking strings for translation.
It is commonly used as a shorthand for marking strings in Flask applications.

Returns:
    str: The translated string.
"""    


if __name__ == '__main__':
    """run the app"""
    app.run(debug=True)
