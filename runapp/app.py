import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

import os
# Flask
from flask import Flask, request, render_template

# SQL Alchemy
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# PyMySQL
import pymysql

# Pandas
import pandas as pd

# Import your config
#from config import remote_db_endpoint, remote_db_port, remote_gwsis_dbname, remote_gwsis_dbuser, remote_gwsis_dbpwd
remote_db_endpoint = os.environ.get('remote_db_endpoint')
remote_db_port = os.environ.get('remote_db_port')
remote_gwsis_dbname = os.environ.get('remote_gwsis_dbname')
remote_gwsis_dbuser = os.environ.get('remote_gwsis_dbuser')
remote_gwsis_dbpwd = os.environ.get('remote_gwsis_dbpwd')


# Configure MySQL connection and connect 
pymysql.install_as_MySQLdb()
engine = create_engine(f"mysql://{remote_gwsis_dbuser}:{remote_gwsis_dbpwd}@{remote_db_endpoint}:{remote_db_port}/{remote_gwsis_dbname}")

# Set up SQL Alchemy connection and classes
Base = automap_base() # Declare a Base using `automap_base()`
Base.prepare(engine, reflect=True) # Use the Base class to reflect the database tables
sqlkey = Base.classes.datadownloadAWS
#begin session
session = Session(engine)
    
#query dataset
results = session.query(sqlkey.FIPS, sqlkey.State, sqlkey.County, 
                        sqlkey.PCT_OBESE_ADULTS08, sqlkey.CHILDPOVRATE15, 
                        sqlkey.FOODINSEC_13_15, sqlkey.MEDHHINC15, 
                        sqlkey.PC_FSRSALES07, sqlkey.PC_SNAPBEN10, 
                        sqlkey.PCT_DIABETES_ADULTS08, sqlkey.PCT_FREE_LUNCH09, 
                        sqlkey.PCT_LACCESS_BLACK15, sqlkey.PCT_NHBLACK10, 
                        sqlkey.PCT_NSLP09, sqlkey.POVRATE15).all()
df = pd.DataFrame(results, columns=['FIPS', 'State', 'County', 'PCT_OBESE_ADULTS08', 
                                    'CHILDPOVRATE15', 'FOODINSEC_13_15', 'MEDHHINC15', 
                                    'PC_FSRSALES07', 'PC_SNAPBEN10', 
                                    'PCT_DIABETES_ADULTS08', 'PCT_FREE_LUNCH09', 
                                    'PCT_LACCESS_BLACK15', 'PCT_NHBLACK10', 
                                    'PCT_NSLP09', 'POVRATE15'])
def floater(columnname, list_df):
    for i in df[columnname].values.tolist():
        list_df.append(float(i))
#create list of column names
columnnames = ['PCT_OBESE_ADULTS08', 'CHILDPOVRATE15', 'FOODINSEC_13_15', 'MEDHHINC15', 'PC_FSRSALES07', 'PC_SNAPBEN10', 'PCT_DIABETES_ADULTS08', 'PCT_FREE_LUNCH09', 'PCT_LACCESS_BLACK15', 'PCT_NHBLACK10', 'PCT_NSLP09', 'POVRATE15']
#initialize y_value list
list_PCT_OBESE_ADULTS08 = []
#initialize x_value lists
list_CHILDPOVRATE15 = []
list_FOODINSEC_13_15 = []
list_MEDHHINC15 = []
list_PC_FSRSALES07 = []
list_PC_SNAPBEN10 = []
list_PCT_DIABETES_ADULTS08 = []
list_PCT_FREE_LUNCH09 = []
list_PCT_LACCESS_BLACK15 = []
list_PCT_NHBLACK10 = []
list_PCT_NSLP09 = []
list_POVRATE15 = []
lists = [list_PCT_OBESE_ADULTS08, list_CHILDPOVRATE15, list_FOODINSEC_13_15, list_MEDHHINC15, list_PC_FSRSALES07, list_PC_SNAPBEN10, list_PCT_DIABETES_ADULTS08, list_PCT_FREE_LUNCH09, list_PCT_LACCESS_BLACK15, list_PCT_NHBLACK10, list_PCT_NSLP09, list_POVRATE15]
counter = 0
for i in columnnames:
    floater(i, lists[counter])
    counter = counter + 1


# Initialize Flask application
app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/route1")
def route1():
    # Format the data for Plotly
    trace = {
        "x": lists[1],
        "y": list_PCT_OBESE_ADULTS08,
        "mode": 'markers',
        "type": "scatter"
    }
    return jsonify(trace)
@app.route("/route2")
def route2():
    # Format the data for Plotly
    trace = {
        "x": lists[2],
        "y": list_PCT_OBESE_ADULTS08,
        "mode": 'markers',
        "type": "scatter"
    }
    return jsonify(trace)

@app.route("/route3")
def route3():
    # Format the data for Plotly
    trace = {
        "x": lists[3],
        "y": list_PCT_OBESE_ADULTS08,
        "mode": 'markers',
        "type": "scatter"
    }
    return jsonify(trace)
@app.route("/route4")
def route4():
    # Format the data for Plotly
    trace = {
        "x": lists[4],
        "y": list_PCT_OBESE_ADULTS08,
        "mode": 'markers',
        "type": "scatter"
    }
    return jsonify(trace)

@app.route("/route5")
def route5():
    # Format the data for Plotly
    trace = {
        "x": lists[5],
        "y": list_PCT_OBESE_ADULTS08,
        "mode": 'markers',
        "type": "scatter"
    }
    return jsonify(trace)

@app.route("/route6")
def route6():
    # Format the data for Plotly
    trace = {
        "x": lists[6],
        "y": list_PCT_OBESE_ADULTS08,
        "mode": 'markers',
        "type": "scatter"
    }
    return jsonify(trace)

@app.route("/route7")
def route7():
    # Format the data for Plotly
    trace = {
        "x": lists[7],
        "y": list_PCT_OBESE_ADULTS08,
        "mode": 'markers',
        "type": "scatter"
    }
    return jsonify(trace)

@app.route("/route8")
def route8():
    # Format the data for Plotly
    trace = {
        "x": lists[8],
        "y": list_PCT_OBESE_ADULTS08,
        "mode": 'markers',
        "type": "scatter"
    }
    return jsonify(trace)

@app.route("/route9")
def route9():
    # Format the data for Plotly
    trace = {
        "x": lists[9],
        "y": list_PCT_OBESE_ADULTS08,
        "mode": 'markers',
        "type": "scatter"
    }
    return jsonify(trace)

@app.route("/route10")
def route10():
    # Format the data for Plotly
    trace = {
        "x": lists[10],
        "y": list_PCT_OBESE_ADULTS08,
        "mode": 'markers',
        "type": "scatter"
    }
    return jsonify(trace)

@app.route("/route11")
def route11():
    # Format the data for Plotly
    trace = {
        "x": lists[11],
        "y": list_PCT_OBESE_ADULTS08,
        "mode": 'markers',
        "type": "scatter"
    }
    return jsonify(trace)

if __name__ == "__main__":
    app.run(debug=True)    