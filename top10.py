import PySimpleGUI as sg
from config import guardar
from os import path
import json
import sys

sys.path.insert(1, "/guardado")


archivo_config = path.join(path.dirname(__file__), r"guardado/top10.json")
default_config = path.join(path.dirname(__file__), r"guardado/top10vacio.json")


def cargar(window, a, ad):
    try:
        with open(a, "r") as jsonFile:
            datos = json.load(jsonFile)
            window.FindElement("nombre0").Update(value=list(datos.keys())[0])
            window.FindElement("nombre1").Update(value=list(datos.keys())[1])
            window.FindElement("nombre2").Update(value=list(datos.keys())[2])
            window.FindElement("nombre3").Update(value=list(datos.keys())[3])
            window.FindElement("nombre4").Update(value=list(datos.keys())[4])
            window.FindElement("nombre5").Update(value=list(datos.keys())[5])
            window.FindElement("nombre6").Update(value=list(datos.keys())[6])
            window.FindElement("nombre7").Update(value=list(datos.keys())[7])
            window.FindElement("nombre8").Update(value=list(datos.keys())[8])
            window.FindElement("nombre9").Update(value=list(datos.keys())[9])
            window.FindElement("puntos0").Update(value=datos[list(datos.keys())[0]])
            window.FindElement("puntos1").Update(value=datos[list(datos.keys())[1]])
            window.FindElement("puntos2").Update(value=datos[list(datos.keys())[2]])
            window.FindElement("puntos3").Update(value=datos[list(datos.keys())[3]])
            window.FindElement("puntos4").Update(value=datos[list(datos.keys())[4]])
            window.FindElement("puntos5").Update(value=datos[list(datos.keys())[5]])
            window.FindElement("puntos6").Update(value=datos[list(datos.keys())[6]])
            window.FindElement("puntos7").Update(value=datos[list(datos.keys())[7]])
            window.FindElement("puntos8").Update(value=datos[list(datos.keys())[8]])
            window.FindElement("puntos9").Update(value=datos[list(datos.keys())[9]])
    except Exception:
        with open(ad, "r") as jsonFile:
            datos = json.load(jsonFile)
            window.FindElement("nombre0").Update(value=list(datos.keys())[0])
            window.FindElement("nombre1").Update(value=list(datos.keys())[1])
            window.FindElement("nombre2").Update(value=list(datos.keys())[2])
            window.FindElement("nombre3").Update(value=list(datos.keys())[3])
            window.FindElement("nombre4").Update(value=list(datos.keys())[4])
            window.FindElement("nombre5").Update(value=list(datos.keys())[5])
            window.FindElement("nombre6").Update(value=list(datos.keys())[6])
            window.FindElement("nombre7").Update(value=list(datos.keys())[7])
            window.FindElement("nombre8").Update(value=list(datos.keys())[8])
            window.FindElement("nombre9").Update(value=list(datos.keys())[9])
            window.FindElement("puntos0").Update(value=datos[list(datos.keys())[0]])
            window.FindElement("puntos1").Update(value=datos[list(datos.keys())[1]])
            window.FindElement("puntos2").Update(value=datos[list(datos.keys())[2]])
            window.FindElement("puntos3").Update(value=datos[list(datos.keys())[3]])
            window.FindElement("puntos4").Update(value=datos[list(datos.keys())[4]])
            window.FindElement("puntos5").Update(value=datos[list(datos.keys())[5]])
            window.FindElement("puntos6").Update(value=datos[list(datos.keys())[6]])
            window.FindElement("puntos7").Update(value=datos[list(datos.keys())[7]])
            window.FindElement("puntos8").Update(value=datos[list(datos.keys())[8]])
            window.FindElement("puntos9").Update(value=datos[list(datos.keys())[9]])


