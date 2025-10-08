# guess.py
# "Guess the Air!" web version - Phase 2: API connection test

from flask import Flask, render_template, request, redirect, url_for
import requests
import random

# Initialize Flask app
app = Flask(__name__)

# API token for World Air Quality Index
TOKEN = "81fb791c686ee1a615e96b00aa157e6f186d216c"

def get_city_data(city):
    
    url = "https://api.waqi.info/search/"
    response = requests.get(url, params={"token": TOKEN, "keyword": city})
    data = response.json()
    if data["status"] == "ok" and len(data["data"]) > 0:
        return data["data"][0]
    else:
        return None

# Homepage route : welcome message + start game
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)