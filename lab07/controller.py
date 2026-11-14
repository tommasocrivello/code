import flet as ft
from UI.view import View
from model.model import Model

"""
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
"""

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # ⚠️ DA CAMBIARE ALL'ESAME: Variabili per memorizzare le selezioni correnti (i filtri)
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown_biblioteche(self):
        """Popola il menu a tendina delle biblioteche."""
        # 🚨 FONDAMENTALE: Pulisci sempre le opzioni prima di riempirle
        self._view.dropdown_biblioteca.options.clear()
        self._view.dropdown_biblioteca.options.append(ft.dropdown.Option("Nessun Filtro"))

        # ⚠️ DA CAMBIARE ALL'ESAME: Chiama il metodo corretto del Model
        biblioteche = self._model.get_biblioteche()

        if biblioteche:
            for biblioteca in biblioteche:
                # ⚠️ DA CAMBIARE ALL'ESAME: Usa l'attributo giusto per l'etichetta testuale (es. biblioteca.nome)
                self._view.dropdown_biblioteca.options.append(ft.dropdown.Option(biblioteca.nome))
        else:
            self._view.show_alert("Errore nel caricamento delle biblioteche.")

        # 🚨 FONDAMENTALE: Aggiorna la schermata!
        self._view.update()

    def popola_dropdown_generi(self):
        """Popola il menu a tendina con TUTTI i generi disponibili nel DB."""
        self._view.dropdown_genere.options.clear()
        self._view.dropdown_genere.options.append(ft.dropdown.Option("Nessun Filtro"))

        generi = self._model.get_generi()

        if generi:
            for genere in generi:
                self._view.dropdown_genere.options.append(ft.dropdown.Option(genere))
        else:
            self._view.show_alert("Errore nel caricamento dei generi.")

        self._view.update()

    # CALLBACKS DROPDOWN
    def on_biblioteca_change(self, e):
        """Aggiorna la biblioteca selezionata e salva il valore."""
        valore = e.control.value
        # 🚨 FONDAMENTALE: Traduci la scelta vuota dell'UI in un `None` Python per il COALESCE in SQL
        self.biblioteca_selezionata = None if valore == "Nessun Filtro" else valore

    def on_genere_change(self, e):
        """Aggiorna il genere selezionato e salva il valore."""
        valore = e.control.value
        self.genere_selezionato = None if valore == "Nessun Filtro" else valore

    # AZIONE: MOSTRA RISULTATI
    def mostra_libri(self, e):
        """Mostra i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # 📌 Recupera lo stato salvato dalle tendine
        biblioteca = self.biblioteca_selezionata
        genere = self.genere_selezionato

        # 🚨 FONDAMENTALE: Svuota sempre la ListView prima di popolarla
        self._view.lista_libri.controls.clear()
        
        # ⚠️ DA CAMBIARE ALL'ESAME: Chiama il metodo del Model con i filtri giusti
        lista_libri = self._model.get_libri_filtrati(biblioteca, genere)

        if lista_libri is None:
            self._view.show_alert("Errore di connessione al database.")
        elif len(lista_libri) == 0:
            self._view.show_alert("Nessun libro trovato per i criteri selezionati")
        else:
            for libro in lista_libri:
                # ⚠️ DA CAMBIARE ALL'ESAME: Assicurati che il DTO abbia il def __str__ settato bene
                self._view.lista_libri.controls.append(ft.Text(f"{libro}"))

        # 🚨 FONDAMENTALE: Esegui sempre l'update alla fine dell'handler
        self._view.update()
