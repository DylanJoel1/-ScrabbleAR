import PySimpleGUI as sg
from config import guardar
from os import path
import json
import sys

sys.path.insert(1, "/guardado")


archivo_config = path.join(path.dirname(__file__), r"guardado/top10.json")
default_config = path.join(path.dirname(__file__), r"guardado/top10vacio.json")


def up(window,datos):
    """ Actualiza el tablero de posiciones del top 10 """
    for x in range(10):
                window.FindElement("nombre"+str(x)).Update(value=list(datos.keys())[x])
                window.FindElement("puntos"+str(x)).Update(value=datos[list(datos.keys())[x]])


def cargar(window, a, ad):
    try:
        with open(a, "r") as jsonFile:
            datos = json.load(jsonFile)
            up(window,datos)
    except Exception:
        with open(ad, "r") as jsonFile:
            datos = json.load(jsonFile)
            up(window,datos)


def cargar_default(window, a, ad):
    with open(ad, "r") as jsonFile:
        datos = json.load(jsonFile)
        up(window,datos)
    with open(a, "w") as jsonFile:
        json.dump(datos, jsonFile)


def main():
    primera = 1

    columna2 = [
        [
            sg.T((str(x+1)), size=(8, 1), justification="center", pad=(0, 0)),
            sg.T("Vacio", size=(14, 1), justification="center", pad=(0, 0), key=("nombre"+str(x))),
            sg.T("0", size=(8, 1), justification="center", pad=(0, 0), key=("puntos"+str(x)))
        ]
        for x in range(10)
    ]

    layout = [
        [sg.T("Top 10", font=("Helvetica", 30), text_color="black", border_width=30)],
        [
            sg.B("Pos.", button_color=("black", "grey"), size=(8, 1), pad=(0, 0)),
            sg.B("Nombre", button_color=("black", "grey"), size=(14, 1), pad=(0, 0)),
            sg.B("Puntos", button_color=("black", "grey"), size=(8, 1), pad=(0, 0)),
        ],
        [sg.Column(columna2, justification="c")],
        [
            sg.B(
                "Restaurar a por defecto",
                size=(20, 2),
                key="-default-",
                button_color=("black", "#FA8072"),
            ),
            sg.B(
                "Volver",
                size=(8, 2),
                key="-volver-",
                button_color=("black", "#FA8072"),
            ),
        ],
    ]


    window = sg.Window("Top 10", layout, size=(400, 500), element_justification="c")

    while True:
        if primera == 1:
            window.Finalize()
            cargar(window, archivo_config, default_config)
            primera = 0
        event, values = window.read()
        if event is None or event == "-volver-":
            break
        if event == "-default-":
            cargar_default(window, archivo_config, default_config)
            sg.popup("Configuracion por defecto cargada con exito")

    window.close()
