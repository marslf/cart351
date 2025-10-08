from flask import Flask, render_template, request, redirect, url_for
import requests
import random


# list of cities to randomly pick from based on difficulty level

# EASY = well-known popular cities
EASY_CITIES = ["Montreal", "Toronto", "New York", "London", "Paris", "Tokyo", "Sydney", "Lisbon", "Singapore"]

# MEDIUM = mix of well-known + slightly unusual
MEDIUM_CITIES = EASY_CITIES + [
    "Beijing", "Mexico City", "Rio de Janeiro", "Moscow", "Bangkok", "Delhi", "Los Angeles", "Berlin", "Madrid", "Rome", "Edinburgh", "Monaco", "Lisbon", "Singapore"
]

# HARD = the full long list you asked for
HARD_CITIES = [
    "Montreal", "Toronto", "Vancouver", "New York", "Los Angeles", "Chicago", "Mexico City", "Houston",
    "Miami", "San Francisco", "Boston", "Washington D.C.", "Seattle", "Atlanta", "Denver",
    "Buenos Aires", "Rio de Janeiro", "São Paulo", "Santiago", "Lima", "Bogotá", "Quito", "Caracas", "Montevideo", "La Paz",
    "London", "Paris", "Berlin", "Rome", "Madrid", "Lisbon", "Amsterdam", "Brussels", "Copenhagen", "Stockholm",
    "Oslo", "Helsinki", "Warsaw", "Vienna", "Athens", "Prague", "Budapest", "Dublin", "Zurich", "Edinburgh",
    "Tokyo", "Seoul", "Beijing", "Shanghai", "Hong Kong", "Singapore", "Bangkok", "Delhi", "Mumbai", "Kolkata",
    "Karachi", "Jakarta", "Kuala Lumpur", "Manila", "Tehran", "Baghdad", "Riyadh", "Dhaka",
    "Cairo", "Lagos", "Nairobi", "Johannesburg", "Cape Town", "Casablanca", "Accra", "Addis Ababa", "Dakar", "Algiers",
    "Sydney", "Melbourne", "Auckland", "Wellington", "Brisbane", "Perth", "Adelaide", "Hobart",
    "Reykjavik", "Tallinn", "Vilnius", "Luxembourg", "Valletta", "Monaco", "San Marino", "Andorra la Vella", "Vaduz"
]

#GAME STATS
score = {"points": 0}
lives = {"count": 3}


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
    
# PICK 2 RANDOM CITIES depending on DIFFICULTY
def get_two_cities(difficulty):
    if difficulty == "easy":
        cities = EASY_CITIES
    elif difficulty == "medium":
        cities = MEDIUM_CITIES
    else:
        cities = HARD_CITIES

    city1, city2 = random.sample(cities, 2)
    return city1, city2


# ----- ROUTES -----

# HOMEPAGE ROUTE
@app.route("/")
def index():
    score["points"] = 0  # reset score
    lives["count"] = 3  # reset lives
    return render_template("index.html")


# GAME ROUTE 
@app.route("/game")
def game():
    # get difficulty from homepage buttons (default = easy)
    difficulty = request.args.get("difficulty", "easy")

    current_lives = int(request.args.get("lives", lives["count"]))
    lives["count"] = current_lives

    # pick two random cities
    city1, city2 = get_two_cities(difficulty)
    # get their air data
    data1 = get_city_data(city1)
    data2 = get_city_data(city2)

    # make sure both cities returned valid data
    if not data1 or not data2:
        return redirect(url_for("game"))  # retry if fail

    # get their AQI values
    aqi1 = int(data1["aqi"]) if data1["aqi"].isdigit() else 999
    aqi2 = int(data2["aqi"]) if data2["aqi"].isdigit() else 999

    cloud_count = 0
    if difficulty == "easy":
        cloud_count = 3
    elif difficulty == "medium":
        cloud_count = 6
    elif difficulty == "hard":
        cloud_count = 9

    clouds = []
    for _ in range(cloud_count):
        clouds.append({
            "top": random.randint(5, 200), # y position
            "left": random.randint(-10, 80), # starting x position
            "duration": random.randint(25, 45) # movement speed
        })
        
    return render_template("game.html",
                       city1=city1, city2=city2,
                       aqi1=aqi1, aqi2=aqi2,
                       points=score["points"],
                       difficulty=difficulty,
                       lives=lives["count"],
                       clouds=clouds)


# CHECK WHICH CITY IS CLEANER 
@app.route("/guess", methods=["POST"])
def guess():
    # get form data from player input (HTML buttons)
    chosen_city = request.form.get("city")
    city1 = request.form.get("city1")
    city2 = request.form.get("city2")
    aqi1 = int(request.form.get("aqi1"))
    aqi2 = int(request.form.get("aqi2"))
    difficulty = request.form.get("difficulty")
    current_lives = int(request.form.get("lives", lives["count"]))
    lives["count"] = current_lives

    # determine which city is cleaner (lower AQI = cleaner air)
    correct_city = city1 if aqi1 < aqi2 else city2

    # check answer
    if chosen_city == correct_city:
        score["points"] += 1
        result = "Correct! 🌿"
    else:
        result = "Wrong! 💨"
        lives["count"] = max(0, current_lives - 1)

    # if lives = 0 = game over 
    if lives["count"] <= 0:
        return render_template("gameover.html", points=score["points"])

    # show result screen
    return render_template("result.html", 
                           result=result, 
                           correct_city=correct_city, 
                           points=score["points"], 
                           difficulty=difficulty,
                           lives=lives["count"])

if __name__ == "__main__":
    app.run(debug=True)