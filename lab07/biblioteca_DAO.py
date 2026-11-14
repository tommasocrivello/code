from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    DAO Base per Select Semplice (Senza filtri)
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    @staticmethod
    def get_biblioteche() -> list[Biblioteca] | None:
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        # 🚨 FONDAMENTALE: dictionary=True ti salva la vita se l'ordine colonne cambia!
        cursor = cnx.cursor(dictionary=True)
        
        # ⚠️ DA CAMBIARE ALL'ESAME: La query
        query = """ SELECT * FROM biblioteca """

        try:
            cursor.execute(query)
            for row in cursor:
                # ⚠️ DA CAMBIARE ALL'ESAME: Costruisci il DTO estraendo i campi per nome col dizionario
                biblioteca = Biblioteca(
                    id=row["id"],
                    nome=row["nome"],
                    indirizzo=row["indirizzo"]
                )
                result.append(biblioteca)
        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
            
        # 🚨 FONDAMENTALE: Chiudi SEMPRE in un blocco finally per evitare memory leak del DB
        finally:
            cursor.close()
            cnx.close()

        return result
