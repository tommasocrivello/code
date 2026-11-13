import flet as ft

class View:
    def __init__(self, page):
        self._page = page
        self._controller = None
        self._list_view = None
        self._dd = None

    def set_controller(self, controller):
        self._controller = controller

    def initialize_ui(self):
        self._page.window.width = 600
        self._page.window.height = 400
        #self._page.window.resizable = False

        # 📌 EVENTO - ⚠️ DA CAMBIARE ALL'ESAME: Associa on_click all'handler corretto
        btn = ft.Button(content="All trips",
                        on_click = self._controller.handler_btn)

        # 📌 EVENTO - ⚠️ DA CAMBIARE ALL'ESAME: Dropdown con on_select per intercettare subito il cambiamento
        self._dd = ft.Dropdown(label="Letter",
                               on_select=self._controller.handler_btn_sel)
                               
        # ⚠️ DA CAMBIARE ALL'ESAME: Opzioni del menu. Spesso andranno caricate dal database tramite Controller!
        self._dd.options.append(ft.DropdownOption(key="A", text="A"))
        self._dd.options.append(ft.DropdownOption(key="B", text="B"))
        self._dd.options.append(ft.DropdownOption(key="C", text="C"))

        btn_sel = ft.Button(content="Selected trips",
                        on_click = self._controller.handler_btn_sel)

        row = ft.Row([btn, self._dd, btn_sel],
                     alignment = ft.MainAxisAlignment.CENTER)
        
        self._page.controls.append(row)

        # 🚨 FONDAMENTALE: Usa expand=True sulla ListView in modo che faccia auto-scroll!
        self._list_view = ft.ListView(expand=True, spacing=10)
        #list_view.controls.append(ft.Text("Ciao"))
        self._page.controls.append(self._list_view)
        #self.update_ui()

    # 🚨 FONDAMENTALE: Questo metodo va chiamato dalla fine di ogni handler del Controller
    def update_ui(self):
        self._page.update()

    def show_alert_dialog(self, message):
        # 🚨 FONDAMENTALE: Alert standard di Flet (versione del prof). Copiaincolla ignorando i warning di PyCharm.
        dialog=ft.AlertDialog(
            title=ft.Text(message)
        )
        self._page.show_dialog(dialog)
