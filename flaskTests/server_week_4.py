from flask import Flask,render_template
app = Flask(__name__)

#BASIC / MAIN ROUTE
@app.route('/')
def index():
    return render_template("pineapples.html")

@app.route('/another')
def another():
    return render_template("pineapples_2.html")

app.run(debug=True)
@app.route('/three')
def three():
    someNewVar = "Sabine"
    return render_template("pineapples_3.html", my_variable = someNewVar)