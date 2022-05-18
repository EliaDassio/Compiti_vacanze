from flask import Flask
import requests
from datetime import datetime

count = 0

while True:
    gr = input('Inserire in nome della grandezza misurata: ')
    st = input('\nInserire il nome della stazione che ha eseguito la misurazione: ')
    val = int(input('\nInserire il valore della grandeza misurata: '))
    dt = input('\nInserire la data e l\'ora della misurazione: ')

    count += count

    gr = gr.lower()
    st = st.lower()
    dt = datetime. strptime(dt, '%d/%m/%y %H:%M:%S')

@app.route("/client/get_contatore", methods=["GET"])
def get_grandeza():
    return count

@app.route("/client/get_grandezza", methods=["GET"])
def get_grandeza():
    return gr

@app.route("/client/get_stazione", methods=["GET"])
def get_stazione():
    return st

@app.route("/client/get_valore", methods=["GET"])
def get_valore():
    return val

@app.route("/client/get_datetime", methods=["GET"])
def get_datetime():
    return dt