import flet as ft

class Controller():
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def handler_btn(self, e):
        print("Button clicked")
        # 📌 1. Chiedi i dati al Model
        result = self._model.get_trips()
        
        # 🚨 FONDAMENTALE 2. Pulisci SEMPRE la ListView prima di aggiungerci roba, o la riempirai di cloni!
        self._view._list_view.controls.clear()
        
        # 📌 3. Mostra i risultati
        self._view._list_view.controls.append(ft.Text(f"{len(result)}"))
        for trip in result:
            self._view._list_view.controls.append(ft.Text(f"{trip}"))
            
        # 🚨 FONDAMENTALE 4. Aggiorna sempre la schermata alla fine!
        self._view.update_ui()

    def handler_btn_sel(self, e):
        print("Button selected trips clicked")
        
        # 📌 1. Leggi i valori inseriti dall'utente nella View
        letter = self._view._dd.value
        
        # 🚨 FONDAMENTALE 2. Controllo Errori: Impedisci all'app di crashare se l'utente non ha scelto nulla
        if letter is None:
            self._view.show_alert_dialog("You must select a letter first")
            return
            
        # 📌 3. Passa il parametro estratto al Model
        result = self._model.get_selected_trips(letter)
        
        # 🚨 FONDAMENTALE 4. Pulisci, Popola e Aggiorna!
        self._view._list_view.controls.clear()
        self._view._list_view.controls.append(ft.Text(f"{len(result)}"))
        for trip in result:
            self._view._list_view.controls.append(ft.Text(f"{trip}"))
            
        self._view.update_ui()
