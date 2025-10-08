from flask import Flask, render_template, request, redirect, url_for
import requests
import random

# --- GAME SETTINGS ---
# list of cities to randomly pick from
CITIES = ["Montreal", "Tokyo", "Paris", "Mexico City", "Toronto", "Beijing", "New York", "Sydney", "London", "Delhi"]

#dictionary to keep track of score
score = {"points": 0}


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
    
# pick 2 different random cities
def get_two_cities():
    city1, city2 = random.sample(CITIES, 2)
    return city1, city2


# HOMEPAGE ROUTE
@app.route("/")
def index():
    return render_template("index.html")


# MAIN GAME ROUTE 
@app.route("/game")
def game():
    # pick two random cities
    city1, city2 = get_two_cities()

    # get their air data
    data1 = get_city_data(city1)
    data2 = get_city_data(city2)

    # make sure both cities returned valid data
    if not data1 or not data2:
        return redirect(url_for("game"))  # retry if something failed

    # get their AQI values
    aqi1 = int(data1["aqi"]) if data1["aqi"].isdigit() else 999
    aqi2 = int(data2["aqi"]) if data2["aqi"].isdigit() else 999

    # pass data to template
    return render_template("game.html", city1=city1, city2=city2, aqi1=aqi1, aqi2=aqi2, points=score["points"])


# CHECK WHICH CITY IS CLEANER 
@app.route("/guess", methods=["POST"])
def guess():
    # get form data from the HTML buttons
    chosen_city = request.form.get("city")
    city1 = request.form.get("city1")
    city2 = request.form.get("city2")
    aqi1 = int(request.form.get("aqi1"))
    aqi2 = int(request.form.get("aqi2"))

    # determine which city is cleaner (lower AQI = cleaner air)
    correct_city = city1 if aqi1 < aqi2 else city2

    # check if user guessed right
    if chosen_city == correct_city:
        score["points"] += 1
        result = "Correct! 🌿"
    else:
        result = "Wrong! 💨"

    # show result screen
    return render_template("result.html", result=result, correct_city=correct_city, points=score["points"])

if __name__ == "__main__":
    app.run(debug=True)