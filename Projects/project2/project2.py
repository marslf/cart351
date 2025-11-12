# 1. IMPORTS
from flask import Flask, render_template, request, jsonify
import os, json

# 2. APP SETUP
app = Flask(__name__)

# 3. Ensure files folder exists
os.makedirs("files", exist_ok=True)
DATA_FILE = os.path.join("files", "creatures.json")

# 4. Helper: load creatures (returns list)
def load_creatures():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# 5. Helper: save creatures list
def save_creatures(creatures):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(creatures, f, indent=2)

# 6. ROUTES
#Home
@app.route("/")
def index():
    return render_template("index.html")

#Create page
@app.route("/create")
def create_page():
    return render_template("create.html")

#Community pond page
@app.route("/pond")
def pond_page():
    return render_template("pond.html")

#POST endpoint: receive new creature, save to JSON
@app.route("/postCreature", methods=["POST"])
def post_creature():
    data = request.get_json() or {}
    # expected fields: type, name, color
    ctype = data.get("type", "frog")
    name = data.get("name", "anon")
    color = data.get("color", None)

    # make a simple creature record with a random-ish position 
    # store timestamp-ish id or allow client to send x,y
    creature = {
        "type": ctype,
        "name": name,
        "color": color,
    }

    creatures = load_creatures()
    creatures.append(creature)
    save_creatures(creatures)

    return jsonify({"message": f"Saved {name} the {ctype}!", "count": len(creatures)})

# 6.5 GET endpoint: return all creatures JSON
@app.route("/getCreatures")
def get_creatures():
    creatures = load_creatures()
    return jsonify({"creatures": creatures})

# 7. RUN
if __name__ == "__main__":
    app.run(debug=True)