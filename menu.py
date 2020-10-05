import PySimpleGUI as sg
import Juego 
import comoJugar 
import config 
import dificultad 
import top10 
import os
def so():
    try:
        if os.name != "nt" or os.name != "posix":
            WIDTH = 20
            HEIGHT = 3
            BUTTON_BORDER = 4
            return WIDTH, HEIGHT, BUTTON_BORDER
        elif os.name == "nt":
            WIDTH = 20
            HEIGHT = 3
            BUTTON_BORDER = 4
            return WIDTH, HEIGHT, BUTTON_BORDER
        elif os.name == "posix":
            WIDTH = 20
            HEIGHT = 2
            BUTTON_BORDER = 2
            return WIDTH, HEIGHT, BUTTON_BORDER
    except Exception:
        WIDTH = 20
        HEIGHT = 3
        BUTTON_BORDER = 4
        return WIDTH, HEIGHT, BUTTON_BORDER


def main():
    WIDTH, HEIGHT, BUTTON_BORDER = so()
    FUENTE = "arial"
    name = ["JUGAR","Configuración","Cómo Jugar","Top 10","SALIR"]
    keys = ["-comenzar-","-config-","-instrucc-","-top10-","-salir-"]

    botones = [
        [
            sg.B(
                x,
                button_color=("black", "green"),
                size=(WIDTH, HEIGHT),
                border_width=BUTTON_BORDER,
                focus=True,
                font=FUENTE,
                key=y
            )
            
        ]
        for x,y in zip(name,keys)
    ]

    

    layout = [
        [sg.T("ScrabbleAR", font=("Helvetica", 30), text_color="black", border_width=30)],
        [sg.Column(botones, justification="c")],
    ]

    window = sg.Window("ScrabbleAR", layout, size=(400, 500), element_justification="c")
    window.Finalize()
    window.FindElement("-salir-").Update(button_color=("black","#ff4d4d"))
    while True:
        event, _ = window.read()
        if event is None or event == "-salir-":
            break
        if event == "-comenzar-":
            dificultad.main()
        elif event == "-config-":
            config.Config()
        elif event == "-instrucc-":
            comoJugar.Reglas()
        elif event == "-top10-":
            top10.main()

    window.close()
