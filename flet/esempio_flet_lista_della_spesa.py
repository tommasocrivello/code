import flet as ft

def main(page : ft.Page):

    myTextField = ft.TextField("Aggiungi elemento:")

    myListView = ft.ListView()

    def aggiungi_handler():
        #page.controls.append(ft.Checkbox(f"{myTextField.value}"))
        myListView.controls.append(ft.Checkbox(f"{myTextField.value}"))
        page.update()

    myButtonAdd = ft.CupertinoButton(content="Aggiungi", on_click=aggiungi_handler)

    row1 = ft.Row([myTextField, myButtonAdd], alignment=ft.MainAxisAlignment.CENTER)

    #page.controls.append(myTextField)
    #page.controls.append(myButtonAdd)

    page.controls.append(row1)
    page.controls.append(myListView)

    page.update()



ft.run(main)