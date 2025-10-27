#library
from flask import Flask,render_template,request,session,redirect,url_for
import os
app = Flask(__name__)

# Details on the Secret Key: https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing
#       the session data.
app.secret_key = 'BAD_SECRET_KEY'

@app.route("/")
def index():
    return render_template("index.html",
                           user={"username":"sabine"},
                           passedDictionary={
                                            "fav_color":"fuscia", 
                                             "fav_veg":"cauliflower",
                                             "fav_fruit":"kiwi",
                                             "fav_animal":"toucan"
                                             },
                            imgPath = "../static/images/pineapple_2.jpg"
                                        
                           ) 

@app.route("/inputPlant")
def addPlantData():
    return render_template("addPlantData.html") 

#version 2
@app.route("/thank_you")
def thank_you():
     app.logger.info(request.args)
  
     if('a_name' in request.args):
         owner_name = request.args["a_name"] 
         app.logger.info(owner_name)
          #url is not clean
         #return render_template("thankyou.html",owner_name = request.args["a_name"]) 
        
         # issue we lose the parameters! - but url is clean :)
         return redirect(url_for("thank_you")) 
     #part of the reloading process... we redirect - then headers rewritten and reload the template
     else:
         return render_template("thankyou.html") 
    
#@app.route("/thank_you")
#def thank_you():
#    app.logger.info(request.args)
#    owner_name = request.args["a_name"] 
#    app.logger.info(owner_name)
#         #url is not clean
#    return render_template("thankyou.html",owner_name = owner_name) 



@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#add session route
@app.route('/inputSessionData')
def inputSessionData():
    return render_template("inputSessionData.html")

@app.route('/saveSession')
def saveSession():
    app.logger.info(request.args['data_a'])
    #reload  - use url_for() here :) - the function...
    #but note that the data will be gone
    # so add in a session variable
    session['data_a'] = request.args['data_a']
    session['data_b'] = request.args['data_b']
    return redirect(url_for('inputSessionData'))

#modify session route
@app.route('/modifySessionData')
def modifySessionData():
    return render_template("modifySessionData.html")

@app.route('/modifySession')
def modifySession():
    app.logger.info(request.args['data_a'])
 
    #reload  - use url_for here :) - the function...
    #but note that the data will be gone
    # so add in a session variable
    session['data_a'] = request.args['data_a']
    session['data_b'] = request.args['data_b']
    return redirect(url_for('modifySessionData'))
#everytime you click submit = reloads the page = the data gets updated everywhere!

#delete Session 
@app.route('/deleteSession')
def deleteSession():
    # Clear the session data stored in the session object
    session.pop('data_a', default=None)
    session.pop('data_b', default=None)
    return redirect(url_for('modifySessionData'))

# aroute == fetch
@app.route('/getForm')
def getFetchForm():
    return render_template("form_fetch_get.html")

# for the get
@app.route('/getDataFromForm')
def getDataFromForm():
    app.logger.info(request.args)
    return ({"data_received":"success","owner":request.args['o_name']})

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/postRegFormFetch",methods = ['POST'])
def postRegFormFetch():
    app.logger.info(request.form)
    return ({"data_received":"success","f_name":request.form["f_name"]})



app.run(debug=True)