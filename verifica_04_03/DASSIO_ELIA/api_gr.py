from flask import Flask
import sqlite3
from pathlib import Path
import requests

dir_path = str(Path(__file__).parent.resolve())

app = Flask(__name__)
app.config["DEBUG"] = True

"""
questa è una semplice api che converte il nome della grandezza nell'id 
di essa permettendo all'api compilatrice di compilare la tabella del db 
correttamente
"""

@app.route("/api/grandezza_id", methods=["GET"])
def grandezza_id():
    
    gr = requests.get("http://127.0.0.1:5000/server/get_grandezza")


    con = sqlite3.connect('meteo_db.db')
    cur = con.cursor()

    id = cur.execute(f'SELECT id_misura FROM grandezze WHERE grandezza_misura = {gr}')

    con.close()

    return id
