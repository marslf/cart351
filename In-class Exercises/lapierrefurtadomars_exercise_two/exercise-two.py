from flask import Flask,render_template,request
import os
app = Flask(__name__)


# the default route
@app.route("/")
def index():
      return render_template("index.html")

#*************************************************

#Task: Variables and JinJa Templates
@app.route("/t1")
def t1():
    the_topic = "donuts"
    number_of_donuts = 28
    donut_data = {
        "flavours": ["Regular", "Chocolate", "Blueberry", "Devil's Food"],
        "toppings": [
            "None", "Glazed", "Sugar", "Powdered Sugar",
            "Chocolate with Sprinkles", "Chocolate", "Maple"
        ]
    }
    icecream_flavors = ["Vanilla", "Raspberry", "Cherry", "Lemon"]


    return render_template(
        "t1.html",
        topic=the_topic,
        count=number_of_donuts,
        donut_data=donut_data,
        icecreams=icecream_flavors
    )

#*************************************************

#Task: HTML Form get & Data 
@app.route("/t2")
def t2():
    return render_template("t2.html")

@app.route("/thank_you_t2")
def thank_you_t2():
    name = request.args.get("name")
    color = request.args.get("color")
    message = request.args.get("message")

    combined = f"{name} {color} {message}"

    modified = ""
    for char in combined:
        if char.lower() in "aeiou":
            modified += "*"
        else:
            modified += char

    return render_template("thank_you_t2.html", modified_text=modified)

#*************************************************

#run
app.run(debug=True)