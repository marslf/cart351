from dotenv import load_dotenv
from flask import Flask,render_template,request
# use flask_pymongo instead of  normal pymongo (simplifies integration)
from flask_pymongo import PyMongo
import os
load_dotenv()  # Load variables from .env and .flaskenv
db_user = os.getenv('MONGODB_USER')
db_pass = os.getenv('DATABASE_PASSWORD')

app = Flask(__name__)
# set a config var
uri = f"mongodb+srv://{db_user}:{db_pass}@cluster0.kljrtj4.mongodb.net/?appName=Cluster0"
app.config["MONGO_URI"] = uri
mongo = PyMongo(app)
try:
    #get details of the client
    print (mongo.cx)
    print("You successfully connected to MongoDB!")
except Exception as e:
    print(e)