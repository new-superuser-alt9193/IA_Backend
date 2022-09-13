from flask import Flask, redirect, jsonify
import mysql.connector as sql
import random
from waitress import serve
from predictions import makePrediction

db_connect = sql.connect(host='database-1.c7ext510fslq.us-east-1.rds.amazonaws.com', user='admin', password ='s13sMachineLearning')
cursor = db_connect.cursor()
cursor.execute("USE IA;")

app = Flask(__name__)

def getCustomers():
    cursor.execute("select customer_ID from customer_data limit 10")
    resultado = cursor.fetchall()
    return [row[0] for row in resultado]

def getColumnsNames():
    query = "SHOW COLUMNS from customer_data;"
    cursor.execute(query)
    resultado = cursor.fetchall()
    resultado = resultado[3:]
    columnas = []
    for i in resultado:
        columnas.append(i[0])
    return columnas

def getDataCustomer(id):
    query = "select * from customer_data WHERE customer_ID = '" + id + "'"
    cursor.execute(query)
    resultado = cursor.fetchall()
    resultado = resultado[0]
    resultado = resultado[3:]
    return resultado

def getTargetCustomer(id):
    query = "select target from customer_data WHERE customer_ID = '" + id + "'"
    cursor.execute(query)
    resultado = cursor.fetchall()
    resultado = resultado[0][0]
    return resultado

@app.route('/')
def hello_world():
    return jsonify(hello = "Wolrd")

@app.route('/customers')
def customers():
    return jsonify({"customers": getCustomers()})

@app.route('/random_customer')
def randomCustomer():
    return jsonify({"randomCustomer": random.choice(getCustomers())})

@app.route('/id/<id>', methods = ['POST', 'GET'])
def id(id):
    return jsonify({"columns": getColumnsNames(),"data": getDataCustomer(id), "target": getTargetCustomer(id), "target_calculated": makePrediction([getDataCustomer(id)])})

# @app.route('/localhost')
# def change_to_local():
#     db_connect = sql.connect(host='localhost', user='root', password ='root')
#     return redirect('/')

if __name__ == '__main__':
    # app.run(debug=True)
    serve(app, host='0.0.0.0', port=8080)
