from flask import Flask,render_template,request
app = Flask(__name__)
# a route
@app.route('/')
def index():
    return render_template("index.html")
 
@app.route('/p5Test')
def p5Test():
    return render_template("p5_withFlask.html")

app.run(debug = True)