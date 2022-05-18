from flask import Flask
import sqlite3
from pathlib import Path
import requests

dir_path = str(Path(__file__).parent.resolve())

app = Flask(__name__)
app.config["DEBUG"] = True

"""
il server centrale serve per recuperare i dati dal client e mantenerli sul server
questo permette alle api di comunicare con esso senza bisogno di interagire direttamente
con il client, inoltre grazie alla variabile count permette di sapere quando vengono 
inseriti dei nuovi dati e quindi non ri inserire gli stessi dati di continuo

inoltre ho scelto di fare un file diverso per ogni api in modo che fosse più semplice 
un debug in caso di errori 
"""

old_count = 0

while True:

    # in caso il contatore risulti diverso vuol dire che ci sono state delle nuove misurazioni 
    # e quindi le vado a prelevare

    count = requests.get("http://127.0.0.1:5000/client/get_contatore")
    if old_count != count:
        gr = requests.get("http://127.0.0.1:5000/client/get_grandezza")
        st = requests.get("http://127.0.0.1:5000/client/get_stazione")
        val = requests.get("http://127.0.0.1:5000/client/get_valore")
        dt = requests.get("http://127.0.0.1:5000/client/get_datetime")
    old_count = count

@app.route("/server/get_contatore", methods=["GET"])
def get_grandeza():
    return count

@app.route("/server/get_grandezza", methods=["GET"])
def get_grandeza():
    return gr

@app.route("/server/get_stazione", methods=["GET"])
def get_stazione():
    return st

@app.route("/server/get_valore", methods=["GET"])
def get_valore():
    return val

@app.route("/server/get_datetime", methods=["GET"])
def get_datetime():
    return dt