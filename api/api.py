from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pymysql
import pandas as pd
from flask import Flask, redirect

sqlEngine = create_engine('mysql+pymysql://root:UZ64pXUFbQ38v5@database-1.cruoyzidkoee.us-east-1.rds.amazonaws.com:3306/wines', pool_recycle=3600)
if not database_exists(sqlEngine.url):
    create_database(sqlEngine.url)

app = Flask(__name__)

@app.route('/')
def hello_world():
    dbConnection    = sqlEngine.connect()
    return 'Hello World'

@app.route('/localhost')
def change_to_local():
    sqlEngine = create_engine('mysql+pymysql://root:root@localhost:3306/IA', pool_recycle=3600)
    if not database_exists(sqlEngine.url):
        create_database(sqlEngine.url)
    return redirect('/')
   
if __name__ == '__main__':
   app.run(debug=True)
#    
# 
# if not database_exists(sqlEngine.url):
    # create_database(sqlEngine.url)
# 
# dbConnection    = sqlEngine.connect()
# 
# nombre de la tabla
# tableName   = "winequality_red"