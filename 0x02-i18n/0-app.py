#!/usr/bin/env python3
"""a simple flask page"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """ endpoint for / """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
