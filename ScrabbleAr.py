import PySimpleGUI as sg
import Juego
import comoJugar
import config
import dificultad
import top10
import os


def so():
    try:
        if os.name == "nt":
            WIDTH = 20
            HEIGHT = 3
            BUTTON_BORDER = 4
            return WIDTH, HEIGHT, BUTTON_BORDER
        elif os.name == "posix":
            WIDTH = 20
            HEIGHT = 1
            BUTTON_BORDER = 2
            return WIDTH, HEIGHT, BUTTON_BORDER
    except Exception:
        WIDTH = 20
        HEIGHT = 3
        BUTTON_BORDER = 4
        return WIDTH, HEIGHT, BUTTON_BORDER


WIDTH, HEIGHT, BUTTON_BORDER = so()
FUENTE = "arial"

botones = [
    [
        sg.B(
            "JUGAR",
            button_color=("black", "green"),
            size=(WIDTH, HEIGHT),
            border_width=BUTTON_BORDER,
            focus=True,
            font=FUENTE,
            key="-comenzar-",
        )
    ],
    [
        sg.B(
            "Configuraciones",
            button_color=("black", "green"),
            size=(WIDTH, HEIGHT),
            border_width=BUTTON_BORDER,
            font=FUENTE,
            key="-config-",
        )
    ],
    [
        sg.B(
            "Cómo jugar",
            button_color=("black", "green"),
            size=(WIDTH, HEIGHT),
            border_width=BUTTON_BORDER,
            font=FUENTE,
            key="-instrucc-",
        )
    ],
    [
        sg.B(
            "Top 10",
            button_color=("black", "green"),
            size=(WIDTH, HEIGHT),
            border_width=BUTTON_BORDER,
            font=FUENTE,
            key="-top10-",
        )
    ],
    [
        sg.B(
            "SALIR",
            button_color=("black", "#ff4d4d"),
            size=(WIDTH, HEIGHT),
            border_width=BUTTON_BORDER,
            font=FUENTE,
            key="-salir-",
        )
    ],
]

layout = [
    [sg.T("ScrabbleAR", font=("Helvetica", 30), text_color="black", border_width=30)],
    [sg.Column(botones, justification="c")],
]

window = sg.Window("ScrabbleAR", layout, size=(400, 500), element_justification="c")

while True:
    event, values = window.read()
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
