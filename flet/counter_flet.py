import flet as ft

def main(page : ft.Page):
    page.window.width = 420
    page.window.height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Funzioni cui è delegata la gestione delle interazioni con i controlli della GUI

    def handler_minus(e):
        #print("-")
        v = int(myText.value)
        v = v-1
        myText.value = v
        myText.update()

    def handler_plus(e):
        #print("+")
        v = int(myText.value)
        v = v+1
        myText.value = v
        myText.update()

    # Definizione dei controlli della GUI

    myBtnMinus = ft.IconButton(icon = ft.Icons.REMOVE,
                               icon_size = 50,
                               on_click = handler_minus)
    myBtnPlus = ft.IconButton(icon = ft.Icons.ADD,
                              icon_size = 50,
                              on_click = handler_plus)

    myText = ft.TextField(value = 0,
                          disabled = True,
                          width = 130,
                          text_size = 50,
                          text_align = ft.TextAlign.CENTER
                          )

    # Riga per organizzare i contenuti, allinearli, ...
    myRow = ft.Row([myBtnMinus, myText, myBtnPlus],
                   alignment = ft.MainAxisAlignment.CENTER)

    # Riga aggiunta alla lista di controlli della pagina
    page.controls.append(myRow)

    """
    # Controlli aggiunti uno per volta alla pagina
    page.controls.append(myBtnMinus)
    page.controls.append(myText)
    page.controls.append(myBtnPlus)
    """

    # Aggiornamento della pagina, non necessario per versioni più
    # recenti di flet, ma mantenuto in questi esempio per compatibilità
    page.update()


# Avvio dell'applicazione

ft.run(main)