from dataclasses import dataclass

# ⚠️ DA CAMBIARE ALL'ESAME: Nome della classe (es. Libro, Stazione, Partita, ecc.)
@dataclass
class Trip:
    # ⚠️ DA CAMBIARE ALL'ESAME: Elenca qui ESATTAMENTE i campi nell'ordine in cui li estrai con la SELECT
    trip_id : int
    bike_id : int
    start_station_id : int
    end_station_id : int
    start_time : str
    end_time : str
    duration_seconds : int
    user_type : str

    def __str__(self):
        # 🚨 FONDAMENTALE: Questo è come verrà stampato visivamente l'oggetto nella ListView di Flet!
        return f"Trip {self.trip_id}"
