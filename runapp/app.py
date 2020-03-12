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
from config import remote_db_endpoint, remote_db_port, remote_gwsis_dbname, remote_gwsis_dbuser, remote_gwsis_dbpwd
#remote_db_endpoint = os.environ.get('remote_db_endpoint')
#remote_db_port = os.environ.get('remote_db_port')
#remote_gwsis_dbname = os.environ.get('remote_gwsis_dbname')
#remote_gwsis_dbuser = os.environ.get('remote_gwsis_dbuser')
#remote_gwsis_dbpwd = os.environ.get('remote_gwsis_dbpwd')


# Configure MySQL connection and connect 
pymysql.install_as_MySQLdb()
engine = create_engine(f"mysql://{remote_gwsis_dbuser}:{remote_gwsis_dbpwd}@{remote_db_endpoint}:{remote_db_port}/{remote_gwsis_dbname}")

# Set up SQL Alchemy connection and classes
Base = automap_base() # Declare a Base using `automap_base()`
Base.prepare(engine, reflect=True) # Use the Base class to reflect the database tables
sqlkey = Base.classes.datadownloadAWS

# Initialize Flask application
app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/runquery")
def runquery():
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
    df_json = df.to_json(orient='records')
    return df_json
if __name__ == "__main__":
    app.run(debug=True)    