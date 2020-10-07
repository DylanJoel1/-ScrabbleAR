"""Trabajo Final"""
import PySimpleGUI as sg

from random import shuffle

import json

import random

import puntos

import guardar

import config 

from ClaseFicha import Ficha

from ClaseAtril import Atril

from ClaseEstante import Estante

from ClaseTablero import Tablero

from ClaseJugador import Jugador

from ClaseMaquina import Computadora

from funcionAutenticar import confirmar_Palabra

import datetime, time

import os

from os import path

import collections

import sys

import comoJugar

import configVer


#from Objetos.ClaseAtril import Atril
sys.path.insert(1, "/imagenes")


COLORES_POS_ESPECIALES = {
    "x2":  "#ffff66",
    "x3": "#ff0000",
    "x2let": "#1a53ff",
    "x3let": "#ff1a8c",
    "-2": "#ffeecc",
    "-3": "#ffccff",
    "-1": "#99ffd6"
}

# constante que representa los multiplicadores y descuentos
POS_ESPECIALES = {
    "facil": {
        "x2": [
            (1, 1),(2, 2),(4, 4),(6, 6),(13, 13),(12, 12),
            (10, 10),(8, 8),(1, 13),(2, 12),(4, 10),(6, 8),
            (13, 1),(12, 2),(10, 4),(8, 6),
        ],
        "x2letra": [
            (5, 5),(9, 9),(5, 9),(9, 5),(5, 1),(9, 1),
            (6, 2),(8, 2),(1, 5),(1, 9),(2, 6),(2, 8),
            (5, 13),(9, 13),(6, 12),(8, 12),(13, 5),
            (13, 9),(12, 6),(12, 8),
        ],
        "x3": [
            (0, 0), (14, 14), (0, 14), (14, 0), (7, 0), (0, 7), (7, 14), (14, 7)
            ],
        "x3letra": [
            (3, 0),(11, 0),(0, 3),(0, 11),(3, 14),(11, 14),(14, 3),(14, 11),
        ],
        "-2": [
            (7, 3), (3, 7), (7, 11), (11, 7)
            ],
        "-3": [
            (3, 3), (11, 11), (3, 11), (11, 3)
            ],
    },
    "medio": {
        "x2": [
            (1, 1),(2, 2),(4, 4),(6, 6),(13, 13), (12, 12),
            (10, 10),(8, 8),(1, 13), (2, 12),(4, 10),(6, 8),
            (13, 1), (12, 2),(10, 4),(8, 6),
        ],
        "x2letra": [
            (5, 1),(9, 1),(6, 2), (8, 2),(1, 5),(1, 9),(2, 6),
            (2, 8),(5, 13),(9, 13),(6, 12),(8, 12),(13, 5),
            (13, 9),(12, 6),(12, 8),
        ],
        "x3": [
            (0, 0), (14, 14), (0, 14), (14, 0), (7, 0), (0, 7), (7, 14), (14, 7)
            ],
        "x3letra": [
            (3, 0),(11, 0),(0, 3),(0, 11),(3, 14),(11, 14),(14, 3),(14, 11),
        ],
        "-2": [
            (5, 5), (9, 9), (5, 9), (9, 5), (7, 3), (3, 7), (7, 11), (11, 7)
            ],
        "-3": [
            (3, 3), (11, 11), (3, 11), (11, 3)
            ],
    },
    "dificil": {
        "x2": [
            (2, 2), (4, 4), (12, 12), (10, 10), (2, 12), (4, 10), (12, 2), (10, 4)
            ],
        "x2letra": [
            (5, 1), (9, 1), (1, 5), (1, 9), (5, 13), (9, 13), (13, 5), (13, 9)
            ],
        "x3": [
            (0, 0), (14, 14), (0, 14), (14, 0), (7, 0), (0, 7), (7, 14), (14, 7)
            ],
        "x3letra": [
            (3, 0),(11, 0),(0, 3),(0, 11),(3, 14),(11, 14),(14, 3),(14, 11),
        ],
        "-2": [
            (5, 5), (9, 9), (5, 9), (9, 5)
            ],
        "-3": [
            (3, 3), (11, 11), (3, 11), (11, 3), (7, 3), (3, 7), (7, 11), (11, 7)
            ],
    },
}

# constante que representa el atril del jugador
ATRIL_JUGADOR = ["" for i in range(7)]

TIEMPO_LIMITE_PARTIDA = datetime.datetime.now() + datetime.timedelta(seconds=60)

def retornar_pos_especiales(window, pos, tablero,dificultad):
    if pos in POS_ESPECIALES[dificultad.replace("-", "")]["x2"]:
        tablero.quitar_elemento(window, pos, COLORES_POS_ESPECIALES["x2"])
    elif pos in POS_ESPECIALES[dificultad.replace("-", "")]["x2letra"]:
        tablero.quitar_elemento(window, pos, COLORES_POS_ESPECIALES["x2let"])
    elif pos in POS_ESPECIALES[dificultad.replace("-", "")]["x3"]:
        tablero.quitar_elemento(window, pos, COLORES_POS_ESPECIALES["x3"])
    elif pos in POS_ESPECIALES[dificultad.replace("-", "")]["x3letra"]:
        tablero.quitar_elemento(window, pos, COLORES_POS_ESPECIALES["x3let"])
    elif pos in POS_ESPECIALES[dificultad.replace("-", "")]["-2"]:
        tablero.quitar_elemento(window, pos, COLORES_POS_ESPECIALES["-2"])
    elif pos in POS_ESPECIALES[dificultad.replace("-", "")]["-3"]:
        tablero.quitar_elemento(window, pos, COLORES_POS_ESPECIALES["-3"])
    else:
        tablero.quitar_elemento(window, pos)

    



def cargar():
    # Carga el archivo de configuracion
    try:
        with open("guardado/datos.json", "r") as jsonFile:
            datos = json.load(jsonFile)
        return datos
    except FileNotFoundError:
        sg.popup(
            "No se encontró el archivo, se procedera a cargar un por defecto..."
        )
        with open("guardado/datos_default.json", "r") as jsonFile:
            datos = json.load(jsonFile)
        return datos


