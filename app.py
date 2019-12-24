import os
from flask import Flask,render_template, redirect, request, url_for, request
app = Flask(__name__)

from flask_pymongo import PyMongo
app.config["MONGO_URI"]=os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = 'leMans'

mongo = PyMongo(app)

@app.route('/')
@app.route('/winners')
def get_tasks():
    return render_template("winners.html", 
                           winners=mongo.db.winners.find())
    
if __name__=='__main__':
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)