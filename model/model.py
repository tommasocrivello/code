from database.dao import Dao

class Model:
    def __init__(self):
        pass

    def get_trips(self):
        print("Getting trips ...")
        dao = Dao()
        # ⚠️ DA CAMBIARE ALL'ESAME: Chiama il metodo del DAO giusto senza parametri
        return dao.read_trips_from_db()

    def get_selected_trips(self, letter):
        print("Getting selected trips ...")
        dao = Dao()
        # ⚠️ DA CAMBIARE ALL'ESAME: Chiama il metodo del DAO passando i parametri della View
        return dao.read_selected_trips_from_db(letter)
