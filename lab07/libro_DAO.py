from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    DAO Avanzato per Filtri Dinamici (Join + Coalesce)
"""

class LibroDAO:
    def __init__(self):
        pass

    @staticmethod
    def get_libri_filtrati(biblioteca: str, genere: str) -> list[Libro] | None:
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        # 🚨 FONDAMENTALE: Ritorna i risultati come dizionari
        cursor = cnx.cursor(dictionary=True)
        
        # 📌 QUERY COALESCE - ⚠️ DA CAMBIARE ALL'ESAME
        # 🚨 FONDAMENTALE: Usa COALESCE(%s, nome_colonna) per rendere il filtro OPZIONALE (ignora se passo None)
        query = """
                    SELECT l.*
                    FROM libro l, biblioteca b
                    WHERE b.nome = COALESCE(%s, b.nome) 
                      AND l.genere = COALESCE(%s, l.genere) 
                      AND l.id_biblioteca = b.id
                """
        try:
            # 🚨 FONDAMENTALE: Passa sempre le variabili come TUPLA alla execute, mai con f-strings
            cursor.execute(query, (biblioteca, genere,))
            for row in cursor:
                # ⚠️ DA CAMBIARE ALL'ESAME: Costruzione DTO
                libro = Libro(
                    id=row["id"],
                    titolo=row["titolo"],
                    autore=row["autore"],
                    genere=row["genere"],
                    anno_pubblicazione=row["anno_pubblicazione"],
                    id_biblioteca=row["id_biblioteca"],
                )
                result.append(libro)
        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
            
        # 🚨 FONDAMENTALE
        finally:
            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def get_generi() -> list[str] | None:
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)
        
        # ⚠️ DA CAMBIARE ALL'ESAME: Estrarre valori univoci per tendine dropdown
        query = """
                    SELECT DISTINCT genere
                    FROM libro
                """
        try:
            cursor.execute(query)
            for row in cursor:
                result.append(row["genere"])

        except Exception as e:
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result
