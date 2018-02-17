import datetime
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///DB-ESP8266.db')
app = Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,application/json')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

class Temp(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from esptemp") # This line performs que$
        result = [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
    	try:
            idtemp = request.json['id']
            tempvalue = request.json['tempvalue']
            tempdate = request.json['tempdate']
            tempdate = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            textInsert = "insert into esptemp(tempvalue, tempdate) VALUES(?,?)"
            query = conn.execute(textInsert, (tempvalue, tempdate))
            print "OK JSON POST esptemp"
            return True
        except:
            print "Bad JSON POST esptemp"
            return None

class TempID(Resource):
    def get(self, idtemp):
        conn = db_connect.connect() # connect to database
        try:
            query = conn.execute("select * from esptemp where id =%d "  %int(idtemp))
            for i in query.cursor: result=dict(zip(tuple (query.keys()) ,i))
            print "OK GET FROM esptemp"
            return jsonify(result)
        except:
            print "NOT FOUND FROM esptemp"
            return None


api.add_resource(Temp, '/temp') # Direccion de pagos
api.add_resource(TempID, '/temp/<idtemp>') # Direccion de pagos

if __name__ == '__main__':
     app.run(host='0.0.0.0')

