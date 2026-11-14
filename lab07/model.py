from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

"""
    MODELLO:
    - Fa da passacarte / Facciata
    - Il Controller non deve mai parlare col DAO direttamente
"""

class Model:
    def __init__(self):
        # ⚠️ DA CAMBIARE ALL'ESAME: Inizializza i tuoi DAO
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # ⚠️ DA CAMBIARE ALL'ESAME: Esponi i metodi per il Controller passando i parametri
    def get_libri_filtrati(self, biblioteca: str, genere: str):
        """Restituisce la lista filtrata delegando al DAO."""
        return self._libro_dao.get_libri_filtrati(biblioteca, genere)

    def get_generi(self):
        return self._libro_dao.get_generi()

    def get_biblioteche(self):
        return self._biblioteca_dao.get_biblioteche()