def cargar_default(window, a, ad):
    with open(ad, "r") as jsonFile:
        datos = json.load(jsonFile)
        window.FindElement("nombre0").Update(value=list(datos.keys())[0])
        window.FindElement("nombre1").Update(value=list(datos.keys())[1])
        window.FindElement("nombre2").Update(value=list(datos.keys())[2])
        window.FindElement("nombre3").Update(value=list(datos.keys())[3])
        window.FindElement("nombre4").Update(value=list(datos.keys())[4])
        window.FindElement("nombre5").Update(value=list(datos.keys())[5])
        window.FindElement("nombre6").Update(value=list(datos.keys())[6])
        window.FindElement("nombre7").Update(value=list(datos.keys())[7])
        window.FindElement("nombre8").Update(value=list(datos.keys())[8])
        window.FindElement("nombre9").Update(value=list(datos.keys())[9])
        window.FindElement("puntos0").Update(value=datos[list(datos.keys())[0]])
        window.FindElement("puntos1").Update(value=datos[list(datos.keys())[1]])
        window.FindElement("puntos2").Update(value=datos[list(datos.keys())[2]])
        window.FindElement("puntos3").Update(value=datos[list(datos.keys())[3]])
        window.FindElement("puntos4").Update(value=datos[list(datos.keys())[4]])
        window.FindElement("puntos5").Update(value=datos[list(datos.keys())[5]])
        window.FindElement("puntos6").Update(value=datos[list(datos.keys())[6]])
        window.FindElement("puntos7").Update(value=datos[list(datos.keys())[7]])
        window.FindElement("puntos8").Update(value=datos[list(datos.keys())[8]])
        window.FindElement("puntos9").Update(value=datos[list(datos.keys())[9]])
    with open(a, "w") as jsonFile:
        json.dump(datos, jsonFile)


def main():
    primera = 1
    layout = [
        [sg.T("Top 10", font=("Helvetica", 30), text_color="black", border_width=30)],
        [
            sg.B("Pos.", button_color=("black", "grey"), size=(8, 1), pad=(0, 0)),
            sg.B("Nombre", button_color=("black", "grey"), size=(14, 1), pad=(0, 0)),
            sg.B("Puntos", button_color=("black", "grey"), size=(8, 1), pad=(0, 0)),
        ],
        [
            sg.T("1", size=(8, 1), justification="center", pad=(0, 0)),
            sg.T(
                "Vacio", size=(14, 1), justification="center", pad=(0, 0), key="nombre0"
            ),
            sg.T("0", size=(8, 1), justification="center", pad=(0, 0), key="puntos0"),
        ],
        [
            sg.T("2", size=(8, 1), justification="center", pad=(0, 0)),
            sg.T(
                "Vacio", size=(14, 1), justification="center", pad=(0, 0), key="nombre1"
            ),
            sg.T("0", size=(8, 1), justification="center", pad=(0, 0), key="puntos1"),
        ],
        [
            sg.T("3", size=(8, 1), justification="center", pad=(0, 0)),
            sg.T(
                "Vacio", size=(14, 1), justification="center", pad=(0, 0), key="nombre2"
            ),
            sg.T("0", size=(8, 1), justification="center", pad=(0, 0), key="puntos2"),
        ],
        [
            sg.T("4", size=(8, 1), justification="center", pad=(0, 0)),
            sg.T(
                "Vacio", size=(14, 1), justification="center", pad=(0, 0), key="nombre3"
            ),
            sg.T("0", size=(8, 1), justification="center", pad=(0, 0), key="puntos3"),
        ],
        [
            sg.T("5", size=(8, 1), justification="center", pad=(0, 0)),
            sg.T(
                "Vacio", size=(14, 1), justification="center", pad=(0, 0), key="nombre4"
            ),
            sg.T("0", size=(8, 1), justification="center", pad=(0, 0), key="puntos4"),
        ],
        [
            sg.T("6", size=(8, 1), justification="center", pad=(0, 0)),
            sg.T(
                "Vacio", size=(14, 1), justification="center", pad=(0, 0), key="nombre5"
            ),
            sg.T("0", size=(8, 1), justification="center", pad=(0, 0), key="puntos5"),
        ],
        [
            sg.T("7", size=(8, 1), justification="center", pad=(0, 0)),
            sg.T(
                "Vacio", size=(14, 1), justification="center", pad=(0, 0), key="nombre6"
            ),
            sg.T("0", size=(8, 1), justification="center", pad=(0, 0), key="puntos6"),
        ],
        [
            sg.T("8", size=(8, 1), justification="center", pad=(0, 0)),
            sg.T(
                "Vacio", size=(14, 1), justification="center", pad=(0, 0), key="nombre7"
            ),
            sg.T("0", size=(8, 1), justification="center", pad=(0, 0), key="puntos7"),
        ],
        [
            sg.T("9", size=(8, 1), justification="center", pad=(0, 0)),
            sg.T(
                "Vacio", size=(14, 1), justification="center", pad=(0, 0), key="nombre8"
            ),
            sg.T("0", size=(8, 1), justification="center", pad=(0, 0), key="puntos8"),
        ],
        [
            sg.T("10", size=(8, 1), justification="center", pad=(0, 0)),
            sg.T(
                "Vacio",
                size=(14, 1),
                justification="center",
                pad=(0, 0),
                key="nombre9",
            ),
            sg.T("0", size=(8, 1), justification="center", pad=(0, 0), key="puntos9"),
        ],
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
