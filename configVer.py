import PySimpleGUI as sg
import json
from os import path
import sys
from config import guardar, cargar

sys.path.insert(1, "/guardado")

archivo_config = path.join(path.dirname(__file__), r"guardado/datos.json")
default_config = path.join(path.dirname(__file__), r"guardado/datos_default.json")

def Ver(dif):

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
            sg.T("",size=(2, 1), key="fhora"),
            sg.T("horas", justification="left", size=(4, 1)),
            sg.T("",size=(2, 1), key="fmin"),
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
            sg.T("",size=(2, 1), key="mhora"),
            sg.T("horas", justification="left", size=(4, 1)),
            sg.T("",size=(2, 1), key="mmin"),
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
            sg.T("",size=(2, 1), key="dhora"),
            sg.T("horas", justification="left", size=(4, 1)),
            sg.T("",size=(2, 1), key="dmin"),
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
            sg.T("",size=(2, 1), key="fpuntosa"),
            sg.T("",size=(2, 1), key="fcantidada"),
        ],
        [
            sg.T("B", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosb"),
            sg.T("",size=(2, 1), key="fcantidadb"),
        ],
        [
            sg.T("C", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosc"),
            sg.T("",size=(2, 1), key="fcantidadc"),
        ],
        [
            sg.T("D", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosd"),
            sg.T("",size=(2, 1), key="fcantidadd"),
        ],
        [
            sg.T("E", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntose"),
            sg.T("",size=(2, 1), key="fcantidade"),
        ],
        [
            sg.T("F", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosf"),
            sg.T("",size=(2, 1), key="fcantidadf"),
        ],
        [
            sg.T("G", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosg"),
            sg.T("",size=(2, 1), key="fcantidadg"),
        ],
        [
            sg.T("H", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosh"),
            sg.T("",size=(2, 1), key="fcantidadh"),
        ],
        [
            sg.T("I", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosi"),
            sg.T("",size=(2, 1), key="fcantidadi"),
        ],
        [
            sg.T("J", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosj"),
            sg.T("",size=(2, 1), key="fcantidadj"),
        ],
    ]

    columnaf2 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("K", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosk"),
            sg.T("",size=(2, 1), key="fcantidadk"),
        ],
        [
            sg.T("L", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosl"),
            sg.T("",size=(2, 1), key="fcantidadl"),
        ],
        [
            sg.T("LL", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosll"),
            sg.T("",size=(2, 1), key="fcantidadll"),
        ],
        [
            sg.T("M", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosm"),
            sg.T("",size=(2, 1), key="fcantidadm"),
        ],
        [
            sg.T("N", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosn"),
            sg.T("",size=(2, 1), key="fcantidadn"),
        ],
        [
            sg.T("Ñ", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosñ"),
            sg.T("",size=(2, 1), key="fcantidadñ"),
        ],
        [
            sg.T("O", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntoso"),
            sg.T("",size=(2, 1), key="fcantidado"),
        ],
        [
            sg.T("P", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosp"),
            sg.T("",size=(2, 1), key="fcantidadp"),
        ],
        [
            sg.T("Q", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosq"),
            sg.T("",size=(2, 1), key="fcantidadq"),
        ],
        [
            sg.T("R", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosr"),
            sg.T("",size=(2, 1), key="fcantidadr"),
        ],
    ]

    columnaf3 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("RR", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosrr"),
            sg.T("",size=(2, 1), key="fcantidadrr"),
        ],
        [
            sg.T("S", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntoss"),
            sg.T("",size=(2, 1), key="fcantidads"),
        ],
        [
            sg.T("T", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntost"),
            sg.T("",size=(2, 1), key="fcantidadt"),
        ],
        [
            sg.T("U", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosu"),
            sg.T("",size=(2, 1), key="fcantidadu"),
        ],
        [
            sg.T("V", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosv"),
            sg.T("",size=(2, 1), key="fcantidadv"),
        ],
        [
            sg.T("W", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosw"),
            sg.T("",size=(2, 1), key="fcantidadw"),
        ],
        [
            sg.T("X", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosx"),
            sg.T("",size=(2, 1), key="fcantidadx"),
        ],
        [
            sg.T("Y", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosy"),
            sg.T("",size=(2, 1), key="fcantidady"),
        ],
        [
            sg.T("Z", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="fpuntosz"),
            sg.T("",size=(2, 1), key="fcantidadz"),
        ],
    ]

    columnam1 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("A", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosa"),
            sg.T("",size=(2, 1), key="mcantidada"),
        ],
        [
            sg.T("B", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosb"),
            sg.T("",size=(2, 1), key="mcantidadb"),
        ],
        [
            sg.T("C", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosc"),
            sg.T("",size=(2, 1), key="mcantidadc"),
        ],
        [
            sg.T("D", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosd"),
            sg.T("",size=(2, 1), key="mcantidadd"),
        ],
        [
            sg.T("E", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntose"),
            sg.T("",size=(2, 1), key="mcantidade"),
        ],
        [
            sg.T("F", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosf"),
            sg.T("",size=(2, 1), key="mcantidadf"),
        ],
        [
            sg.T("G", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosg"),
            sg.T("",size=(2, 1), key="mcantidadg"),
        ],
        [
            sg.T("H", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosh"),
            sg.T("",size=(2, 1), key="mcantidadh"),
        ],
        [
            sg.T("I", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosi"),
            sg.T("",size=(2, 1), key="mcantidadi"),
        ],
        [
            sg.T("J", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosj"),
            sg.T("",size=(2, 1), key="mcantidadj"),
        ],
    ]

    columnam2 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("K", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosk"),
            sg.T("",size=(2, 1), key="mcantidadk"),
        ],
        [
            sg.T("L", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosl"),
            sg.T("",size=(2, 1), key="mcantidadl"),
        ],
        [
            sg.T("LL", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosll"),
            sg.T("",size=(2, 1), key="mcantidadll"),
        ],
        [
            sg.T("M", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosm"),
            sg.T("",size=(2, 1), key="mcantidadm"),
        ],
        [
            sg.T("N", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosn"),
            sg.T("",size=(2, 1), key="mcantidadn"),
        ],
        [
            sg.T("Ñ", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosñ"),
            sg.T("",size=(2, 1), key="mcantidadñ"),
        ],
        [
            sg.T("O", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntoso"),
            sg.T("",size=(2, 1), key="mcantidado"),
        ],
        [
            sg.T("P", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosp"),
            sg.T("",size=(2, 1), key="mcantidadp"),
        ],
        [
            sg.T("Q", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosq"),
            sg.T("",size=(2, 1), key="mcantidadq"),
        ],
        [
            sg.T("R", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosr"),
            sg.T("",size=(2, 1), key="mcantidadr"),
        ],
    ]

    columnam3 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("RR", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosrr"),
            sg.T("",size=(2, 1), key="mcantidadrr"),
        ],
        [
            sg.T("S", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntoss"),
            sg.T("",size=(2, 1), key="mcantidads"),
        ],
        [
            sg.T("T", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntost"),
            sg.T("",size=(2, 1), key="mcantidadt"),
        ],
        [
            sg.T("U", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosu"),
            sg.T("",size=(2, 1), key="mcantidadu"),
        ],
        [
            sg.T("V", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosv"),
            sg.T("",size=(2, 1), key="mcantidadv"),
        ],
        [
            sg.T("W", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosw"),
            sg.T("",size=(2, 1), key="mcantidadw"),
        ],
        [
            sg.T("X", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosx"),
            sg.T("",size=(2, 1), key="mcantidadx"),
        ],
        [
            sg.T("Y", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosy"),
            sg.T("",size=(2, 1), key="mcantidady"),
        ],
        [
            sg.T("Z", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="mpuntosz"),
            sg.T("",size=(2, 1), key="mcantidadz"),
        ],
    ]

    columnad1 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("A", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosa"),
            sg.T("",size=(2, 1), key="dcantidada"),
        ],
        [
            sg.T("B", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosb"),
            sg.T("",size=(2, 1), key="dcantidadb"),
        ],
        [
            sg.T("C", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosc"),
            sg.T("",size=(2, 1), key="dcantidadc"),
        ],
        [
            sg.T("D", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosd"),
            sg.T("",size=(2, 1), key="dcantidadd"),
        ],
        [
            sg.T("E", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntose"),
            sg.T("",size=(2, 1), key="dcantidade"),
        ],
        [
            sg.T("F", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosf"),
            sg.T("",size=(2, 1), key="dcantidadf"),
        ],
        [
            sg.T("G", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosg"),
            sg.T("",size=(2, 1), key="dcantidadg"),
        ],
        [
            sg.T("H", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosh"),
            sg.T("",size=(2, 1), key="dcantidadh"),
        ],
        [
            sg.T("I", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosi"),
            sg.T("",size=(2, 1), key="dcantidadi"),
        ],
        [
            sg.T("J", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosj"),
            sg.T("",size=(2, 1), key="dcantidadj"),
        ],
    ]

    columnad2 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("K", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosk"),
            sg.T("",size=(2, 1), key="dcantidadk"),
        ],
        [
            sg.T("L", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosl"),
            sg.T("",size=(2, 1), key="dcantidadl"),
        ],
        [
            sg.T("LL", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosll"),
            sg.T("",size=(2, 1), key="dcantidadll"),
        ],
        [
            sg.T("M", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosm"),
            sg.T("",size=(2, 1), key="dcantidadm"),
        ],
        [
            sg.T("N", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosn"),
            sg.T("",size=(2, 1), key="dcantidadn"),
        ],
        [
            sg.T("Ñ", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosñ"),
            sg.T("",size=(2, 1), key="dcantidadñ"),
        ],
        [
            sg.T("O", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntoso"),
            sg.T("",size=(2, 1), key="dcantidado"),
        ],
        [
            sg.T("P", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosp"),
            sg.T("",size=(2, 1), key="dcantidadp"),
        ],
        [
            sg.T("Q", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosq"),
            sg.T("",size=(2, 1), key="dcantidadq"),
        ],
        [
            sg.T("R", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosr"),
            sg.T("",size=(2, 1), key="dcantidadr"),
        ],
    ]

    columnad3 = [
        [sg.T("       P      C", justification="left", size=(9, 1))],
        [
            sg.T("RR", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosrr"),
            sg.T("",size=(2, 1), key="dcantidadrr"),
        ],
        [
            sg.T("S", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntoss"),
            sg.T("",size=(2, 1), key="dcantidads"),
        ],
        [
            sg.T("T", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntost"),
            sg.T("",size=(2, 1), key="dcantidadt"),
        ],
        [
            sg.T("U", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosu"),
            sg.T("",size=(2, 1), key="dcantidadu"),
        ],
        [
            sg.T("V", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosv"),
            sg.T("",size=(2, 1), key="dcantidadv"),
        ],
        [
            sg.T("W", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosw"),
            sg.T("",size=(2, 1), key="dcantidadw"),
        ],
        [
            sg.T("X", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosx"),
            sg.T("",size=(2, 1), key="dcantidadx"),
        ],
        [
            sg.T("Y", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosy"),
            sg.T("",size=(2, 1), key="dcantidady"),
        ],
        [
            sg.T("Z", justification="left", size=(2, 1)),
            sg.T("",size=(2, 1), key="dpuntosz"),
            sg.T("",size=(2, 1), key="dcantidadz"),
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
                "P y C significan Puntos y Cantidad respectivamente.",
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
                "P y C significan Puntos y Cantidad respectivamente",
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
                "P y C significan Puntos y Cantidad respectivamente.",
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
                        sg.Tab("Facil", facil_layout, key="-fl-",disabled=False),
                        sg.Tab("Medio", medio_layout, key="-ml-", disabled=False),
                        sg.Tab("Dificil", dificil_layout, key="-dl-", disabled=False),
                    ]
                ]
            )
        ],
        [
            sg.B(
                "Volver", size=(8, 2), key="-volver-", button_color=("black", "#FA8072")
            ),
        ],
    ]

    window = sg.Window("Configuracion", layout_Config)

    while True:
        if primera == 1:
            window.Finalize()
            if dif == "-facil-":
                window.FindElement("-ml-").Update(disabled=True)
                window.FindElement("-dl-").Update(disabled=True)
            elif dif == "-medio-":
                window.FindElement("-dl-").Update(disabled=True)
                window.FindElement("-fl-").Update(disabled=True)
            elif dif == "-dificil-":
                window.FindElement("-ml-").Update(disabled=True)
                window.FindElement("-fl-").Update(disabled=True)

            cargar(window, keys, archivo_config, default_config)
            primera = 0
        event, values = window.read()
        if event is None or event == "-volver-":
            break
    window.close()