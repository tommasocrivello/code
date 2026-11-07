import flet as ft


def main(page : ft.Page):
    myText = ft.Text("Hello in red!", size = 34, color = "red")

    # Funzione invocata da Python/Flet quando noi premiamo quel pulsante
    def button_handler():
        print("L'utente ha premuto il pulsante!!!!")
        myText.color = "yellow"
        myText.update()

    myButton = ft.Button(content="Cambia colore :-)", on_click=button_handler)

    page.controls.append(myText)
    page.controls.append(myButton)

    page.update()




ft.run(main)



