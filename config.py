import PySimpleGUI as sg
import json
from os import path
import sys

sys.path.insert(1, "/guardado")

archivo_config = path.join(path.dirname(__file__), r"guardado/datos.json")
default_config = path.join(path.dirname(__file__), r"guardado/datos_default.json")


def val_hora(values, nhora, window):
    try:
        if values[nhora][-1] not in ("0123456789"):
            window.FindElement(nhora).Update(values[nhora][:-1])
    except IndexError:
        pass
    if len(values[nhora][:-1]) >= 1:
        window.FindElement(nhora).Update(values[nhora][:-1])
    try:
        if len(values[nhora]) > 1 and int(values[nhora]) > 9:
            window.FindElement(nhora).Update(9)
    except ValueError:
        window.FindElement(nhora).Update(0)


def val_min(values, nmin, window):
    try:
        if values[nmin][-1] not in ("0123456789"):
            window.FindElement(nmin).Update(values[nmin][:-1])
    except IndexError:
        pass
    if len(values[nmin][:-1]) >= 2:
        window.FindElement(nmin).Update(values[nmin][:-1])
    try:
        if len(values[nmin]) > 1 and int(values[nmin]) > 59:
            window.FindElement(nmin).Update(59)
    except ValueError:
        window.FindElement(nmin).Update(1)


def val_pc(values, pc, window):
    try:
        if values[pc][-1] not in ("0123456789"):
            window.FindElement(pc).Update(values[pc][:-1])
    except IndexError:
        pass
    if len(values[pc][:-1]) >= 2:
        window.FindElement(pc).Update(values[pc][:-1])
    try:
        if len(values[pc]) > 1 and int(values[pc]) > 99:
            window.FindElement(pc).Update(99)
    except ValueError:
        window.FindElement(pc).Update(0)
    try:
        if len(values[pc]) >= 1 and int(values[pc]) < 1:
            window.FindElement(pc).Update(1)
    except ValueError:
        window.FindElement(pc).Update(1)


def guardar(a, datos):
    """ Funcion que guarda los datos en el archivo a """
    with open(a, "w") as jsonFile:
        json.dump(datos, jsonFile)
    sg.popup("Se guardo correctamente")


def cargar(window, keys, a, ad):
    try:
        with open(a, "r") as jsonFile:
            datos = json.load(jsonFile)
        for key in keys:
            try:
                window.FindElement(key).Update(value=datos[key])
            except Exception:
                print(f"Problema actualizando la ventana. Key = {key}")
    except FileNotFoundError:
        sg.popup(
            "No se encontró el archivo de configuracion, se procedera a crear uno..."
        )
        with open(ad, "r") as jsonFile:
            datos = json.load(jsonFile)
        guardar(a, datos)
        for key in keys:
            try:
                window.FindElement(key).Update(value=datos[key])
            except Exception:
                print(f"Problema actualizando la ventana. Key = {key}")


def cargar_default(window, keys, ad):
    with open(ad, "r") as jsonFile:
        datos = json.load(jsonFile)
        for key in keys:
            try:
                window.FindElement(key).Update(value=datos[key])
            except Exception:
                print(f"Problema actualizando la ventana. Key = {key}")