def guardar_partida(
    w,
    h,
    sw,
    sh,
    fichas_cant,
    fichas_punt,
    atril,
    jugador_estante,
    tablero,
    sigue,
    juega,
    turno_Act,
    tomo_ficha,
    puede_colocar,
    no_termina_turno,
    pos_ficha_anterior,
    fichas_colocadas,
    palabra_formada,
    dificultad,
    palabras_en_tablero,
    ficha_pos,
    pos_fichas_estante,
    puede_cambiar_letras,
    contador_clickeadas,
    tiempo,
    maquina,
    cantidad_cambios,
    ficha_pos_fija
):
    # guarda la partida
    atrilStr = atril.atril
    atril1 = []
    atril2 = []
    for x in atrilStr:
        atril1.append(x.letra)
        atril2.append(x.valor)
    estantej = jugador_estante.estante.estante
    estante1 = []
    estante2 = []
    for x in estantej:
        try:
            estante1.append(x.letra)
            estante2.append(x.valor)
        except AttributeError:
            try:
                estante1.append(x)
                estante2.append(fichas_punt[x])
            except KeyError:
                pass
    estantec = maquina.estante.estante
    estantec1 = []
    estantec2 = []
    for y in estantec:
        try:
            estantec1.append(y.letra)
            estantec2.append(y.valor)
        except AttributeError:
            try:
                estantec1.append(y)
                estantec2.append(fichas_punt[y])
            except KeyError:
                pass
    datos = {
        "w": w,
        "h": h,
        "sw": sw,
        "sh": sh,
        "fichas_cant": fichas_cant,
        "fichas_punt": fichas_punt,
        "atril1": atril1,
        "atril2": atril2,
        "jugador_estante": {
            "nombre": jugador_estante.nombre,
            "estante1": estante1,
            "estante2": estante2,
            "puntaje": jugador_estante.puntaje,
        },
        "maquina": {
            "estante1": estantec1,
            "estante2": estantec2,
            "puntaje": maquina.puntaje,
        },
        "tablero": tablero.tablero,
        "sigue": sigue,
        "juega": juega,
        "turno_Act": turno_Act,
        "tomo_ficha": tomo_ficha,
        "puede_colocar": puede_colocar,
        "no_termina_turno": no_termina_turno,
        "pos_ficha_anterior": pos_ficha_anterior,
        "fichas_colocadas": fichas_colocadas,
        "palabra_formada": palabra_formada,
        "dificultad": dificultad,
        "palabras_en_tablero": palabras_en_tablero,
        "ficha_pos": ficha_pos,
        "pos_fichas_estante": pos_fichas_estante,
        "puede_cambiar_letras": puede_cambiar_letras,
        "contador_clickeadas": contador_clickeadas,
        "tiempo": tiempo,
        "cantidad_cambios":cantidad_cambios,
        "ficha_pos_fija":ficha_pos_fija
    }
    return datos


def estante_ps(estante, window):
    # actualiza el estante con las letras que le toco al jugador
    i = 0
    for _ in estante:
        # print(estante[i].get_letra())
        window.FindElement(i).Update(
            text=estante[i].get_letra(),
            image_filename=("imagenes/" + estante[i].get_letra() + ".png"),
        )
        i = i + 1


def datos(dificultad):
    # Devuelve la cantidad de fichas y los puntajes de cada una dependiendo de la dificultad y el archivo de configuracion
    if dificultad == "-facil-":
        valores = cargar()
        keysp = []
        for x in puntos.keys:
            keysp.append("fpuntos"+((str(x))).lower())
        keysc = []
        for x in puntos.keys:
            keysc.append("fcantidad"+((str(x))).lower())
        fichas_cant = {y: valores[x] for x, y in zip(keysc, puntos.keys)}
        fichas_punt = {y: valores[x] for x, y in zip(keysp, puntos.keys)}
        return fichas_cant, fichas_punt
    elif dificultad == "-medio-":
        valores = cargar()
        keysp = []
        for x in puntos.keys:
            keysp.append("mpuntos"+((str(x))).lower())
        keysc = []
        for x in puntos.keys:
            keysc.append("mcantidad"+((str(x))).lower())
        fichas_cant = {y: valores[x] for x, y in zip(keysc, puntos.keys)}
        fichas_punt = {y: valores[x] for x, y in zip(keysp, puntos.keys)}
        return fichas_cant, fichas_punt
    elif dificultad == "-dificil-":
        valores = cargar()
        keysp = []
        for x in puntos.keys:
            keysp.append("dpuntos"+((str(x))).lower())
        keysc = []
        for x in puntos.keys:
            keysc.append("dcantidad"+((str(x))).lower())
        fichas_cant = {y: valores[x] for x, y in zip(keysc, puntos.keys)}
        fichas_punt = {y: valores[x] for x, y in zip(keysp, puntos.keys)}
        return fichas_cant, fichas_punt


def salir_juego(evento):
    # Funcion que detecta si se salio del juego
    if evento is None:
        #Si clikean la X superior derecha se cierra la ventana antes de que salga el popup, por lo que si o si cierra el juego
        return True
    elif evento == "Salir":
        if sg.popup_yes_no('Desea salir del juego?') == "Yes":
            return True
        else:
            return False

def calcular_lugares(pos,tablero,palabra):
    """
        parametros
            pos:int (posicion de la cual parte a calcular las posiciones)
            tablero: Class
            palabra: string (palabra que se quiere colocar)

        return: Lista (lista con las pos disponibles)
    """
    indice_aux=pos[1]
    aux_contadora=0
    posiciones_disp=[]
    
    for _ in palabra:
        if indice_aux <14:
            if tablero[pos[0]][indice_aux] == False:
                posiciones_disp.append((pos[0],indice_aux))
                aux_contadora+=1
                indice_aux+=1
        else:
            break
    if aux_contadora==len(palabra):
        return posiciones_disp
    else:
        posiciones_disp=[]
        aux_contadora=0
        indice_aux=pos[1]
    
    for _ in palabra:
        if indice_aux > 0:
            if tablero[pos[0]][indice_aux]==False:
                posiciones_disp.append((pos[0],indice_aux))
                aux_contadora=aux_contadora+1
                indice_aux-=1
        else:
            break
    if aux_contadora==len(palabra):
        return posiciones_disp
    else:
        posiciones_disp=[]
        aux_contadora=0
        indice_aux=pos[0]
    for _ in palabra:
        if (indice_aux < 14):
            if (tablero[indice_aux][pos[1]]==False):
                posiciones_disp.append((indice_aux,pos[1]))
                aux_contadora = aux_contadora + 1
                indice_aux+=1
        else:
            break
    if aux_contadora==len(palabra):
        return posiciones_disp
    else:
        posiciones_disp=[]
        aux_contadora=0
        indice_aux=pos[0]
    
    for _ in palabra:
        if (indice_aux >0):
            if tablero[indice_aux][pos[1]]==False:
                posiciones_disp.append((indice_aux,pos[1]))
                aux_contadora+=1
                indice_aux-=1
        else:
            break
    if aux_contadora==len(palabra):
        return posiciones_disp 
    else:
        posiciones_disp=[]
    return posiciones_disp


