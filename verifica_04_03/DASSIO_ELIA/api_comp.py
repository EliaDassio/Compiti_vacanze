import sqlite3
from pathlib import Path
import requests

dir_path = str(Path(__file__).parent.resolve())

"""
questa api serve per caricara i dati sul db richiedendo i dati sia al server
centrale sia alle altre 2 api specifiche in modo da inserire i dati corretti
inoltre come il server centrale tiene conto di quando vengono inseriti dei 
nuovi dati in modo da non ri inserire gli stessi dadi nel db
"""

old_count = 0

while True:
    count = requests.get("http://127.0.0.1:5000//server/get_contatore")
    if old_count != count:
        
        # recupero i dati sia dalle api, sia dal server centrale

        id_gt = requests.get("http://127.0.0.1:5000/api/grandezza_id")
        id_st = requests.get("http://127.0.0.1:5000/api/stazione_id")
        val = requests.get("http://127.0.0.1:5000//server/get_valore")
        dt = requests.get("http://127.0.0.1:5000//server/get_datetime")
        
        con = sqlite3.connect('meteo_db.db')
        cur = con.cursor()

        # dopo aver aperto la connessione con il db vado ad inserire in ordine corretto i valori recuperati per poi chiudere la
        # connessione e fare l'update del contatore

        cur.execute(f'INSERT INTO misurazioni (id_stazione, id_grandezza, data_ora, valore) VALUES ({id_st}, {id_gt}, {dt}, {val})')
        con.commit()

        con.close()

    
    old_count = count