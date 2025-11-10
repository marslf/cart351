from dotenv import load_dotenv
from flask import Flask,render_template,request, redirect, url_for,session
# use flask_pymongo instead of  normal pymongo (simplifies integration)
from flask_pymongo import PyMongo
import os
load_dotenv()  # Load variables from .env and .flaskenv
db_user = os.getenv('MONGODB_USER')
db_pass = os.getenv('DATABASE_PASSWORD')
db_name = os.getenv('DATABASE_NAME')

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'
# set a config var
#uri = f"mongodb+srv://{db_user}:{db_pass}@cluster0.kljrtj4.mongodb.net/?appName=Cluster0"
uri = f"mongodb+srv://{db_user}:{db_pass}@cluster0.kljrtj4.mongodb.net/{db_name}?retryWrites=true&w=majority"
app.config["MONGO_URI"] = uri
mongo = PyMongo(app)
# try:
#     #get details of the client
#     print (mongo.cx)
#     print("You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# try:
#     # #get details of the client
#     # print (mongo.cx)
#     # #get db
#     # print (mongo.db)
#     # #get collection
#     # print (mongo.db.plantRepo)
#     # #print (mongo.db.user): another option to get access to info
#     # print("You successfully connected to MongoDB!")
#     result = mongo.db.plantRepo.insert_one({"testKeyMon":"testValueMon"})
#     print(result)
# except Exception as e:
#     print(e)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/insertTestPage')
def insertTest():
    session.pop('ids', default=None)
    return render_template("testInsert.html")

# a route
@app.route('/insertMany')
def insertMany():
    data = [{'owner_name': 'Sarah',
'plant_name' : 'Snake Plant',
'birthDate':'2002-06-12',
'geoLoc': 'Montreal',
'descript': 'Description for the plant',
'imagePath': 'images/one.png'
},
{
'owner_name': 'Sarah',
'plant_name' :'Cactus',
'birthDate' :'2005-06-13',
'geoLoc':'Toronto',
'descript':'Description for the plant',
'imagePath': 'images/seven.png'
},
 
 {
'owner_name': 'Sarah',
'plant_name' : 'Agapanthus',
'birthDate': '2003-03-19',
'geoLoc': 'Halifax',
'descript': 'Description for the plant',
'imagePath': 'images/seventeen.png'
},
 {
'owner_name': 'Stephen',
'plant_name' : 'Baby Rubber Plant',
'birthDate ': '1999-07-18',
'geoLoc': 'Edinborough',
'descript':'Description for the plant',
'imagePath': 'images/ten.png'
},
 
{
'owner_name': 'Stephen',
'plant_name' : 'Dahlia',
'birthDate' :'2000-05-06',
'geoLoc':'London',
'descript':'Description for the plant',
'imagePath': 'images/thirteen.png'
},
 
{
'owner_name' : 'Harold',
'plant_name' : 'Daphne',
'birthDate': '2012-10-21',
'geoLoc':'New York',
'descript':'Description for the plant',
'imagePath': 'images/three.png'
},
{
'owner_name' : 'Martha',
'plant_name' : 'Daylily',
'birthDate' :'2017-08-21',
'geoLoc':'Paris',
'descript':'Description for the plant',
'imagePath': 'images/nine.png'
}]
    try:
        # insert many works :)
        result = mongo.db.plantRepo.insert_many(data)
        session['ids'] = result.inserted_ids
        return redirect(url_for('testIds'))
    except Exception as e:
        print(e)

@app.route('/testIds')
def testIds():
    print(session['ids'])
    return render_template("testIds.html")

# a route
# retrieve one result (w/ zero criteria)
# @app.route('/viewResults')
# def viewResults():
#     result = mongo.db.plantRepo.find_one({})
#     print(result)
#     return render_template("viewResults.html",result=result)

# retrive all results
@app.route('/viewResults')
def viewResults():
    result = mongo.db.plantRepo.find()
    print(result)
    return render_template("viewResults.html",result=result)

app.run(debug = True)