def hay_espacio(
    window, lista_pos, tablero, direc="disponibles"):  
    """
        parametros:
            window: sg.window
            lista_pos: lista
            tablero: Class
            direc: String

        return: si el parametro direc usa su valor por defecto retorna una lista
        return: si el parametro direc referencia una direc retorna Boolean

        La función retorna todas las posiciones disponibles del tablero ó si hay espacio disponible hacia una dirección particular

    """
    if direc == "disponibles":
        aux = []
        if lista_pos[0] != 0:
            if tablero.tablero[lista_pos[0] - 1][lista_pos[1]] == False:
                aux.append([lista_pos[0] - 1, lista_pos[1]])
        if lista_pos[0] != 14:
            if tablero.tablero[lista_pos[0] + 1][lista_pos[1]] == False:
                aux.append([lista_pos[0] + 1, lista_pos[1]])
        if lista_pos[1] != 0:

            if tablero.tablero[lista_pos[0]][lista_pos[1] - 1] == False:
                aux.append([lista_pos[0], lista_pos[1] - 1])
        if lista_pos[1] != 14:

            if tablero.tablero[lista_pos[0]][lista_pos[1] + 1] == False:
                aux.append([lista_pos[0], lista_pos[1] + 1])
        return aux
    elif direc == "derecha":
        if lista_pos[1] != 14:

            if tablero.tablero[lista_pos[0]][lista_pos[1] + 1] == True:

                return False
            return True
        else:
            return False

    elif direc == "izquierda":
        if lista_pos[1] != 0:

            if tablero.tablero[lista_pos[0]][lista_pos[1] - 1] == True:
                return False
            return True
        else:
            return False
    elif direc == "arriba":
        if lista_pos[0] != 0:

            if tablero.tablero[lista_pos[0] - 1][lista_pos[1]] == True:

                return False
            return True
        else:
            return False
    elif direc == "abajo":
        if lista_pos[0] != 14:

            if tablero.tablero[lista_pos[0] + 1][lista_pos[1]] == True:
                return False
            return True
        else:
            return False


def so():
    # Funcion que detecta el sistema operativo para reacomodar el tamaño de las casillas (ya que en linux se ve diferente)
    try:
        if os.name != "nt" or os.name != "posix":
            WIDTH = 4
            HEIGHT = 2
            SW = 1000
            SH = 1000
            return WIDTH, HEIGHT, SW, SH
        elif os.name == "nt":
            WIDTH = 4
            HEIGHT = 2
            SW = 1000
            SH = 1000
            return WIDTH, HEIGHT, SW, SH
        elif os.name == "posix":
            WIDTH = 2
            HEIGHT = 1
            SW = 700
            SH = 700
            return WIDTH, HEIGHT, SW, SH
    except Exception:
        WIDTH = 4
        HEIGHT = 2
        SW = 1000
        SH = 1000
        return WIDTH, HEIGHT, SW, SH


def tablero_especial(window, dificultad):
    """
        Pone las fichas especiales en el tablero segun la dificultad
        parametros:
            window:sg.window
            dificultad:String
    """
    for pos in POS_ESPECIALES[dificultad]["x2"]:
        window.FindElement(pos).Update(button_color=("black",COLORES_POS_ESPECIALES["x2"]))
    for pos in POS_ESPECIALES[dificultad]["x2letra"]:
        window.FindElement(pos).Update(button_color=("black",COLORES_POS_ESPECIALES["x2let"]))
    for pos in POS_ESPECIALES[dificultad]["x3"]:
        window.FindElement(pos).Update(button_color=("black",COLORES_POS_ESPECIALES["x3"]))
    for pos in POS_ESPECIALES[dificultad]["x3letra"]:
        window.FindElement(pos).Update(button_color=("black",COLORES_POS_ESPECIALES["x3let"]))
    for pos in POS_ESPECIALES[dificultad]["-2"]:
        window.FindElement(pos).Update(button_color=("black",COLORES_POS_ESPECIALES["-2"]))
    for pos in POS_ESPECIALES[dificultad]["-3"]:
        window.FindElement(pos).Update(button_color=("black",COLORES_POS_ESPECIALES["-3"]))


def tiempo_int():
    return int(round(time.time() * 100))


def fin(jugador_estante=None, maquina=None):
    sg.Popup("Se acabó la partida")
    if (jugador_estante != None) and (maquina != None):
        estantej = jugador_estante.estante.estante
        estantec = maquina.estante.estante
        puntospj = jugador_estante.puntaje
        puntospc = maquina.puntaje
    else:
        estantej = puntos.estantejglobal.estante.estante
        estantec = puntos.estantecglobal.estante.estante
        puntospj = puntos.estantejglobal.puntaje
        puntospc = puntos.estantecglobal.puntaje
    estante1 = []
    estante2 = []
    for x in estantej:
        try:
            estante1.append(x.letra)
            estante2.append(x.valor)
        except AttributeError:
            try:
                estante1.append(x)
                estante2.append(puntos.fichas_punt_global[x])
            except KeyError:
                pass
    estantec1 = []
    estantec2 = []
    for y in estantec:
        try:
            estantec1.append(y.letra)
            estantec2.append(y.valor)
        except AttributeError:
            try:
                estantec1.append(y)
                estantec2.append(puntos.fichas_punt_global[y])
            except KeyError:
                pass
    restapj = 0
    restapc = 0
    for valor in estante2:
        restapj = restapj + int(valor)
    for valor in estantec2:
        restapc = restapc + int(valor)
    sg.Popup("Puntaje Jugador:", puntospj, " Puntaje Maquina:", puntospc)
    sg.Popup("A tu puntaje se le resta:", restapj, " Al puntaje de la maquina se le resta:", restapc)
    puntospj = puntospj - restapj
    puntospc = puntospc - restapc
    if puntospc < 0:
        puntospc = 0
    if puntospj < 0:
        puntospj = 0
    sg.Popup("Puntaje Jugador:", puntospj, " Puntaje Maquina:", puntospc)
    
    if puntospj > puntospc:
        nombre = "null"
        nombre=sg.popup_get_text("Ganaste, Ingresa tu nombre:")
        while nombre == "":
            nombre=sg.popup_get_text("Ingresa un nombre valido:")
        sg.Popup("Nombre:",nombre,"Puntuacion:", puntospj)
        try:
            with open("guardado/top10.json", "r") as jsonFile:
                top10 = json.load(jsonFile)
        except Exception:
            with open("guardado/top10vacio.json", "r") as jsonFile:
                top10 = json.load(jsonFile)
        minimo = 9999
        minimon = 1
        for a in range(10):
            if int(top10[list(top10.keys())[a]]) < int(minimo):
                minimo = top10[list(top10.keys())[a]]
                minimon = a
        if puntospj > minimo:
            top10[nombre] = top10.pop(list(top10.keys())[minimon])
            top10[nombre] = puntospj
            top10s = sorted(top10.items(), key=lambda kv: kv[1])
            top10s.reverse()
            top10or = collections.OrderedDict(top10s)
            config.guardar("guardado/top10.json",top10or)
        else:
            sg.Popup("Tu puntaje no es suficiente para entrar al top 10")
    else:
        sg.Popup("Perdiste")


