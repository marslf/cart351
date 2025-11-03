# guess_terminal.py
# Converted from Flask web app to terminal-based game

# Sound Credits (original web version):
# "Air Puff" by waymonds (2025) — https://freesound.org/people/waymonds/sounds/817695/
# "Bell ding 3.wav" by 5ro4 (2021) — https://freesound.org/people/5ro4/sounds/611111/
# Both used under Creative Commons license from Freesound.org

import requests
import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

# --- Constants ---
TOKEN = "81fb791c686ee1a615e96b00aa157e6f186d216c"

EASY_CITIES = ["Montreal", "Toronto", "New York", "London", "Paris", "Tokyo", "Sydney", "Lisbon", "Singapore"]
MEDIUM_CITIES = EASY_CITIES + [
    "Beijing", "Mexico City", "Rio de Janeiro", "Moscow", "Bangkok", "Delhi",
    "Los Angeles", "Berlin", "Madrid", "Rome", "Edinburgh", "Monaco"
]
HARD_CITIES = [
    "Montreal", "Toronto", "Vancouver", "New York", "Los Angeles", "Chicago", "Mexico City", "Houston",
    "Miami", "San Francisco", "Boston", "Washington D.C.", "Seattle", "Atlanta", "Denver",
    "Buenos Aires", "Rio de Janeiro", "São Paulo", "Santiago", "Lima", "Bogotá", "Quito",
    "London", "Paris", "Berlin", "Rome", "Madrid", "Lisbon", "Amsterdam", "Brussels", "Copenhagen", "Stockholm",
    "Tokyo", "Seoul", "Beijing", "Shanghai", "Hong Kong", "Singapore", "Bangkok", "Delhi", "Mumbai", "Kolkata",
    "Cairo", "Lagos", "Johannesburg", "Cape Town", "Casablanca", "Accra",
    "Sydney", "Melbourne", "Auckland", "Brisbane", "Perth"
]

# --- Helper functions ---

def get_city_data(city):
    """Fetch live air quality data for a city."""
    url = "https://api.waqi.info/search/"
    try:
        response = requests.get(url, params={"token": TOKEN, "keyword": city}, timeout=5)
        data = response.json()
        if data["status"] == "ok" and len(data["data"]) > 0:
            aqi = data["data"][0]["aqi"]
            if isinstance(aqi, int) or aqi.isdigit():
                return int(aqi)
        return None
    except Exception:
        return None


def get_two_cities(difficulty):
    """Pick two random cities based on difficulty level."""
    if difficulty == "easy":
        cities = EASY_CITIES
    elif difficulty == "medium":
        cities = MEDIUM_CITIES
    else:
        cities = HARD_CITIES
    return random.sample(cities, 2)


def print_with_delay(text, delay=0.5):
    """Helper to make output feel more dynamic."""
    print(text)
    time.sleep(delay)


# --- Main Game Loop ---
def play_game():
    print(Fore.CYAN + Style.BRIGHT + "\n🌍 Welcome to 'Guess the Air!' 🌤️\n")
    print("Your goal is to guess which city has cleaner air (lower AQI).")
    print("You start with 3 lives ❤️. Each wrong guess costs one life.\n")

    difficulty = input("Choose difficulty (easy / medium / hard): ").strip().lower()
    if difficulty not in ["easy", "medium", "hard"]:
        difficulty = "easy"

    score = 0
    lives = 3

    while lives > 0:
        city1, city2 = get_two_cities(difficulty)

        print_with_delay(Fore.YELLOW + f"\nFetching air quality data for {city1} and {city2}...")
        aqi1 = get_city_data(city1)
        aqi2 = get_city_data(city2)

        if not aqi1 or not aqi2:
            print(Fore.RED + "⚠️ Couldn't fetch data for one of the cities, retrying...\n")
            continue

        print(Fore.CYAN + f"\n🌆 1. {city1}\n🌇 2. {city2}")
        guess = input(Fore.WHITE + "\nWhich city do you think has cleaner air? (1 or 2): ").strip()

        correct_city = city1 if aqi1 < aqi2 else city2
        correct_aqi = min(aqi1, aqi2)

        if (guess == "1" and correct_city == city1) or (guess == "2" and correct_city == city2):
            print(Fore.GREEN + Style.BRIGHT + "\n✅ Correct! The air is cleaner in " + correct_city)
            print(f"AQI: {correct_aqi}")
            score += 1
        else:
            print(Fore.RED + Style.BRIGHT + "\n❌ Wrong! The cleaner air was in " + correct_city)
            print(f"AQI: {correct_aqi}")
            lives -= 1

        print(Fore.MAGENTA + f"\nScore: {score} | Lives: {'❤️ ' * lives}\n")
        time.sleep(1)

    # Game Over screen
    total_rounds = score + (3 - lives)
    accuracy = (score / total_rounds * 100) if total_rounds > 0 else 0
    mood_icon = "🌞" if accuracy >= 60 else "🌤️" if accuracy >= 30 else "☁️"

    print(Fore.BLUE + Style.BRIGHT + "\n--- GAME OVER ---")
    print(f"Final Score: {score}")
    print(f"Accuracy: {accuracy:.1f}% {mood_icon}")
    print("\nThanks for playing 'Guess the Air!' 💨\n")


if __name__ == "__main__":
    play_game()
