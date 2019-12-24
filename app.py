import os
from flask import Flask,render_template, redirect, request, url_for, request, jsonify
from bson.json_util import dumps
app = Flask(__name__)

from flask_pymongo import PyMongo
app.config["MONGO_URI"]=os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = 'leMans'

mongo = PyMongo(app)

@app.route('/')

def inst():
    return render_template("winners.html")


                           
@app.route('/api/v1/resources/winners/all', methods=['GET'])
def api_all():
    winners=dumps(mongo.db.winners.find())
    
    return jsonify(winners)

@app.route('/api/v1/resources/winners', methods=['GET'])
def api_filter():
    query_parameters = request.args
    search_var={}
    year = query_parameters.get('year')
    team = query_parameters.get('team')
    car = query_parameters.get('car')
    drivers=query_parameters.get('driver')
    
    if year:
       search_var.update( {'year' : year} )
    if team:
       search_var.update( {'team' : team} )
    if car:
       search_var.update( {'car' : car} )
    if drivers:
       
       search_var.update( {'drivers' : drivers} )

    winners=dumps(mongo.db.winners.find(search_var))
    

    return jsonify(winners)
if __name__=='__main__':
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)