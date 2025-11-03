from flask import Flask,render_template,request, json, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads' # Or os.path.join(app.instance_path, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB limit

# the default route
@app.route("/")
def index():
      return render_template("index.html")

#*************************************************
#Task: CAPTURE & POST & FETCH & SAVE
@app.route("/t2")
def t2():
    return render_template("t2.html")

#route to receive star data and save to file
@app.route("/postDataFetch", methods=['POST'])
def postDataFetch():
    data = request.get_json()
    stars = data.get("stars", []) #get star coords

    filepath = os.path.join("files", "data.txt")

    #convert data to JSON string with indentation
    data_to_save = {"stars": stars}
    data_s = json.dumps(data_to_save, indent=4)

    # Open file in append mode
    with open(filepath, "a") as f:
        f.write(data_s + "\n")  # Add newline between constellations

    print("Saved stars:", stars) #log in terminal

    # Send JSON response to client
    return jsonify({"message": f"✨ Saved {len(stars)} stars as a constellation!"})
#*************************************************
#run
app.run(debug=True)