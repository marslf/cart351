from flask import Flask

app = Flask(__name__) # a python key term (anything with framed with _x_)


#HOMEPAGE
@app.route("/") # @ = decorator = app.route knows that since it is directly on top of def index it means that it is directly connected with it (+ adds a bunch of stuff on it)
def index(): # view function
    return '<h1> Hello CART 351!</h1>'

#PATHWAYS
@app.route("/about") #define the pathways (you can make up your own)
def about():
    return '<h1 style = "color:purple"> About Cart 351!</h1>' # now if you go to the website and add /about at the end you will open this new page

#DYNAMIC ROUTING
@app.route("/user/<name>") #variable used in string
def user_profile(name):
    # we will use templates sooN!
    return f"<h2> This is <span style = 'color:orange'>{name}'s</span> profile page"

#DEBUG MODE 
@app.route("/another/<dynamicVar>")
def another_route(dynamicVar):
    # we will use templates sooN!
    return f"<h2> the 100th letter of {dynamicVar} is {dynamicVar[99]}</h2>"
#if you dont insert smt w/ 100 digits/letters = Internal Server Error 
#add debug=True inside of app.run(HERE) = enter debig mode to find out what is going wrong
#dont forget to turn off debig when youre done developping

#-------------------------------

#ROUTING EXERCISE : CAT LATIN
@app.route("/catlatin/<catname>")
def cat_latin(catname):
    #A: if it does not end in y = add y
    if not catname.endswith("y"):
        newcatname = catname + "y"
    #B: if it ends in y = replace y with iful
    else:
        newcatname = catname[:-1] + "iful"
    
    return f"<h2>{catname} in Cat-Latin is: <span style='color:green'>{newcatname}</span></h2>"


app.run()
#app.run(debug=True)