def cargar_fichas(ficha_pos_fija,window):
    for key in ficha_pos_fija:
        k2 = eval(key)
        window.FindElement(k2).Update(image_filename="imagenes/"+ficha_pos_fija[key]+".png")



def main(dificultad, datosC):
    # Se inicializan todas las variables a utilizar y se ejecuta el juego en si
    if datosC != None:
        dificultad = datosC["dificultad"]
        w, h, sw, sh = so()
        fichas_cant, fichas_punt = datosC["fichas_cant"], datosC["fichas_punt"]
        atril = Atril(None, None, datosC)
        jugador_estante = Jugador(atril, datosC)
        tablero = Tablero(datosC)
        sigue = datosC["sigue"]
        juega = datosC["juega"]
        turno_Act = datosC["turno_Act"]
        tomo_ficha = datosC["tomo_ficha"]
        puede_colocar = datosC["puede_colocar"]
        no_termina_turno = datosC["no_termina_turno"]
        pos_ficha_anterior = datosC["pos_ficha_anterior"]
        fichas_colocadas = datosC["fichas_colocadas"]
        palabra_formada = datosC["palabra_formada"]
        primera = 1
        poder_guardar = False
        ficha_pos = datosC["ficha_pos"]
        pos_fichas_estante = datosC["pos_fichas_estante"]

        puede_cambiar_letras=datosC["puede_cambiar_letras"]
        marcar_fichas=False
        contador_clickeadas=datosC["contador_clickeadas"]
        tiempo = datosC["tiempo"]
        tiempo_act = 0
        tiempo_ini = tiempo_int()
        maquina= Computadora(atril,0,"",datosC)
        cantidad_cambios = datosC["cantidad_cambios"]
        puntos.fichas_punt_global = fichas_punt
        ficha_pos_fija = datosC["ficha_pos_fija"]
        puede_retornar_ficha=False
        
    else:
        datosA = cargar()
        w, h, sw, sh = so()
        fichas_cant, fichas_punt = datos(dificultad)
        puntos.fichas_punt_global = fichas_punt
        atril = Atril(fichas_cant, fichas_punt)
        jugador_estante = Jugador(atril)
        tablero = Tablero()
        maquina= Computadora(atril)

        sigue = 0
        juega = False
        puede_cambiar_letras=1
        ficha_pos_fija = {}

        marcar_fichas=False
        contador_clickeadas=-1
        tomo_ficha = False
        puede_colocar = False
        no_termina_turno = True
        pos_ficha_anterior = []
        ficha_pos = {}
        fichas_colocadas = 0
        palabra_formada = ""
        pos_fichas_estante = []

        primera = 0
        poder_guardar = True
        puede_retornar_ficha = False
        if dificultad == "-facil-":
            aux = (int(datosA["fhora"])*60)*60
            aux = aux + int(datosA["fmin"])*60
            tiempo = (aux*100)
        elif dificultad == "-medio-":
            aux = (int(datosA["mhora"])*60)*60
            aux = aux + int(datosA["mmin"])*60
            tiempo = (aux*100)
        else:
            aux = (int(datosA["dhora"])*60)*60
            aux = aux + int(datosA["dmin"])*60
            tiempo = (aux*100)
        tiempo_act = 0
        tiempo_ini = tiempo_int()

    layout2 = [
        [
            sg.B(
                "",
                button_color=("black", "white"),
                key=(i, j),
                size=(w, h),
                pad=(2, 2),
                disabled_button_color=("black", "white"),
            )
            for j in range(15)
        ]
        for i in range(15)
    ]
    layout2.append(
        [
            sg.T("", font=("Arial ", 15), key="-Turno-", size=(18, 1), text_color="black"), 
            sg.T("Tiempo restante:", font=("arial", 15)),
            sg.T("", font=("arial", 15), key="-tiempo-", size=(30, 1))
        ]
    )
    layout2.append([sg.T("Estante Jugador", font=("arial", 15), size=(37, 1)), sg.T("Estante Computadora", font=("arial", 15))])
    layout2.append(
        [
            sg.B("", button_color=("black", "white"), key=(0), size=(w, h), pad=(2, 2)),
            sg.B("", button_color=("black", "white"), key=(1), size=(w, h), pad=(2, 2)),
            sg.B("", button_color=("black", "white"), key=(2), size=(w, h), pad=(2, 2)),
            sg.B("", button_color=("black", "white"), key=(3), size=(w, h), pad=(2, 2)),
            sg.B("", button_color=("black", "white"), key=(4), size=(w, h), pad=(2, 2)),
            sg.B("", button_color=("black", "white"), key=(5), size=(w, h), pad=(2, 2)),
            sg.B("", button_color=("black", "white"), key=(6), size=(w, h), pad=(2, 2)),
            sg.T("", size=(3, 1)),
            sg.B("", button_color=("black", "white"), key=(7), size=(w, h), pad=(2, 2), disabled=True),
            sg.B("", button_color=("black", "white"), key=(8), size=(w, h), pad=(2, 2), disabled=True),
            sg.B("", button_color=("black", "white"), key=(9), size=(w, h), pad=(2, 2), disabled=True),
            sg.B("", button_color=("black", "white"), key=(10), size=(w, h), pad=(2, 2), disabled=True),
            sg.B("", button_color=("black", "white"), key=(11), size=(w, h), pad=(2, 2), disabled=True),
            sg.B("", button_color=("black", "white"), key=(12), size=(w, h), pad=(2, 2), disabled=True),
            sg.B("", button_color=("black", "white"), key=(13), size=(w, h), pad=(2, 2), disabled=True),
        ]
    )  # Desde que puse el layout3 y el layout aca se duplican keys???
    layout2.append(
        [
            sg.B(
                "Confirmar Palabra",
                disabled=True,
                size=(14, 2),
                button_color=("black", "green"),
                disabled_button_color=("#2e2e1f", "green"),
            ),
            sg.B(
                "retornar ficha",
                size=(14, 2),
                disabled=True,
                button_color=("black", "#FFA500"),
                disabled_button_color=("#2e2e1f", "#FFA500"),
                key="-devolver_ficha-",
            ),
            sg.B(
                "Cambiar Ficha/s",
                button_color=("black","#FFA500"),
                disabled=False,size=(14,2), 
                key="-cambiar_fichas-"
            ),
            sg.B(
                "Cambiar todas las fichas",
                button_color=("black","#FFA500"),
                disabled=False,size=(14,2), 
                key="-cambiar_todas_fichas-"
            ),
            sg.B(
                "Confirmar",
                button_color=("black","#FFA500"),
                disabled= True, size=(10, 2),
                key="-confirmar_letras-"
                
            )
            
        ]
    )
    layout2.append(
        [
            sg.B("Jugar", size=(8, h)),
            sg.B("Terminar", size=(8, h), visible=True),
            sg.B("Salir", size=(8, h), button_color=("black", "#ff4d4d")),
            sg.B("Guardar", size=(8, h), visible=False)
        ]
    )

    layout3 = [

        [
            sg.T("Puntaje Jugador:", font=("arial", 15)),
            sg.T("0", font=("arial", 15,), size=(5, 1), key="-puntaje-"),
            sg.T("Puntaje Computadora:", font=("arial", 15)),
            sg.T("0", font=("arial", 15,), size=(5, 1), key="-puntajepc-"),
        ],
        [sg.Multiline(size=(30, 20), disabled=True, autoscroll=False, key="-out-"),
        sg.Multiline(size=(30, 20), disabled=True, autoscroll=False, key="-outpc-")],
        [sg.T("Casillas con premio o descuento:", font=("arial", 15))],
        [
            sg.T("Palabras x2:"),
            sg.B("", button_color=("black", COLORES_POS_ESPECIALES["x2"])),
            sg.T("Palabras x3:"),
            sg.B("", button_color=("black", COLORES_POS_ESPECIALES["x3"])),
            sg.T("Letras x2:"),
            sg.B("", button_color=("black", COLORES_POS_ESPECIALES["x2let"])),
            sg.T("Letras x3:"),
            sg.B("", button_color=("black", COLORES_POS_ESPECIALES["x3let"])),
        ],
        [
            sg.T("Descuento -1:"),
            sg.B("", button_color=("black",COLORES_POS_ESPECIALES["-1"])),
            sg.T("Descuento -2:"),
            sg.B("", button_color=("black",COLORES_POS_ESPECIALES["-2"])),
            sg.T("Descuento -3:"),
            sg.B("", button_color=("black", COLORES_POS_ESPECIALES["-3"])),
        ],
    ]
    if dificultad == "-facil-":
        layout3.append(
            [
                sg.T("Dificultad:", font=("arial", 15)),
                sg.T(text="Fácil", font=("arial", 15,), size=(5, 1)),
            ]
        )
        layout3.append([sg.T("Se permite cualquier tipo de palabra (Sustantivos, adjetivos y verbos)")])
    elif dificultad == "-medio-":
        layout3.append(
            [
                sg.T("Dificultad:", font=("arial", 15)),
                sg.T(text="Medio", font=("arial", 15,), size=(5, 1)),
            ]
        )
        layout3.append([sg.T("Solo se permiten verbos y adjetivos")])
    else:
        layout3.append(
            [
                sg.T("Dificultad:", font=("arial", 15)),
                sg.T(text="Difícil", font=("arial", 15,), size=(5, 1)),
            ]
        )
        layout3.append([sg.T("Solo se permiten verbos y adjetivos")])

    layout3.append([sg.B("Como Jugar", size=(10, h), key="-comojugar-")])
    layout3.append([sg.B("Configuracion", size=(12, h), key="-verconfig-")])

    layout = [
        [
            sg.TabGroup(
                [
                    [
                        sg.Tab("Tablero", layout2, key="elemt"),
                        sg.Tab("Datos", layout3, key="elemd"),
                    ]
                ]
            )
        ]
    ]
    window = sg.Window(
        "ScrabbleAR", size=(sw, sh), element_justification="c", resizable=True
    ).Layout(layout)
    while True:
       
           # La variable "primera" se utiliza para preparar la interfaz cuando se clikea el boton "jugar"
      
        if primera == 1:
            window.Finalize()
            arregloEstante = jugador_estante.get_estante()
            estante_ps(arregloEstante, window)
            window.FindElement("Jugar").Update(visible=False)
            juega = datosC["juega"]
            palabras_en_tablero = datosC["palabras_en_tablero"]
            estante = jugador_estante.get_estante()
            if dificultad == "-facil-":
                tablero_especial(window, "facil")
            elif dificultad == "-medio-":
                tablero_especial(window, "medio")
            else:
                tablero_especial(window, "dificil")
            cargar_fichas(ficha_pos_fija,window)
            window.FindElement("-puntaje-").Update(jugador_estante.puntaje)
            window.FindElement("-puntajepc-").Update(maquina.puntaje)
            window.FindElement("Terminar").Update(visible=True)
            primera = 0

        event, _ = window.Read(timeout=10)
        tiempo_act = tiempo_int() - tiempo_ini
        tiempoR = tiempo - tiempo_act

        if salir_juego(event):
            break
        if event == "-comojugar-":
            comoJugar.Reglas()
        if event == "-verconfig-":
            configVer.Ver(dificultad)
        if event == "Jugar":
            # Si toca jugar carga el estante del jugador con las fichas aleatorias, bloquea el tablero y guarda en una variable que ya inicio el juego
            arregloEstante = jugador_estante.get_estante()
            estante_ps(arregloEstante, window)
            
            estante = jugador_estante.get_estante()
            window.FindElement("Terminar").Update(visible=True)
            window.FindElement("Jugar").Update(visible=False)            
            window.FindElement("Guardar").Update(visible=True)
            # Preparo el tablero con sus casillas especiales
            if dificultad == "-facil-":
                tablero_especial(window, "facil")
            elif dificultad == "-medio-":
                tablero_especial(window, "medio")
            else:
                tablero_especial(window, "dificil")

            juega = True

            palabras_en_tablero = 0

            # Genero de forma aleatoria quien inicia a jugar
            turno_Act = random.choice(range(1, 3))

            # Muestro en pantalla el turno actual
            if turno_Act == 1:
                window.FindElement("-Turno-").Update(value="Turno de el jugador",background_color="green")
            else:
                window.FindElement("-Turno-").Update(value="Turno de la maquina",background_color="#008B8B")
            #Inicio el tiempo
            tiempo_ini = tiempo_int()
            
            cantidad_cambios=3
        elif juega:
            # Si ya se tocó el boton de jugar inicia a preguntar por los turnos y preparar el tablero para las jugadas



            if no_termina_turno == False:
                # Si el turno del jugador terminó reseteo el contador de fichas colocadas
                fichas_colocadas = 0

            #El tiempo representado
            prim = 1
            if tiempoR > 0:
                window.FindElement('-tiempo-').Update('{:02d}:{:02d}.{:02d}'.format((tiempoR // 100) // 60, (tiempoR // 100) % 60, tiempoR % 100))
            else:
                window.FindElement('-tiempo-').Update('00:00.00')
                if prim == 1:
                    fin(jugador_estante,maquina)
                    prim = 0
                    break
                  
            
            # --------------------------------------------TURNO JUGADOR---------------------------------------------
            if cantidad_cambios >0:
                window.FindElement("-cambiar_fichas-").Update("Cambiar Ficha/s ("+str(cantidad_cambios)+")",disabled=True)
                window.FindElement("-cambiar_todas_fichas-").Update("Cambiar todas las fichas ("+str(cantidad_cambios)+")",disabled=True)
            if (event == "-cambiar_todas_fichas-") and  turno_Act==1:
                puntos.estantejglobal = jugador_estante
                turno_Act = 2
                no_termina_turno= False
                if jugador_estante.estante.cambiar_fichas(window, ATRIL_JUGADOR) == False:
                    fin(None, None)
                    sg.popup("Se terminaron Las fichas")
                time.sleep(1)
                window.FindElement("-Turno-").Update(
                            value="Turno de la maquina",
                            background_color="#008B8B"
                        )
                cantidad_cambios-=1

            if event == "-cambiar_fichas-" and  turno_Act==1:
                sg.popup("Clikea las fichas que quiere cambiar, cuando termine aprete el boton 'confirmar' ")
                window.FindElement("-confirmar_letras-").Update(disabled=False)
                turno_Act=0
                marcar_fichas=True
            
            if marcar_fichas:
                if event in range(7):
                    
                    
                    ficha = str(estante[event])
                    
                    ficha = ficha.split(
                        ","
                    )
                    ATRIL_JUGADOR[event]=ficha[0]
                    
                    window.FindElement(event).Update(disabled=True)
                    
                    contador_clickeadas= ATRIL_JUGADOR.count("")
        
                if  contador_clickeadas == 0:
                    cantidad_cambios-=1
                    time.sleep(1)
                    turno_Act = 2
                    no_termina_turno= False
                    if jugador_estante.estante.cambiar_fichas(window) == False:
                        fin(None,None)
                    marcar_fichas=False
                    contador_clickeadas=-1
                    for i in range(7):
                    
                        window.FindElement(i).Update(disabled=False)
                    
                        ATRIL_JUGADOR[i]=""

                        
                if event== "-confirmar_letras-":
                    cantidad_cambios-=1
                    puntos.estantejglobal = jugador_estante
                    turno_Act = 2
                    no_termina_turno=False
                    marcar_fichas=False
                    if jugador_estante.estante.cambiar_fichas(window,"marcadas") == False:
                        fin(None,None)
                    for i in range(7):
                        window.FindElement(i).Update(disabled=False)
                    
                        ATRIL_JUGADOR[i]=""
                    window.FindElement("-confirmar_letras-").Update(disabled=True)
                    time.sleep(1)
                    window.FindElement("-Turno-").Update(
                            value="Turno de la maquina",
                            background_color="#008B8B"
                        )
                    window.FindElement("-cambiar_fichas-").Update(disabled=True)
                    window.FindElement("-cambiar_todas_fichas-").Update(disabled=True)
                    


            if (turno_Act == 1) and (no_termina_turno):
                # si es el turno del jugador y su turno aun no finaliza:
                if poder_guardar:
                    window.FindElement("Guardar").Update(visible=True)
                    poder_guardar = False

                if puede_cambiar_letras == 1 and cantidad_cambios >0:
                    window.FindElement("-cambiar_fichas-").Update(disabled=False)
                    window.FindElement("-cambiar_todas_fichas-").Update(disabled=False)
                
                
                
                if fichas_colocadas > 0 and puede_retornar_ficha:
                    # Si ya colocó una ficha aparece el boton para recuperarla
                    window.FindElement("-devolver_ficha-").Update(disabled=False)
                else:
                    window.FindElement("-devolver_ficha-").Update(disabled=True)

                if event in range(7) and puede_colocar==False:
                    # CLIKEA UNA FICHA:
                    
                    estante = jugador_estante.get_estante()
                    
                    puede_retornar_ficha=False
                    
                    window.FindElement("-cambiar_fichas-").Update(disabled=True)
                    window.FindElement("-cambiar_todas_fichas-").Update(disabled=True)
                        
                    window.FindElement("-devolver_ficha-").Update(disabled=True)
                    window.Finalize()
                    
                    window.FindElement("Guardar").Update(visible=False)
                    evento_ficha = event
                    ficha = str(estante[event])
                    ficha = ficha.split(
                        ","
                    )  # Tengo la ficha separada como (letra,valor)
                    jugador_estante.estante.quitar_Ficha_De_Estante(
                        evento_ficha, window, ATRIL_JUGADOR
                    )
                    sigue = 1
                    puede_colocar = True
                if event == "-devolver_ficha-" and fichas_colocadas > 0:
                    puede_colocar = False
                    sigue = 0
                    jugador_estante.estante.retornar_Ficha_Al_Estante(
                        window, pos_fichas_estante[len(pos_fichas_estante) - 1], ATRIL_JUGADOR
                    )
                    pos = pos_ficha_anterior[len(pos_ficha_anterior) - 1]
                    #Reviso si la ficha que saqué del tablero tenia una casilla especial
                    #Para retornar la imagen a su lugar correspondiente
                    retornar_pos_especiales(window,pos,tablero,dificultad)
                    tablero.tablero[pos[0]][pos[1]] = False
                    fichas_colocadas -= 1
                    if fichas_colocadas < 3:
                        window.FindElement(
                            "Confirmar Palabra").Update(disabled=True)
                    ATRIL_JUGADOR[pos_fichas_estante[len(pos_fichas_estante) - 1]] = ""
                    pos_fichas_estante.pop()
                    pos_ficha_anterior.pop()
                    list(ficha_pos_fija)[-1]
                    list(ficha_pos)[-1]
                    palabra_formada = palabra_formada[:-1]

                    window.finalize()

                # COLOCA LA FICHA EN EL TABLERO

                if sigue == 1:
                    
                    pos_libres_para_colocar=[]
                    
                    if palabras_en_tablero == 0 and fichas_colocadas == 0:
                        # si no hay palabras en el tablero y tampoco hay fichas colocadas solo desbloqueo el centro del tablero
                        

                        pos_libres_para_colocar.append((7,7))

                    if fichas_colocadas == 0 and palabras_en_tablero > 0:
                        # Si ya hay palabras formadas en el tablero y no coloqué fichas, desbloqueo todas las pos adyacentes a las palabras formadas
                        
                        pos_adyacentes = tablero.Pos_Libres_Tablero()
                        for pos in pos_adyacentes:
                            pos_libres_para_colocar.append((pos[0],pos[1]))
                    
                    if fichas_colocadas == 1:
                        # Si ya colocó una ficha desbloqueo los lugares disponibles que esten adyacentes a la primera ficha colocada
                        pos_disponibles = hay_espacio(window, pos_ficha_anterior[0], tablero)
                        for pos in pos_disponibles:

                            pos_libres_para_colocar.append((pos[0],pos[1]))
                   
                    if fichas_colocadas > 1:
                        # Si ya colocó más de una ficha me fijo la direccion a la cual forma la palabra y controlo que no se le termine el tablero

                        if (
                            pos_ficha_anterior[0][0]
                            == pos_ficha_anterior[len(pos_ficha_anterior) - 1][0]
                        ):
                            # si en la lista de posiciones no cambió el primer valor (el valor de las filas) es porque la palabra se está formando de forma horizontal

                            if pos_ficha_anterior[0][1] < pos_ficha_anterior[
                                len(pos_ficha_anterior) - 1][1] and hay_espacio(window,
                                pos_ficha_anterior[len(pos_ficha_anterior) - 1],
                                tablero,
                                "derecha",
                            ):

                                pos_libres_para_colocar.append((pos_ficha_anterior[len(pos_ficha_anterior) - 1][0],
                                                                pos_ficha_anterior[len(pos_ficha_anterior) - 1][1]+1))

                            elif pos_ficha_anterior[0][1] > pos_ficha_anterior[
                                len(pos_ficha_anterior) - 1
                            ][1] and hay_espacio(
                                window,
                                pos_ficha_anterior[len(pos_ficha_anterior) - 1],
                                tablero,
                                "izquierda",
                            ):

                                pos_libres_para_colocar.append((pos_ficha_anterior[0][0],
                                                                pos_ficha_anterior[len(pos_ficha_anterior) - 1][1]- 1
                                                                ))
                            else:
                                # Si no tenia espacio a la izquierda o a la derecha entra a el else
                                sigue = 0
                                puede_colocar = False
                                sg.Popup(
                                    "No hay más espacio en el tablero, confirme la"
                                    " palabra o intente formar otra"
                                )
                                jugador_estante.estante.retornar_Ficha_Al_Estante(
                                    window, evento_ficha, ATRIL_JUGADOR
                                )
                                ATRIL_JUGADOR[evento_ficha]=""

                        else:
                            # Si entra en este else es porque el valor de la columna de la primera ficha colocada y la ultima no cambió, por lo tanto la palabra se forma de manera vertical

                            if pos_ficha_anterior[0][0] < pos_ficha_anterior[
                                len(pos_ficha_anterior) - 1
                            ][0] and hay_espacio(
                                window,
                                pos_ficha_anterior[len(pos_ficha_anterior) - 1],
                                tablero,
                                "abajo",
                            ):

                                pos_libres_para_colocar.append((pos_ficha_anterior[len(pos_ficha_anterior) - 1][0]+ 1,
                                                                pos_ficha_anterior[len(pos_ficha_anterior) - 1][1])
                                                                )
                                

                            elif pos_ficha_anterior[0][0] > pos_ficha_anterior[
                                len(pos_ficha_anterior) - 1
                            ][0] and hay_espacio(
                                window, pos_ficha_anterior[0], tablero, "arriba"):

                                pos_libres_para_colocar.append((pos_ficha_anterior[len(pos_ficha_anterior) - 1][0]-1,
                                                                pos_ficha_anterior[0][1]))

                            else:
                                # qué pasa si no se puede formar más la palabra
                                sigue = 0
                                puede_colocar = False
                                sg.Popup(
                                    "No hay más espacio en el tablero, confirme la"
                                    " palabra o intente formar otra"
                                )
                                jugador_estante.estante.retornar_Ficha_Al_Estante(
                                    window, evento_ficha, ATRIL_JUGADOR
                                )
                        
                                ATRIL_JUGADOR[evento_ficha]=""
                        
                    for pos in pos_libres_para_colocar:
                        window.FindElement(pos).Update(button_color=("black", "green"))
                    if (
                        puede_colocar
                        and not (event in range(7))
                        and isinstance(event, tuple) and event in pos_libres_para_colocar
                    ):
                        # si la variable puede colocar está en true, el evento no es el atril y el evento es una tupla, coloco la ficha
                        
                        
                        for pos_ant in pos_libres_para_colocar:
                            window.FindElement(pos_ant).Update(button_color=("black", "white"))
                            if pos_ant != event:
                                retornar_pos_especiales(
                                    window, pos_ant, tablero, dificultad)
                        window.FindElement(event).Update(
                            text=ficha[0],
                            image_filename=(("imagenes/" + ficha[0] + ".png")),
                        )
                        ATRIL_JUGADOR[evento_ficha] = ficha[0]
                        # vuelvo a desbloquear el atril para que puedan seguir tomando fichas
                        jugador_estante.estante.desbloquear_pos_Estante(window, ATRIL_JUGADOR)
                        # Me guardo las posiciones en las cuales colocó una ficha
                        pos_ficha_anterior.append(event)
                        # agrego la ficha junto a su posicion para luego ver si hay un multiplicador
                        ficha_pos_fija.update({str(event):ficha[0]})
                        ficha_pos.update({event:ficha[0]})
                        fichas_colocadas = fichas_colocadas + 1
                        sigue = 0
                        palabra_formada += ficha[0]
                        pos_fichas_estante.append(evento_ficha)
                        puede_colocar=False
                        puede_cambiar_letras=0
                        window.FindElement("-cambiar_fichas-").Update(disabled=True)
                        window.FindElement("-cambiar_todas_fichas-").Update(disabled=True)
                        puede_retornar_ficha=True


                if fichas_colocadas == 2:
                    # Si ya colocó 2 fichas aparece el boton para confirmar palabra
                    window.FindElement("Confirmar Palabra").Update(disabled=False)

                if event == "Confirmar Palabra":

                    if confirmar_Palabra(palabra_formada, dificultad):
                        
                        puede_cambiar_letras=1
                        
                        puntos_provisional = puntos.puntaje_palabra(
                            fichas_punt, palabra_formada, window, "-out-"
                        )
                        for pos in pos_ficha_anterior:
                            puntos_provisional = puntos.multipal(
                                pos[0],
                                pos[1],
                                dificultad,
                                puntos_provisional,
                                POS_ESPECIALES,
                                window,
                                "-out-"
                            )
                            tablero.tablero[pos[0]][pos[1]] = True
                        agregado = 0
                        for key in ficha_pos:
                            agregado = agregado + puntos.multilet(
                                key,
                                ficha_pos[key],
                                dificultad,
                                fichas_punt,
                                POS_ESPECIALES,
                                window,
                                "-out-"
                            )
                        puntos_provisional += agregado
                        jugador_estante.incrementar_puntaje(puntos_provisional, window)
                        poder_guardar = True
                        jugador_estante.estante.eliminar_fichas_estante(ATRIL_JUGADOR)
                        if jugador_estante.estante.agregar_fichas( window, ATRIL_JUGADOR) == False:
                            fin(None, None)
                        sigue = 0
                        puntos.estantejglobal = jugador_estante
                        turno_Act = 2
                        palabras_en_tablero += 1
                        fichas_colocadas = 0
                        puede_colocar = False
                        no_termina_turno = False
                        window.FindElement("Confirmar Palabra").Update(disabled=True)
                        window.FindElement("-Turno-").Update(
                            value="Turno de la maquina",
                            background_color="#008B8B"
                        )
                        for pos in range(len(ATRIL_JUGADOR)):
                            if ATRIL_JUGADOR[pos] != "":
                                ATRIL_JUGADOR[pos] = ""
                        pos_fichas_estante = []
                        palabra_formada = ""
                        ficha_pos = {}
                        # Vuelvo a desbloquear el estante para que siga jugando con las nuevas fichas
                        jugador_estante.estante.desbloquear_pos_Estante(window,ATRIL_JUGADOR)
                    else:
                        
                        sg.Popup("No era una palabra")
                        puede_colocar = False
                        poder_guardar = True
                        window.FindElement("Confirmar Palabra").Update(disabled=True)
                        sigue = 0

                        for pos in pos_fichas_estante:
                            jugador_estante.estante.retornar_Ficha_Al_Estante(
                                window, pos,ATRIL_JUGADOR 
                            )
                            ATRIL_JUGADOR[pos] = ""
                        for pos in pos_ficha_anterior:
                            # Si la pos de las fichas utilizadas eran una casilla especial, vuelvo a colocar la imagen de la ficha especial en su lugar
                            retornar_pos_especiales(
                                window, pos, tablero, dificultad)
                            tablero.tablero[pos[0]][pos[1]] = False
                        #Se coloca en 1 para volver a habilitar los botones de cambiar fichas
                        puede_cambiar_letras=1

                        pos_ficha_anterior = []
                        pos_fichas_estante = []
                        fichas_colocadas = 0
                        ficha_pos = {}
                        palabra_formada = ""

                if event == "Guardar":
                    datosg = guardar_partida(
                        w,
                        h,
                        sw,
                        sh,
                        fichas_cant,
                        fichas_punt,
                        atril,
                        jugador_estante,
                        tablero,
                        sigue,
                        juega,
                        turno_Act,
                        tomo_ficha,
                        puede_colocar,
                        no_termina_turno,
                        pos_ficha_anterior,
                        fichas_colocadas,
                        palabra_formada,
                        dificultad,
                        palabras_en_tablero,
                        ficha_pos,
                        pos_fichas_estante,
                        puede_cambiar_letras,
                        contador_clickeadas,
                        tiempoR,
                        maquina,
                        cantidad_cambios,
                        ficha_pos_fija
                    )
                    guardar.main(datosg)
                
                if event == "Terminar":
                    if sg.popup_yes_no('Desea finalizar la partida?') == "Yes":
                        fin(jugador_estante, maquina)
                        break

            elif turno_Act == 2:

                #Tomo letras y se las asigno a la maquina
                letras=""
                estante_maquina=maquina.get_estante()
                for elem in estante_maquina:
                    #Le envío a la maquina todas las letras juntas
                    aux=str(elem)
                    letras+= aux[0]
                maquina.set_letras(letras)
                palabra=maquina.crearPalabra(dificultad)
                if palabra != "":
                
                    if palabras_en_tablero==0:
                        aux=7
                        puntos_pc = puntos.puntaje_palabra(
                            fichas_punt, palabra, window, "-outpc-"
                        )
                        for let in palabra:
                            window.FindElement((7,aux)).Update(
                                text=let,
                                image_filename=(("imagenes/" + let + ".png")),
                            )
                            ficha_pos_fija.update({str((7,aux)):let})
                            puntos_pc = puntos.multipal(
                                7,
                                aux,
                                dificultad,
                                puntos_pc,
                                POS_ESPECIALES,
                                window,
                                "-outpc-"
                            )
                            agregado = 0
                            agregado = agregado + puntos.multilet(
                                    (7,aux),
                                    let,
                                    dificultad,
                                    fichas_punt,
                                    POS_ESPECIALES,
                                    window,
                                    "-outpc-"
                             )
                            puntos_pc = puntos_pc + agregado
                        
                            aux+=1
                            time.sleep(1)
                            window.Finalize()
                            tablero.tablero[7][aux-1]=True
                        maquina.incrementar_puntaje(puntos_pc, window)
                        palabras_en_tablero+=1
                    elif palabras_en_tablero > 0:
                        puede_formar_palabra=True
                        while puede_formar_palabra:
                        #En caso de que la posicion que tomé de las disponibles no tiene lugar hacia ninguna dirección para formar la palabra:
                        #Sigue en el bucle hasta que encuentre una posicion
                            pos_adyacentes_libres = tablero.Pos_Libres_Tablero()
                            pos= random.choice(pos_adyacentes_libres)
                            pos_adyacentes_libres.remove(pos)
                            posiciones_disponibles=calcular_lugares(pos,tablero.tablero,palabra)
                            if (posiciones_disponibles != []):
                                #Si la funcion que me calcula las posiciones hacia las que puedo formar la palabra no me devuelve una lista vacía:
                                #Formo la palabra
                                puntos_pc = puntos.puntaje_palabra(
                                fichas_punt, palabra, window, "-outpc-"
                                )
                                pos_letra=0
                                for coor in posiciones_disponibles:
                                    window.FindElement((coor[0],coor[1])).Update(
                                        text=palabra[pos_letra],
                                        image_filename=(("imagenes/" + palabra[pos_letra] + ".png")),
                                    )
                                    ficha_pos_fija.update({str((coor[0],coor[1])):palabra[pos_letra]})
                                    puntos_pc = puntos.multipal(
                                            coor[0],
                                            coor[1],
                                            dificultad,
                                            puntos_pc,
                                            POS_ESPECIALES,
                                            window,
                                            "-outpc-"
                                        )
                                    agregado = 0
                                
                                    agregado = agregado + puntos.multilet(
                                            (coor[0],coor[1]),
                                            palabra[pos_letra],
                                            dificultad,
                                            fichas_punt,
                                            POS_ESPECIALES,
                                            window,
                                            "-outpc-"
                                            )
                                    puntos_pc = puntos_pc + agregado
                                    pos_letra+=1
                                    tablero.tablero[coor[0]][coor[1]]=True
                                    time.sleep(1)
                                    window.Finalize()
                                maquina.incrementar_puntaje(puntos_pc, window)
                                palabras_en_tablero+=1
                
                                puede_formar_palabra=False
                    if maquina.cambiar_letras(palabra, ATRIL_JUGADOR) == False:
                        fin(None,None)
                else:
                    if maquina.pedir_fichas_nuevas(ATRIL_JUGADOR) == False:
                        fin(None,None)
                
                puntos.estantecglobal = maquina
                turno_Act = 1
                no_termina_turno = True
                sigue = 0
                pos_ficha_anterior = []
                time.sleep(2)
                window.FindElement("-Turno-").Update(
                    value="Turno de el jugador",
                    background_color="green",
    
                )
    window.Close()
