import flet as ft

from model.model import Model
from UI.view import View
from UI.controller import Controller

# 🚨 FONDAMENTALE: Struttura di bootstrap dell'app. Copia incollare identica.
def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    
    # 📌 Questa riga differisce dal vecchio template: l'UI si carica DOPO aver settato il controller!
    my_view.load_interface()

ft.run(main)
