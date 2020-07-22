import os

from dotenv import load_dotenv
from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
)

load_dotenv()
app = Flask(__name__)
app.secret_key = "ssssh don't tell anyone"

if __name__ == '__main__':
    app.run()