def Config():

    FUENTE = "arial"
    primera = 1
    keys = {
        "dpuntosa": "",
        "dpuntosb": "",
        "dpuntosc": "",
        "dpuntosd": "",
        "dpuntose": "",
        "dpuntosf": "",
        "dpuntosg": "",
        "dpuntosh": "",
        "dpuntosi": "",
        "dpuntosj": "",
        "dpuntosk": "",
        "dpuntosl": "",
        "dpuntosll": "",
        "dpuntosm": "",
        "dpuntosn": "",
        "dpuntos\u00f1": "",
        "dpuntoso": "",
        "dpuntosp": "",
        "dpuntosq": "",
        "dpuntosr": "",
        "dpuntoss": "",
        "dpuntost": "",
        "dpuntosu": "",
        "dpuntosv": "",
        "dpuntosw": "",
        "dpuntosx": "",
        "dpuntosy": "",
        "dpuntosz": "",
        "dpuntosrr": "",
        "dcantidada": "",
        "dcantidadb": "",
        "dcantidadc": "",
        "dcantidadd": "",
        "dcantidade": "",
        "dcantidadf": "",
        "dcantidadg": "",
        "dcantidadh": "",
        "dcantidadi": "",
        "dcantidadj": "",
        "dcantidadk": "",
        "dcantidadl": "",
        "dcantidadll": "",
        "dcantidadm": "",
        "dcantidadn": "",
        "dcantidad\u00f1": "",
        "dcantidado": "",
        "dcantidadp": "",
        "dcantidadq": "",
        "dcantidadr": "",
        "dcantidads": "",
        "dcantidadt": "",
        "dcantidadu": "",
        "dcantidadv": "",
        "dcantidadw": "",
        "dcantidadx": "",
        "dcantidady": "",
        "dcantidadz": "",
        "dcantidadrr": "",
        "fpuntosa": "",
        "fpuntosb": "",
        "fpuntosc": "",
        "fpuntosd": "",
        "fpuntose": "",
        "fpuntosf": "",
        "fpuntosg": "",
        "fpuntosh": "",
        "fpuntosi": "",
        "fpuntosj": "",
        "fpuntosk": "",
        "fpuntosl": "",
        "fpuntosll": "",
        "fpuntosm": "",
        "fpuntosn": "",
        "fpuntos\u00f1": "",
        "fpuntoso": "",
        "fpuntosp": "",
        "fpuntosq": "",
        "fpuntosr": "",
        "fpuntoss": "",
        "fpuntost": "",
        "fpuntosu": "",
        "fpuntosv": "",
        "fpuntosw": "",
        "fpuntosx": "",
        "fpuntosy": "",
        "fpuntosz": "",
        "fpuntosrr": "",
        "fcantidada": "",
        "fcantidadb": "",
        "fcantidadc": "",
        "fcantidadd": "",
        "fcantidade": "",
        "fcantidadf": "",
        "fcantidadg": "",
        "fcantidadh": "",
        "fcantidadi": "",
        "fcantidadj": "",
        "fcantidadk": "",
        "fcantidadl": "",
        "fcantidadll": "",
        "fcantidadm": "",
        "fcantidadn": "",
        "fcantidad\u00f1": "",
        "fcantidado": "",
        "fcantidadp": "",
        "fcantidadq": "",
        "fcantidadr": "",
        "fcantidads": "",
        "fcantidadt": "",
        "fcantidadu": "",
        "fcantidadv": "",
        "fcantidadw": "",
        "fcantidadx": "",
        "fcantidady": "",
        "fcantidadz": "",
        "fcantidadrr": "",
        "mpuntosa": "",
        "mpuntosb": "",
        "mpuntosc": "",
        "mpuntosd": "",
        "mpuntose": "",
        "mpuntosf": "",
        "mpuntosg": "",
        "mpuntosh": "",
        "mpuntosi": "",
        "mpuntosj": "",
        "mpuntosk": "",
        "mpuntosl": "",
        "mpuntosll": "",
        "mpuntosm": "",
        "mpuntosn": "",
        "mpuntos\u00f1": "",
        "mpuntoso": "",
        "mpuntosp": "",
        "mpuntosq": "",
        "mpuntosr": "",
        "mpuntoss": "",
        "mpuntost": "",
        "mpuntosu": "",
        "mpuntosv": "",
        "mpuntosw": "",
        "mpuntosx": "",
        "mpuntosy": "",
        "mpuntosz": "",
        "mpuntosrr": "",
        "mcantidada": "",
        "mcantidadb": "",
        "mcantidadc": "",
        "mcantidadd": "",
        "mcantidade": "",
        "mcantidadf": "",
        "mcantidadg": "",
        "mcantidadh": "",
        "mcantidadi": "",
        "mcantidadj": "",
        "mcantidadk": "",
        "mcantidadl": "",
        "mcantidadll": "",
        "mcantidadm": "",
        "mcantidadn": "",
        "mcantidad\u00f1": "",
        "mcantidado": "",
        "mcantidadp": "",
        "mcantidadq": "",
        "mcantidadr": "",
        "mcantidads": "",
        "mcantidadt": "",
        "mcantidadu": "",
        "mcantidadv": "",
        "mcantidadw": "",
        "mcantidadx": "",
        "mcantidady": "",
        "mcantidadz": "",
        "mcantidadrr": "",
        "fhora": "",
        "fmin": "",
        "mhora": "",
        "mmin": "",
        "dhora": "",
        "dmin": "",
    }

    columnahf = [
        [
            sg.T("Duración de la partida:", justification="left", size=(17, 1)),
            sg.Input(size=(2, 1), key="fhora", enable_events=True, default_text="0"),
            sg.T("horas", justification="left", size=(4, 1)),
            sg.Input(size=(2, 1), key="fmin", enable_events=True, default_text="30"),
            sg.T("minutos", justification="left", size=(6, 1)),
        ],
        [
            sg.T("Tipos de palabras permitidas:", justification="left", size=(21, 1)),
            sg.T("Sustantivos:", justification="left", size=(9, 1)),
            sg.CB("", key="fsustantivos", default=True, disabled=True),
            sg.T("Adjetivos:", justification="left", size=(7, 1)),
            sg.CB("", key="fadjetivos", default=True, disabled=True),
            sg.T("Verbos:", justification="left", size=(6, 1)),
            sg.CB("", key="fverbos", default=True, disabled=True),
        ],
    ]

    columnahm = [
        [
            sg.T("Duración de la partida:", justification="left", size=(17, 1)),
            sg.Input(size=(2, 1), key="mhora", enable_events=True, default_text="0"),
            sg.T("horas", justification="left", size=(4, 1)),
            sg.Input(size=(2, 1), key="mmin", enable_events=True, default_text="30"),
            sg.T("minutos", justification="left", size=(6, 1)),
        ],
        [
            sg.T("Tipos de palabras permitidas:", justification="left", size=(21, 1)),
            sg.T("Sustantivos:", justification="left", size=(9, 1)),
            sg.CB("", key="msustantivos", default=True, disabled=True),
            sg.T("Adjetivos:", justification="left", size=(7, 1)),
            sg.CB("", key="madjetivos", default=True, disabled=True),
            sg.T("Verbos:", justification="left", size=(6, 1)),
            sg.CB("", key="mverbos", default=True, disabled=True),
        ],
    ]

    columnahd = [
        [
            sg.T("Duración de la partida:", justification="left", size=(17, 1)),
            sg.Input(size=(2, 1), key="dhora", enable_events=True, default_text="0"),
            sg.T("horas", justification="left", size=(4, 1)),
            sg.Input(size=(2, 1), key="dmin", enable_events=True, default_text="30"),
            sg.T("minutos", justification="left", size=(6, 1)),
        ],
        [
            sg.T("Tipos de palabras permitidas:", justification="left", size=(21, 1)),
            sg.T("Sustantivos:", justification="left", size=(9, 1)),
            sg.CB("", key="dsustantivos", default=True, disabled=True),
            sg.T("Adjetivos:", justification="left", size=(7, 1)),
            sg.CB("", key="dadjetivos", default=True, disabled=True),
            sg.T("Verbos:", justification="left", size=(6, 1)),
            sg.CB("", key="dverbos", default=True, disabled=True),
        ],
    ]

    columnaf1 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("A", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosa", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidada", enable_events=True),
        ],
        [
            sg.T("B", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosb", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadb", enable_events=True),
        ],
        [
            sg.T("C", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosc", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadc", enable_events=True),
        ],
        [
            sg.T("D", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosd", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadd", enable_events=True),
        ],
        [
            sg.T("E", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntose", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidade", enable_events=True),
        ],
        [
            sg.T("F", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosf", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadf", enable_events=True),
        ],
        [
            sg.T("G", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosg", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadg", enable_events=True),
        ],
        [
            sg.T("H", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosh", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadh", enable_events=True),
        ],
        [
            sg.T("I", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosi", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadi", enable_events=True),
        ],
        [
            sg.T("J", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosj", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadj", enable_events=True),
        ],
    ]

    columnaf2 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("K", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosk", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadk", enable_events=True),
        ],
        [
            sg.T("L", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosl", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadl", enable_events=True),
        ],
        [
            sg.T("LL", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosll", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadll", enable_events=True),
        ],
        [
            sg.T("M", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosm", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadm", enable_events=True),
        ],
        [
            sg.T("N", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosn", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadn", enable_events=True),
        ],
        [
            sg.T("Ñ", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosñ", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadñ", enable_events=True),
        ],
        [
            sg.T("O", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntoso", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidado", enable_events=True),
        ],
        [
            sg.T("P", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosp", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadp", enable_events=True),
        ],
        [
            sg.T("Q", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosq", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadq", enable_events=True),
        ],
        [
            sg.T("R", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosr", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadr", enable_events=True),
        ],
    ]

    columnaf3 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("RR", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosrr", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadrr", enable_events=True),
        ],
        [
            sg.T("S", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntoss", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidads", enable_events=True),
        ],
        [
            sg.T("T", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntost", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadt", enable_events=True),
        ],
        [
            sg.T("U", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosu", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadu", enable_events=True),
        ],
        [
            sg.T("V", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosv", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadv", enable_events=True),
        ],
        [
            sg.T("W", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosw", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadw", enable_events=True),
        ],
        [
            sg.T("X", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosx", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadx", enable_events=True),
        ],
        [
            sg.T("Y", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosy", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidady", enable_events=True),
        ],
        [
            sg.T("Z", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="fpuntosz", enable_events=True),
            sg.Input(size=(2, 1), key="fcantidadz", enable_events=True),
        ],
    ]

    columnam1 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("A", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosa", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidada", enable_events=True),
        ],
        [
            sg.T("B", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosb", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadb", enable_events=True),
        ],
        [
            sg.T("C", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosc", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadc", enable_events=True),
        ],
        [
            sg.T("D", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosd", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadd", enable_events=True),
        ],
        [
            sg.T("E", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntose", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidade", enable_events=True),
        ],
        [
            sg.T("F", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosf", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadf", enable_events=True),
        ],
        [
            sg.T("G", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosg", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadg", enable_events=True),
        ],
        [
            sg.T("H", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosh", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadh", enable_events=True),
        ],
        [
            sg.T("I", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosi", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadi", enable_events=True),
        ],
        [
            sg.T("J", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosj", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadj", enable_events=True),
        ],
    ]

    columnam2 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("K", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosk", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadk", enable_events=True),
        ],
        [
            sg.T("L", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosl", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadl", enable_events=True),
        ],
        [
            sg.T("LL", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosll", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadll", enable_events=True),
        ],
        [
            sg.T("M", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosm", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadm", enable_events=True),
        ],
        [
            sg.T("N", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosn", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadn", enable_events=True),
        ],
        [
            sg.T("Ñ", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosñ", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadñ", enable_events=True),
        ],
        [
            sg.T("O", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntoso", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidado", enable_events=True),
        ],
        [
            sg.T("P", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosp", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadp", enable_events=True),
        ],
        [
            sg.T("Q", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosq", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadq", enable_events=True),
        ],
        [
            sg.T("R", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosr", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadr", enable_events=True),
        ],
    ]

    columnam3 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("RR", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosrr", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadrr", enable_events=True),
        ],
        [
            sg.T("S", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntoss", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidads", enable_events=True),
        ],
        [
            sg.T("T", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntost", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadt", enable_events=True),
        ],
        [
            sg.T("U", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosu", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadu", enable_events=True),
        ],
        [
            sg.T("V", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosv", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadv", enable_events=True),
        ],
        [
            sg.T("W", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosw", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadw", enable_events=True),
        ],
        [
            sg.T("X", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosx", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadx", enable_events=True),
        ],
        [
            sg.T("Y", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosy", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidady", enable_events=True),
        ],
        [
            sg.T("Z", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="mpuntosz", enable_events=True),
            sg.Input(size=(2, 1), key="mcantidadz", enable_events=True),
        ],
    ]

    columnad1 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("A", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosa", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidada", enable_events=True),
        ],
        [
            sg.T("B", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosb", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadb", enable_events=True),
        ],
        [
            sg.T("C", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosc", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadc", enable_events=True),
        ],
        [
            sg.T("D", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosd", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadd", enable_events=True),
        ],
        [
            sg.T("E", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntose", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidade", enable_events=True),
        ],
        [
            sg.T("F", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosf", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadf", enable_events=True),
        ],
        [
            sg.T("G", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosg", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadg", enable_events=True),
        ],
        [
            sg.T("H", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosh", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadh", enable_events=True),
        ],
        [
            sg.T("I", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosi", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadi", enable_events=True),
        ],
        [
            sg.T("J", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosj", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadj", enable_events=True),
        ],
    ]

    columnad2 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("K", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosk", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadk", enable_events=True),
        ],
        [
            sg.T("L", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosl", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadl", enable_events=True),
        ],
        [
            sg.T("LL", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosll", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadll", enable_events=True),
        ],
        [
            sg.T("M", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosm", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadm", enable_events=True),
        ],
        [
            sg.T("N", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosn", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadn", enable_events=True),
        ],
        [
            sg.T("Ñ", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosñ", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadñ", enable_events=True),
        ],
        [
            sg.T("O", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntoso", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidado", enable_events=True),
        ],
        [
            sg.T("P", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosp", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadp", enable_events=True),
        ],
        [
            sg.T("Q", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosq", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadq", enable_events=True),
        ],
        [
            sg.T("R", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosr", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadr", enable_events=True),
        ],
    ]

    columnad3 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("RR", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosrr", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadrr", enable_events=True),
        ],
        [
            sg.T("S", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntoss", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidads", enable_events=True),
        ],
        [
            sg.T("T", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntost", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadt", enable_events=True),
        ],
        [
            sg.T("U", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosu", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadu", enable_events=True),
        ],
        [
            sg.T("V", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosv", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadv", enable_events=True),
        ],
        [
            sg.T("W", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosw", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadw", enable_events=True),
        ],
        [
            sg.T("X", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosx", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadx", enable_events=True),
        ],
        [
            sg.T("Y", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosy", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidady", enable_events=True),
        ],
        [
            sg.T("Z", justification="left", size=(2, 1)),
            sg.Input(size=(2, 1), key="dpuntosz", enable_events=True),
            sg.Input(size=(2, 1), key="dcantidadz", enable_events=True),
        ],
    ]

    facil_layout = [
        [
            sg.T(
                "Fácil",
                justification="center",
                font=(FUENTE, 20),
                size=(54, 1),
                background_color="#00FFFF",
                text_color="#000080",
            )
        ],
        [
            sg.T(
                "A continuación podrá configurar la partida para la dificultad"
                " seleccionada. La minima duración de partida es de 1 minuto.",
                justification="center",
                size=(110, 1),
            )
        ],
        [
            sg.T(
                "P y C significan Puntos y Cantidad respectivamente. No se pueden"
                " cambiar los tipos de palabras permitidas.",
                justification="center",
                size=(110, 1),
            )
        ],
        [
            sg.Column(columnaf1),
            sg.Column(columnaf2),
            sg.Column(columnaf3),
            sg.Column(columnahf),
        ],
    ]

    medio_layout = [
        [
            sg.T(
                "Medio",
                justification="center",
                font=(FUENTE, 20),
                size=(54, 1),
                background_color="#00FFFF",
                text_color="#000080",
            )
        ],
        [
            sg.T(
                "A continuación podrá configurar la partida para la dificultad"
                " seleccionada. La minima duración de partida es de 1 minuto.",
                justification="center",
                size=(110, 1),
            )
        ],
        [
            sg.T(
                "P y C significan Puntos y Cantidad respectivamente. No se pueden"
                " cambiar los tipos de palabras permitidas.",
                justification="center",
                size=(110, 1),
            )
        ],
        [
            sg.Column(columnam1),
            sg.Column(columnam2),
            sg.Column(columnam3),
            sg.Column(columnahm),
        ],
    ]

    dificil_layout = [
        [
            sg.T(
                "Difícil",
                justification="center",
                font=(FUENTE, 20),
                size=(54, 1),
                background_color="#00FFFF",
                text_color="#000080",
            )
        ],
        [
            sg.T(
                "A continuación podrá configurar la partida para la dificultad"
                " seleccionada. La minima duración de partida es de 1 minuto.",
                justification="center",
                size=(110, 1),
            )
        ],
        [
            sg.T(
                "P y C significan Puntos y Cantidad respectivamente. No se pueden"
                " cambiar los tipos de palabras permitidas.",
                justification="center",
                size=(110, 1),
            )
        ],
        [
            sg.Column(columnad1),
            sg.Column(columnad2),
            sg.Column(columnad3),
            sg.Column(columnahd),
        ],
    ]

    layout_Config = [
        [
            sg.T(
                "Configuración",
                justification="center",
                font=(FUENTE, 20),
                size=(55, 1),
                background_color="#00FFFF",
                text_color="#000080",
            )
        ],
        [
            sg.TabGroup(
                [
                    [
                        sg.Tab("Facil", facil_layout),
                        sg.Tab("Medio", medio_layout),
                        sg.Tab("Dificil", dificil_layout),
                    ]
                ]
            )
        ],
        [
            sg.B(
                "Guardar",
                size=(8, 2),
                key="-guardar-",
                button_color=("black", "#FA8072"),
            ),
            sg.B(
                "Restaurar a por defecto",
                size=(20, 2),
                key="-default-",
                button_color=("black", "#FA8072"),
            ),
            sg.B(
                "Volver", size=(8, 2), key="-volver-", button_color=("black", "#FA8072")
            ),
        ],
    ]

    window = sg.Window("Configuracion", layout_Config)

    while True:
        if primera == 1:
            window.Finalize()
            cargar(window, keys, archivo_config, default_config)
            primera = 0
        event, values = window.read()
        if event is None or event == "-volver-":
            break
        if event == "fhora":
            print("event fhora")
            val_hora(values, event, window)
        if event == "fmin":
            print("event fmin")
            val_min(values, event, window)
        if (
            event == "fpuntosa"
            or event == "fpuntosb"
            or event == "fpuntosc"
            or event == "fpuntosd"
            or event == "fpuntose"
            or event == "fpuntosf"
            or event == "fpuntosg"
            or event == "fpuntosh"
            or event == "fpuntosi"
            or event == "fpuntosj"
            or event == "fpuntosk"
            or event == "fpuntosl"
            or event == "fpuntosll"
            or event == "fpuntosm"
            or event == "fpuntosn"
            or event == "fpuntosñ"
            or event == "fpuntoso"
            or event == "fpuntosp"
            or event == "fpuntosq"
            or event == "fpuntosr"
            or event == "fpuntosrr"
            or event == "fpuntoss"
            or event == "fpuntost"
            or event == "fpuntosu"
            or event == "fpuntosv"
            or event == "fpuntosw"
            or event == "fpuntosx"
            or event == "fpuntosy"
            or event == "fpuntosz"
            or event == "mpuntosa"
            or event == "mpuntosb"
            or event == "mpuntosc"
            or event == "mpuntosd"
            or event == "mpuntose"
            or event == "mpuntosf"
            or event == "mpuntosg"
            or event == "mpuntosh"
            or event == "mpuntosi"
            or event == "mpuntosj"
            or event == "mpuntosk"
            or event == "mpuntosl"
            or event == "mpuntosll"
            or event == "mpuntosm"
            or event == "mpuntosn"
            or event == "mpuntosñ"
            or event == "mpuntoso"
            or event == "mpuntosp"
            or event == "mpuntosq"
            or event == "mpuntosr"
            or event == "mpuntosrr"
            or event == "mpuntoss"
            or event == "mpuntost"
            or event == "mpuntosu"
            or event == "mpuntosv"
            or event == "mpuntosw"
            or event == "mpuntosx"
            or event == "mpuntosy"
            or event == "mpuntosz"
            or event == "dpuntosa"
            or event == "dpuntosb"
            or event == "dpuntosc"
            or event == "dpuntosd"
            or event == "dpuntose"
            or event == "dpuntosf"
            or event == "dpuntosg"
            or event == "dpuntosh"
            or event == "dpuntosi"
            or event == "dpuntosj"
            or event == "dpuntosk"
            or event == "dpuntosl"
            or event == "dpuntosll"
            or event == "dpuntosm"
            or event == "dpuntosn"
            or event == "dpuntosñ"
            or event == "dpuntoso"
            or event == "dpuntosp"
            or event == "dpuntosq"
            or event == "dpuntosr"
            or event == "dpuntosrr"
            or event == "dpuntoss"
            or event == "dpuntost"
            or event == "dpuntosu"
            or event == "dpuntosv"
            or event == "dpuntosw"
            or event == "dpuntosx"
            or event == "dpuntosy"
            or event == "dpuntosz"
            or event == "fcantidada"
            or event == "fcantidadb"
            or event == "fcantidadc"
            or event == "fcantidadd"
            or event == "fcantidade"
            or event == "fcantidadf"
            or event == "fcantidadg"
            or event == "fcantidadh"
            or event == "fcantidadi"
            or event == "fcantidadj"
            or event == "fcantidadk"
            or event == "fcantidadl"
            or event == "fcantidadll"
            or event == "fcantidadm"
            or event == "fcantidadn"
            or event == "fcantidadñ"
            or event == "fcantidado"
            or event == "fcantidadp"
            or event == "fcantidadq"
            or event == "fcantidadr"
            or event == "fcantidadrr"
            or event == "fcantidads"
            or event == "fcantidadt"
            or event == "fcantidadu"
            or event == "fcantidadv"
            or event == "fcantidadw"
            or event == "fcantidadx"
            or event == "fcantidady"
            or event == "fcantidadz"
            or event == "mcantidada"
            or event == "mcantidadb"
            or event == "mcantidadc"
            or event == "mcantidadd"
            or event == "mcantidade"
            or event == "mcantidadf"
            or event == "mcantidadg"
            or event == "mcantidadh"
            or event == "mcantidadi"
            or event == "mcantidadj"
            or event == "mcantidadk"
            or event == "mcantidadl"
            or event == "mcantidadll"
            or event == "mcantidadm"
            or event == "mcantidadn"
            or event == "mcantidadñ"
            or event == "mcantidado"
            or event == "mcantidadp"
            or event == "mcantidadq"
            or event == "mcantidadr"
            or event == "mcantidadrr"
            or event == "mcantidads"
            or event == "mcantidadt"
            or event == "mcantidadu"
            or event == "mcantidadv"
            or event == "mcantidadw"
            or event == "mcantidadx"
            or event == "mcantidady"
            or event == "mcantidadz"
            or event == "dcantidada"
            or event == "dcantidadb"
            or event == "dcantidadc"
            or event == "dcantidadd"
            or event == "dcantidade"
            or event == "dcantidadf"
            or event == "dcantidadg"
            or event == "dcantidadh"
            or event == "dcantidadi"
            or event == "dcantidadj"
            or event == "dcantidadk"
            or event == "dcantidadl"
            or event == "dcantidadll"
            or event == "dcantidadm"
            or event == "dcantidadn"
            or event == "dcantidadñ"
            or event == "dcantidado"
            or event == "dcantidadp"
            or event == "dcantidadq"
            or event == "dcantidadr"
            or event == "dcantidadrr"
            or event == "dcantidads"
            or event == "dcantidadt"
            or event == "dcantidadu"
            or event == "dcantidadv"
            or event == "dcantidadw"
            or event == "dcantidadx"
            or event == "dcantidady"
            or event == "dcantidadz"
        ):
            print("event pc")
            val_pc(values, event, window)
        if event == "-guardar-":
            if (values["fhora"] == "0") and (values["fmin"] == "0"):
                print("doble 0")
                window.FindElement("fmin").Update(1)
                values["fmin"] = "1"
            if (values["mhora"] == "0") and (values["mmin"] == "0"):
                window.FindElement("mmin").Update(1)
                values["mmin"] = "1"
            if (values["dhora"] == "0") and (values["dmin"] == "0"):
                window.FindElement("dmin").Update(1)
                values["dmin"] = "1"
            datos = {
                "dpuntosa": values["dpuntosa"],
                "dpuntosb": values["dpuntosb"],
                "dpuntosc": values["dpuntosc"],
                "dpuntosd": values["dpuntosd"],
                "dpuntose": values["dpuntose"],
                "dpuntosf": values["dpuntosf"],
                "dpuntosg": values["dpuntosg"],
                "dpuntosh": values["dpuntosh"],
                "dpuntosi": values["dpuntosi"],
                "dpuntosj": values["dpuntosj"],
                "dpuntosk": values["dpuntosk"],
                "dpuntosl": values["dpuntosl"],
                "dpuntosll": values["dpuntosll"],
                "dpuntosm": values["dpuntosm"],
                "dpuntosn": values["dpuntosn"],
                "dpuntosñ": values["dpuntosñ"],
                "dpuntoso": values["dpuntoso"],
                "dpuntosp": values["dpuntosp"],
                "dpuntosq": values["dpuntosq"],
                "dpuntosr": values["dpuntosr"],
                "dpuntoss": values["dpuntoss"],
                "dpuntost": values["dpuntost"],
                "dpuntosu": values["dpuntosu"],
                "dpuntosv": values["dpuntosv"],
                "dpuntosw": values["dpuntosw"],
                "dpuntosx": values["dpuntosx"],
                "dpuntosy": values["dpuntosy"],
                "dpuntosz": values["dpuntosz"],
                "dpuntosrr": values["dpuntosrr"],
                "dcantidada": values["dcantidada"],
                "dcantidadb": values["dcantidadb"],
                "dcantidadc": values["dcantidadc"],
                "dcantidadd": values["dcantidadd"],
                "dcantidade": values["dcantidade"],
                "dcantidadf": values["dcantidadf"],
                "dcantidadg": values["dcantidadg"],
                "dcantidadh": values["dcantidadh"],
                "dcantidadi": values["dcantidadi"],
                "dcantidadj": values["dcantidadj"],
                "dcantidadk": values["dcantidadk"],
                "dcantidadl": values["dcantidadl"],
                "dcantidadll": values["dcantidadll"],
                "dcantidadm": values["dcantidadm"],
                "dcantidadn": values["dcantidadn"],
                "dcantidadñ": values["dcantidadñ"],
                "dcantidado": values["dcantidado"],
                "dcantidadp": values["dcantidadp"],
                "dcantidadq": values["dcantidadq"],
                "dcantidadr": values["dcantidadr"],
                "dcantidads": values["dcantidads"],
                "dcantidadt": values["dcantidadt"],
                "dcantidadu": values["dcantidadu"],
                "dcantidadv": values["dcantidadv"],
                "dcantidadw": values["dcantidadw"],
                "dcantidadx": values["dcantidadx"],
                "dcantidady": values["dcantidady"],
                "dcantidadz": values["dcantidadz"],
                "dcantidadrr": values["dcantidadrr"],
                "fpuntosa": values["fpuntosa"],
                "fpuntosb": values["fpuntosb"],
                "fpuntosc": values["fpuntosc"],
                "fpuntosd": values["fpuntosd"],
                "fpuntose": values["fpuntose"],
                "fpuntosf": values["fpuntosf"],
                "fpuntosg": values["fpuntosg"],
                "fpuntosh": values["fpuntosh"],
                "fpuntosi": values["fpuntosi"],
                "fpuntosj": values["fpuntosj"],
                "fpuntosk": values["fpuntosk"],
                "fpuntosl": values["fpuntosl"],
                "fpuntosll": values["fpuntosll"],
                "fpuntosm": values["fpuntosm"],
                "fpuntosn": values["fpuntosn"],
                "fpuntosñ": values["fpuntosñ"],
                "fpuntoso": values["fpuntoso"],
                "fpuntosp": values["fpuntosp"],
                "fpuntosq": values["fpuntosq"],
                "fpuntosr": values["fpuntosr"],
                "fpuntoss": values["fpuntoss"],
                "fpuntost": values["fpuntost"],
                "fpuntosu": values["fpuntosu"],
                "fpuntosv": values["fpuntosv"],
                "fpuntosw": values["fpuntosw"],
                "fpuntosx": values["fpuntosx"],
                "fpuntosy": values["fpuntosy"],
                "fpuntosz": values["fpuntosz"],
                "fpuntosrr": values["fpuntosrr"],
                "fcantidada": values["fcantidada"],
                "fcantidadb": values["fcantidadb"],
                "fcantidadc": values["fcantidadc"],
                "fcantidadd": values["fcantidadd"],
                "fcantidade": values["fcantidade"],
                "fcantidadf": values["fcantidadf"],
                "fcantidadg": values["fcantidadg"],
                "fcantidadh": values["fcantidadh"],
                "fcantidadi": values["fcantidadi"],
                "fcantidadj": values["fcantidadj"],
                "fcantidadk": values["fcantidadk"],
                "fcantidadl": values["fcantidadl"],
                "fcantidadll": values["fcantidadll"],
                "fcantidadm": values["fcantidadm"],
                "fcantidadn": values["fcantidadn"],
                "fcantidadñ": values["fcantidadñ"],
                "fcantidado": values["fcantidado"],
                "fcantidadp": values["fcantidadp"],
                "fcantidadq": values["fcantidadq"],
                "fcantidadr": values["fcantidadr"],
                "fcantidads": values["fcantidads"],
                "fcantidadt": values["fcantidadt"],
                "fcantidadu": values["fcantidadu"],
                "fcantidadv": values["fcantidadv"],
                "fcantidadw": values["fcantidadw"],
                "fcantidadx": values["fcantidadx"],
                "fcantidady": values["fcantidady"],
                "fcantidadz": values["fcantidadz"],
                "fcantidadrr": values["fcantidadrr"],
                "mpuntosa": values["mpuntosa"],
                "mpuntosb": values["mpuntosb"],
                "mpuntosc": values["mpuntosc"],
                "mpuntosd": values["mpuntosd"],
                "mpuntose": values["mpuntose"],
                "mpuntosf": values["mpuntosf"],
                "mpuntosg": values["mpuntosg"],
                "mpuntosh": values["mpuntosh"],
                "mpuntosi": values["mpuntosi"],
                "mpuntosj": values["mpuntosj"],
                "mpuntosk": values["mpuntosk"],
                "mpuntosl": values["mpuntosl"],
                "mpuntosll": values["mpuntosll"],
                "mpuntosm": values["mpuntosm"],
                "mpuntosn": values["mpuntosn"],
                "mpuntosñ": values["mpuntosñ"],
                "mpuntoso": values["mpuntoso"],
                "mpuntosp": values["mpuntosp"],
                "mpuntosq": values["mpuntosq"],
                "mpuntosr": values["mpuntosr"],
                "mpuntoss": values["mpuntoss"],
                "mpuntost": values["mpuntost"],
                "mpuntosu": values["mpuntosu"],
                "mpuntosv": values["mpuntosv"],
                "mpuntosw": values["mpuntosw"],
                "mpuntosx": values["mpuntosx"],
                "mpuntosy": values["mpuntosy"],
                "mpuntosz": values["mpuntosz"],
                "mpuntosrr": values["mpuntosrr"],
                "mcantidada": values["mcantidada"],
                "mcantidadb": values["mcantidadb"],
                "mcantidadc": values["mcantidadc"],
                "mcantidadd": values["mcantidadd"],
                "mcantidade": values["mcantidade"],
                "mcantidadf": values["mcantidadf"],
                "mcantidadg": values["mcantidadg"],
                "mcantidadh": values["mcantidadh"],
                "mcantidadi": values["mcantidadi"],
                "mcantidadj": values["mcantidadj"],
                "mcantidadk": values["mcantidadk"],
                "mcantidadl": values["mcantidadl"],
                "mcantidadll": values["mcantidadll"],
                "mcantidadm": values["mcantidadm"],
                "mcantidadn": values["mcantidadn"],
                "mcantidadñ": values["mcantidadñ"],
                "mcantidado": values["mcantidado"],
                "mcantidadp": values["mcantidadp"],
                "mcantidadq": values["mcantidadq"],
                "mcantidadr": values["mcantidadr"],
                "mcantidads": values["mcantidads"],
                "mcantidadt": values["mcantidadt"],
                "mcantidadu": values["mcantidadu"],
                "mcantidadv": values["mcantidadv"],
                "mcantidadw": values["mcantidadw"],
                "mcantidadx": values["mcantidadx"],
                "mcantidady": values["mcantidady"],
                "mcantidadz": values["mcantidadz"],
                "mcantidadrr": values["mcantidadrr"],
                "fhora": values["fhora"],
                "fmin": values["fmin"],
                "mhora": values["mhora"],
                "mmin": values["mmin"],
                "dhora": values["dhora"],
                "dmin": values["dmin"],
            }
            guardar(archivo_config, datos)
        if event == "-default-":
            cargar_default(window, keys, default_config)
            sg.popup("Configuracion por defecto cargada con exito")
    window.close()
