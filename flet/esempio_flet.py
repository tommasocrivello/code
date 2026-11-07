import asyncio

import flet as ft

async def main(page : ft.Page):
    myText = ft.Text("Il mio testo", size = 48, color = "blue")

    page.controls.append(myText)

    for i in range (1, 100):
        myText.value = f"{i}"
        await asyncio.sleep(1)
        myText.update()

    page.update()

#main()
ft.run(main)
