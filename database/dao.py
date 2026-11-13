from database.db_connect import DB_Connect
# ⚠️ DA CAMBIARE ALL'ESAME: Importa il DTO corretto
from model.trip import Trip

class Dao:
    def __init__(self):
        pass

    def read_trips_from_db(self):
        db = DB_Connect()
        cnx = db.get_connection()
        if cnx is not None:
            print("Connection established")
            
            # 📌 QUERY - ⚠️ DA CAMBIARE ALL'ESAME: Inserisci la tua SQL
            query = "SELECT trip_id, bike_id, start_station_id, end_station_id, start_time, end_time, duration_seconds, user_type FROM trip"
            
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            
            for row in cursor:
                # 🚨 FONDAMENTALE: *row scompatta la tupla. L'ordine dei campi SQL deve coincidere col DTO!
                trip = Trip(*row)
                result.append(trip)
                
            # 🚨 FONDAMENTALE: Chiudi SEMPRE cursore e connessione, altrimenti l'app si blocca o intasi il DB
            cursor.close()
            cnx.close()
            return result

    def read_selected_trips_from_db(self, letter):
        db = DB_Connect()
        cnx = db.get_connection()
        if cnx is not None:
            print("Connection established")
            
            # 📌 QUERY CON PARAMETRI - ⚠️ DA CAMBIARE ALL'ESAME
            query = f"""SELECT t.*
                       FROM trip t, station s
                       WHERE t.start_station_id = s.station_id
                        AND s.name LIKE '{letter}%'
                    """
            
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            
            for row in cursor:
                # ⚠️ DA CAMBIARE ALL'ESAME: Usa la tua classe (es. Libro(*row))
                trip = Trip(*row)
                result.append(trip)
                
            # 🚨 FONDAMENTALE: Chiusura
            cursor.close()
            cnx.close()
            return result
