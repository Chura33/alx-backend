#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

def index() -> str:
    """Renders the index.html template."""
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
