"""Trabajo Final"""
import PySimpleGUI as sg
from random import shuffle
import json
import random
import puntos
import guardar
import config
from funcionAutenticar import confirmar_Palabra
import datetime, time
import os
from os import path
import collections
import sys
sys.path.insert(1, "/imagenes")


# constante que representa los multiplicadores y descuentos
POS_ESPECIALES = {
    "facil": {
        "x2": [
            (1, 1),
            (2, 2),
            (4, 4),
            (6, 6),
            (13, 13),
            (12, 12),
            (10, 10),
            (8, 8),
            (1, 13),
            (2, 12),
            (4, 10),
            (6, 8),
            (13, 1),
            (12, 2),
            (10, 4),
            (8, 6),
        ],
        "x2letra": [
            (5, 5),
            (9, 9),
            (5, 9),
            (9, 5),
            (5, 1),
            (9, 1),
            (6, 2),
            (8, 2),
            (1, 5),
            (1, 9),
            (2, 6),
            (2, 8),
            (5, 13),
            (9, 13),
            (6, 12),
            (8, 12),
            (13, 5),
            (13, 9),
            (12, 6),
            (12, 8),
        ],
        "x3": [(0, 0), (14, 14), (0, 14), (14, 0), (7, 0), (0, 7), (7, 14), (14, 7)],
        "x3letra": [
            (3, 0),
            (11, 0),
            (0, 3),
            (0, 11),
            (3, 14),
            (11, 14),
            (14, 3),
            (14, 11),
        ],
        "-2": [(7, 3), (3, 7), (7, 11), (11, 7)],
        "-3": [(3, 3), (11, 11), (3, 11), (11, 3)],
    },
    "medio": {
        "x2": [
            (1, 1),
            (2, 2),
            (4, 4),
            (6, 6),
            (13, 13),
            (12, 12),
            (10, 10),
            (8, 8),
            (1, 13),
            (2, 12),
            (4, 10),
            (6, 8),
            (13, 1),
            (12, 2),
            (10, 4),
            (8, 6),
        ],
        "x2letra": [
            (5, 1),
            (9, 1),
            (6, 2),
            (8, 2),
            (1, 5),
            (1, 9),
            (2, 6),
            (2, 8),
            (5, 13),
            (9, 13),
            (6, 12),
            (8, 12),
            (13, 5),
            (13, 9),
            (12, 6),
            (12, 8),
        ],
        "x3": [(0, 0), (14, 14), (0, 14), (14, 0), (7, 0), (0, 7), (7, 14), (14, 7)],
        "x3letra": [
            (3, 0),
            (11, 0),
            (0, 3),
            (0, 11),
            (3, 14),
            (11, 14),
            (14, 3),
            (14, 11),
        ],
        "-2": [(5, 5), (9, 9), (5, 9), (9, 5), (7, 3), (3, 7), (7, 11), (11, 7)],
        "-3": [(3, 3), (11, 11), (3, 11), (11, 3)],
    },
    "dificil": {
        "x2": [(2, 2), (4, 4), (12, 12), (10, 10), (2, 12), (4, 10), (12, 2), (10, 4)],
        "x2letra": [(5, 1), (9, 1), (1, 5), (1, 9), (5, 13), (9, 13), (13, 5), (13, 9)],
        "x3": [(0, 0), (14, 14), (0, 14), (14, 0), (7, 0), (0, 7), (7, 14), (14, 7)],
        "x3letra": [
            (3, 0),
            (11, 0),
            (0, 3),
            (0, 11),
            (3, 14),
            (11, 14),
            (14, 3),
            (14, 11),
        ],
        "-2": [(5, 5), (9, 9), (5, 9), (9, 5)],
        "-3": [(3, 3), (11, 11), (3, 11), (11, 3), (7, 3), (3, 7), (7, 11), (11, 7)],
    },
}

# constante que representa el atril del jugador
ATRIL_JUGADOR = ["" for i in range(7)]

TIEMPO_LIMITE_PARTIDA = datetime.datetime.now() + datetime.timedelta(seconds=60)


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
    tiempo
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
        estante1.append(x.letra)
        estante2.append(x.valor)
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
        "tiempo": tiempo
    }
    print(datos)
    return datos


class Ficha:
    """
    Clase que crea una ficha. La inicializa con la letra y su valor
    """

    def __init__(self, letra, fichas_punt):
        # Inicializa una ficha, con la letra (string) y el diccionario con los valores
        self.letra = letra.upper()
        self.valor = fichas_punt

    def get_valor(self):
        # Devuelve el valor de la ficha
        return self.valor

    def get_letra(self):
        # Devuelve la letra de la ficha.
        return self.letra

    def __repr__(self):
        return self.letra + "," + str(self.valor)

    def __str__(self):
        aux = self.letra + "," + str(self.valor)
        return aux


class Atril:
    """
    Clase que crea el atril con 100 fichas por defecto
    """

    def __init__(self, fichas_cant=None, fichas_punt=None, datos=None):
        # Crea el atril y lo inicializa con 100 fichas por defecto
        # el if es por si se esta cargando una partida
        if fichas_cant == None and fichas_punt == None and datos != None:
            self.atril = []
            for x, y in zip(datos["atril1"], datos["atril2"]):
                self.atril.append(Ficha(x, y))
        else:
            self.atril = []
            self.inicializa_atril(fichas_cant, fichas_punt)

    def agregar(self, letra, cantidad):
        # agrega una letra, la cantidad de veces que se indique, al atril
        for a in range(int(cantidad)):
            self.atril.append(letra)

    def inicializa_atril(self, fichas_cant, fichas_punt):
        # agrega las fichas al atril y las mezcla (shuffle)
        self.agregar(Ficha("A", fichas_punt["A"]), fichas_cant["A"])
        self.agregar(Ficha("B", fichas_punt["B"]), fichas_cant["B"])
        self.agregar(Ficha("C", fichas_punt["C"]), fichas_cant["C"])
        self.agregar(Ficha("D", fichas_punt["D"]), fichas_cant["D"])
        self.agregar(Ficha("E", fichas_punt["E"]), fichas_cant["E"])
        self.agregar(Ficha("F", fichas_punt["F"]), fichas_cant["F"])
        self.agregar(Ficha("G", fichas_punt["G"]), fichas_cant["G"])
        self.agregar(Ficha("H", fichas_punt["H"]), fichas_cant["H"])
        self.agregar(Ficha("I", fichas_punt["I"]), fichas_cant["I"])
        self.agregar(Ficha("J", fichas_punt["J"]), fichas_cant["J"])
        self.agregar(Ficha("K", fichas_punt["K"]), fichas_cant["K"])
        self.agregar(Ficha("L", fichas_punt["L"]), fichas_cant["L"])
        self.agregar(Ficha("LL", fichas_punt["LL"]), fichas_cant["LL"])
        self.agregar(Ficha("M", fichas_punt["M"]), fichas_cant["M"])
        self.agregar(Ficha("N", fichas_punt["N"]), fichas_cant["N"])
        self.agregar(Ficha("Ñ", fichas_punt["Ñ"]), fichas_cant["Ñ"])
        self.agregar(Ficha("O", fichas_punt["O"]), fichas_cant["O"])
        self.agregar(Ficha("P", fichas_punt["P"]), fichas_cant["P"])
        self.agregar(Ficha("Q", fichas_punt["Q"]), fichas_cant["Q"])
        self.agregar(Ficha("R", fichas_punt["R"]), fichas_cant["R"])
        self.agregar(Ficha("RR", fichas_punt["RR"]), fichas_cant["RR"])
        self.agregar(Ficha("S", fichas_punt["S"]), fichas_cant["S"])
        self.agregar(Ficha("T", fichas_punt["T"]), fichas_cant["T"])
        self.agregar(Ficha("U", fichas_punt["U"]), fichas_cant["U"])
        self.agregar(Ficha("V", fichas_punt["V"]), fichas_cant["V"])
        self.agregar(Ficha("W", fichas_punt["W"]), fichas_cant["W"])
        self.agregar(Ficha("X", fichas_punt["X"]), fichas_cant["X"])
        self.agregar(Ficha("Y", fichas_punt["Y"]), fichas_cant["Y"])
        self.agregar(Ficha("Z", fichas_punt["Z"]), fichas_cant["Z"])
        shuffle(self.atril)

    def quitar_ficha(self):
        # Quita una letra del atril y se la da al usuario
        if self.atril == []:
            print("Se acabaron las fichas")
        else:
            return self.atril.pop()

    def cant_letras(self):
        # Devuelve la cantidad de letras que quedan en el atril
        return len(self.atril)


class Estante:
    """
    Clase que crea el estante del jugador. Agrega fichas del atril al estante.
    """

    def __init__(self, atril, datos=None):
        # Inicializa el estante del jugador.
        if datos != None:
            self.estante = []
            self.atril = atril
            for x, y in zip(datos["estante1"], datos["estante2"]):
                self.estante.append(Ficha(x, y))
        else:
            self.estante = []
            self.atril = atril
            self.inicializar()

    def agregar_estante(self):
        # Agrega una ficha al estante quitando esa misma del atril
        self.estante.append(self.atril.quitar_ficha())
    
    def cambiar_fichas(self, window,cant="todas"):
        if cant=="todas":
            for i in range(len(ATRIL_JUGADOR)):
                self.estante[i] = self.atril.quitar_ficha()
                window.FindElement(i).Update(
                    text=self.estante[i].get_letra(),
                    image_filename=("imagenes/" + self.estante[i].get_letra()+ ".png"),
                
                )
        elif cant=="marcadas":
            for i in range(len(ATRIL_JUGADOR)):
                if ATRIL_JUGADOR[i]!="":
                    self.estante[i] = self.atril.quitar_ficha()
                    window.FindElement(i).Update(
                        text=self.estante[i].get_letra(),
                        image_filename=("imagenes/" + self.estante[i].get_letra()+ ".png"),
                
                    )   
        

    def agregar_fichas(self, cant, window):
        # agrega la cantidad de fichas que se le envían por parametro al estante del jugador.
        aux = []
        for i in range(len(ATRIL_JUGADOR)):
            if ATRIL_JUGADOR[i] != "":
                aux += [i]
        for pos in aux:
            self.estante[pos] = self.atril.quitar_ficha()
            window.FindElement(pos).Update(
                text=self.estante[pos].get_letra(),
                image_filename=("imagenes/" + self.estante[pos].get_letra() + ".png"),
            )

    def eliminar_fichas_estante(self, pos=""):
        # Elimina la ficha del estante, no solo de la interfaz
        if pos=="":
            for i in range(len(ATRIL_JUGADOR)):
                if ATRIL_JUGADOR[i] != "":
                    self.estante[i] = ""
        else:
            if ATRIL_JUGADOR[pos] !="":
                self.estante[pos]=""
    
    def no_tiene_fichas(self):

        elementos= self.estante.count("")
        if elementos == 7:
            return True
        else:
            return False
        

    def inicializar(self):
        # Añade las primeras 7 fichas al estante
        for i in range(7):
            self.agregar_estante()

    def quitar_estante(self, ficha):
        # Quita una ficha del estante
        self.estante.remove(ficha)

    def cant_estante(self):
        # Devuelve la cantidad de fichas que hay en el estante
        return len(self.estante)

    def get_estante(self):
        # Devuelve un arreglo con los elementos del estante, para poder representarlo en pysimplegui
        return self.estante

    def bloquear_Estante(self, window):
        # Bloquea el estante
        for i in range(7):
            window.FindElement(i).Update(disabled=True)

    def desbloquear_Estante(self, window):
        # desbloquea el estante
        for i in range(7):
            window.FindElement(i).Update(disabled=False)

    def desbloquear_pos_Estante(self, window):
        # desbloquea el estante
        for i in range(7):
            if ATRIL_JUGADOR[i] == "":
                window.FindElement(i).Update(disabled=False)

    def quitar_Ficha_De_Estante(self, bot, window):
        # quita de la interfaz una ficha del estante
        ATRIL_JUGADOR[bot] = window.FindElement(bot).get_text()
        window.FindElement(bot).Update(
            text="", image_size=(36, 38), image_filename="", disabled=True
        )

    def retornar_Ficha_Al_Estante(self, window, pos_estante):
        # devuelve una ficha del tablero al estante
        self.estante[pos_estante] = ATRIL_JUGADOR[pos_estante]
        if ATRIL_JUGADOR[pos_estante] == "":
            window.FindElement(pos_estante).Update(
                image_filename="", visible=True, image_size=(36, 38)
            )
        else:
            window.FindElement(pos_estante).Update(
                image_filename=(
                    ("imagenes/" + ATRIL_JUGADOR[pos_estante].upper() + ".png")
                ),
                visible=True,
            )
        self.desbloquear_Estante(window)


class Jugador:
    """
    Clase que crea una instancia de Jugador. Crea su estante y agrega su nombre.
    """

    def __init__(self, atril, datos=None):
        # Inicializa un Jugador con su estante.
        if datos != None:
            datosA = datos["jugador_estante"]
            self.nombre = datosA["nombre"]
            self.puntaje = datosA["puntaje"]
            self.estante = Estante(atril, datosA)
        else:
            self.nombre = ""
            self.estante = Estante(atril)
            self.puntaje = 0

    def incrementar_puntaje(self, agregado, window):
        # Incrementa el puntaje del jugador
        self.puntaje += agregado
        window["-puntaje-"].update(self.puntaje)

    def get_puntaje(self):
        # Devuelve el puntaje del jugador
        return self.puntaje

    def set_nombre(self, nombre):
        # Setea el nombre del jugador
        self.nombre = nombre

    def get_nombre(self):
        # Devuelve el nombre del jugador
        return self.nombre

    def get_estante(self):
        # Devuelve un arreglo con los elementos del estante, para poder representarlo en pysimplegui
        return self.estante.get_estante()


class Tablero:
    """
    Clase que representa al tablero para poder modificarlo
    """

    def __init__(self, datos=None):
        # Se inicializa el tablero
        if datos != None:
            self.tablero = datos["tablero"]
        else:
            self.tablero = [[False for j in range(15)] for i in range(15)]

    def mostrar_estado(self):
        # Imprime lo que contiene la variable que representa el tablero
        aux = ""
        for m in range(15):
            for n in range(15):
                aux += "|" + (str(self.tablero[m][n])) + "|"
            aux += "\n"
        print(aux)

    def agregar_elemento(self, element, window, img="", *pos):
        # Actualiza un boton del tablero con el texto que se le envíe
        self.tablero[pos[0]][pos[1]] = True
        window.FindElement((pos[0], pos[1])).Update(text=element)

    def quitar_elemento(self, window, pos, img=""):
        self.tablero[pos[0]][pos[1]] = False
        if img != "":
            window.FindElement(pos).Update(
                text="", image_filename=("imagenes/" + img + ".png")
            )
        else:
            window.FindElement(pos).Update(
                text="", image_filename="", image_size=(36, 38)
            )

    def bloquear_tablero(self, window):
        # Bloquea todas las pos del tablero
        for m in range(15):
            for n in range(15):
                window.FindElement((m, n)).Update(
                    disabled=True,
                    button_color=("black", "white"),
                    disabled_button_color=("black", "white"),
                )

    def desbloquear_tablero(self, window):
        # Desbloquea todas las pos del tablero
        for m in range(15):
            for n in range(15):
                window.FindElement((m, n)).Update(
                    disabled=False, button_color=("green", "green")
                )

    def desbloquear_Pos(self, window, x, y):
        # Desbloquea una pos en particular del tablero
        window.FindElement((x, y)).Update(
            disabled=False, button_color=("green", "green")
        )

    def bloquear_Pos(self, window, x, y):
        # Bloquea una pos en particular del tablero
        window.FindElement((x, y)).Update(
            disabled=True,
            button_color=("black", "white"),
            disabled_button_color=("black", "white"),
        )

    def Pos_Libres_Tablero(self):
        # Funcion que retorna una lista con las coordenadas de las pos disponibles adyacentes a las palabras formadas en el tablero
        coords = []
        for m in range(15):
            for n in range(15):
                if self.tablero[m][n] == True:
                    if m > 0:
                        # si no es la primera fila
                        if self.tablero[m - 1][n] == False:
                            coords.append((m - 1, n))
                    if m < 14:
                        # si no estoy en la ultima fila
                        if self.tablero[m + 1][n] == False:
                            coords.append((m + 1, n))
                    if n > 0:
                        # si no es la primera columna:
                        if self.tablero[m][n - 1] == False:
                            coords.append((m, n - 1))
                    if n < 14:
                        # Si no estoy en la ultima columna:
                        if self.tablero[m][n + 1] == False:
                            coords.append((m, n + 1))
        return coords


def estante_ps(estante, window):
    # actualiza el estante con las letras que le toco al jugador
    i = 0
    for x in estante:
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
        keys = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "LL",
            "M",
            "N",
            "Ñ",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "RR",
        ]
        keysp = [
            "fpuntosa",
            "fpuntosb",
            "fpuntosc",
            "fpuntosd",
            "fpuntose",
            "fpuntosf",
            "fpuntosg",
            "fpuntosh",
            "fpuntosi",
            "fpuntosj",
            "fpuntosk",
            "fpuntosl",
            "fpuntosll",
            "fpuntosm",
            "fpuntosn",
            "fpuntos\u00f1",
            "fpuntoso",
            "fpuntosp",
            "fpuntosq",
            "fpuntosr",
            "fpuntoss",
            "fpuntost",
            "fpuntosu",
            "fpuntosv",
            "fpuntosw",
            "fpuntosx",
            "fpuntosy",
            "fpuntosz",
            "fpuntosrr",
        ]
        keysc = [
            "fcantidada",
            "fcantidadb",
            "fcantidadc",
            "fcantidadd",
            "fcantidade",
            "fcantidadf",
            "fcantidadg",
            "fcantidadh",
            "fcantidadi",
            "fcantidadj",
            "fcantidadk",
            "fcantidadl",
            "fcantidadll",
            "fcantidadm",
            "fcantidadn",
            "fcantidad\u00f1",
            "fcantidado",
            "fcantidadp",
            "fcantidadq",
            "fcantidadr",
            "fcantidads",
            "fcantidadt",
            "fcantidadu",
            "fcantidadv",
            "fcantidadw",
            "fcantidadx",
            "fcantidady",
            "fcantidadz",
            "fcantidadrr",
        ]
        fichas_cant = {y: valores[x] for x, y in zip(keysc, keys)}
        fichas_punt = {y: valores[x] for x, y in zip(keysp, keys)}
        return fichas_cant, fichas_punt
    elif dificultad == "-medio-":
        valores = cargar()
        keys = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "LL",
            "M",
            "N",
            "Ñ",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "RR",
        ]
        keysp = [
            "mpuntosa",
            "mpuntosb",
            "mpuntosc",
            "mpuntosd",
            "mpuntose",
            "mpuntosf",
            "mpuntosg",
            "mpuntosh",
            "mpuntosi",
            "mpuntosj",
            "mpuntosk",
            "mpuntosl",
            "mpuntosll",
            "mpuntosm",
            "mpuntosn",
            "mpuntos\u00f1",
            "mpuntoso",
            "mpuntosp",
            "mpuntosq",
            "mpuntosr",
            "mpuntoss",
            "mpuntost",
            "mpuntosu",
            "mpuntosv",
            "mpuntosw",
            "mpuntosx",
            "mpuntosy",
            "mpuntosz",
            "mpuntosrr",
        ]
        keysc = [
            "mcantidada",
            "mcantidadb",
            "mcantidadc",
            "mcantidadd",
            "mcantidade",
            "mcantidadf",
            "mcantidadg",
            "mcantidadh",
            "mcantidadi",
            "mcantidadj",
            "mcantidadk",
            "mcantidadl",
            "mcantidadll",
            "mcantidadm",
            "mcantidadn",
            "mcantidad\u00f1",
            "mcantidado",
            "mcantidadp",
            "mcantidadq",
            "mcantidadr",
            "mcantidads",
            "mcantidadt",
            "mcantidadu",
            "mcantidadv",
            "mcantidadw",
            "mcantidadx",
            "mcantidady",
            "mcantidadz",
            "mcantidadrr",
        ]
        fichas_cant = {y: valores[x] for x, y in zip(keysc, keys)}
        fichas_punt = {y: valores[x] for x, y in zip(keysp, keys)}
        return fichas_cant, fichas_punt
    elif dificultad == "-dificil-":
        valores = cargar()
        keys = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "LL",
            "M",
            "N",
            "Ñ",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "RR",
        ]
        keysp = [
            "dpuntosa",
            "dpuntosb",
            "dpuntosc",
            "dpuntosd",
            "dpuntose",
            "dpuntosf",
            "dpuntosg",
            "dpuntosh",
            "dpuntosi",
            "dpuntosj",
            "dpuntosk",
            "dpuntosl",
            "dpuntosll",
            "dpuntosm",
            "dpuntosn",
            "dpuntos\u00f1",
            "dpuntoso",
            "dpuntosp",
            "dpuntosq",
            "dpuntosr",
            "dpuntoss",
            "dpuntost",
            "dpuntosu",
            "dpuntosv",
            "dpuntosw",
            "dpuntosx",
            "dpuntosy",
            "dpuntosz",
            "dpuntosrr",
        ]
        keysc = [
            "dcantidada",
            "dcantidadb",
            "dcantidadc",
            "dcantidadd",
            "dcantidade",
            "dcantidadf",
            "dcantidadg",
            "dcantidadh",
            "dcantidadi",
            "dcantidadj",
            "dcantidadk",
            "dcantidadl",
            "dcantidadll",
            "dcantidadm",
            "dcantidadn",
            "dcantidad\u00f1",
            "dcantidado",
            "dcantidadp",
            "dcantidadq",
            "dcantidadr",
            "dcantidads",
            "dcantidadt",
            "dcantidadu",
            "dcantidadv",
            "dcantidadw",
            "dcantidadx",
            "dcantidady",
            "dcantidadz",
            "dcantidadrr",
        ]
        fichas_cant = {y: valores[x] for x, y in zip(keysc, keys)}
        fichas_punt = {y: valores[x] for x, y in zip(keysp, keys)}
        return fichas_cant, fichas_punt


def salir_juego(evento):
    # Funcion que detecta si se salio del juego
    if evento is None or evento == "Salir":
        return True


def hay_espacio(
    window, lista_pos, tablero, direc="disponibles"
):  # Funcion que retorna si es válido o no colocar una ficha en la posición de la direccion asignada. En caso de no dar una direccion retorna una lista con todas las posiciones válidas que rodeen a la ultima ficha colocada.
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
    # Pone las fichas especiales en el tablero segun la dificultad
    for pos in POS_ESPECIALES[dificultad]["x2"]:
        window.FindElement(pos).Update(image_filename="imagenes/x2.png")
    for pos in POS_ESPECIALES[dificultad]["x2letra"]:
        window.FindElement(pos).Update(image_filename="imagenes/x2let.png")
    for pos in POS_ESPECIALES[dificultad]["x3"]:
        window.FindElement(pos).Update(image_filename="imagenes/x3.png")
    for pos in POS_ESPECIALES[dificultad]["x3letra"]:
        window.FindElement(pos).Update(image_filename="imagenes/x3let.png")
    for pos in POS_ESPECIALES[dificultad]["-2"]:
        window.FindElement(pos).Update(image_filename="imagenes/menos2.png")
    for pos in POS_ESPECIALES[dificultad]["-3"]:
        window.FindElement(pos).Update(image_filename="imagenes/menos3.png")


def tiempo_int():
    return int(round(time.time() * 100))


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
    else:
        datosA = cargar()
        w, h, sw, sh = so()
        fichas_cant, fichas_punt = datos(dificultad)
        atril = Atril(fichas_cant, fichas_punt)
        jugador_estante = Jugador(atril)
        tablero = Tablero()

        sigue = 0
        juega = False
        puede_cambiar_letras=1

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
        if dificultad == "-facil-":
            aux = int(datosA["fhora"])*120
            aux = aux + int(datosA["fmin"])*60
            tiempo = (aux*100)
        elif dificultad == "-medio-":
            aux = int(datosA["mhora"])*120
            aux = aux + int(datosA["mmin"])*60
            tiempo = (aux*100)
        else:
            aux = int(datosA["dhora"])*120
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
        [sg.T("", font=("arial", 15), size=(18, 1)),
        sg.T("", font=("arial", 15), key="-Turno-", size=(25, 1))]
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
        [sg.T("Tiempo restante:", font=("arial", 15)),
        sg.T("", font=("arial", 15), key="-tiempo-", size=(30,1))],
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
            sg.B("", image_filename="imagenes/x2.png"),
            sg.T("Palabras x3:"),
            sg.B("", image_filename="imagenes/x3.png"),
            sg.T("Letras x2:"),
            sg.B("", image_filename="imagenes/x2let.png"),
            sg.T("Letras x3:"),
            sg.B("", image_filename="imagenes/x3let.png"),
        ],
        [
            sg.T("Descuento -1:"),
            sg.B("", image_filename="imagenes/menos1.png"),
            sg.T("Descuento -2:"),
            sg.B("", image_filename="imagenes/menos2.png"),
            sg.T("Descuento -3:"),
            sg.B("", image_filename="imagenes/menos3.png"),
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
        if primera == 1:
            window.Finalize()
            arregloEstante = jugador_estante.get_estante()
            estante_ps(arregloEstante, window)
            tablero.bloquear_tablero(window)
            window.FindElement("Jugar").Update(visible=False)
            window.FindElement("Terminar").Update(visible=False)
            juega = datosC["juega"]
            palabras_en_tablero = datosC["palabras_en_tablero"]
            estante = jugador_estante.get_estante()
            if dificultad == "-facil-":
                tablero_especial(window, "facil")
            elif dificultad == "-medio-":
                tablero_especial(window, "medio")
            else:
                tablero_especial(window, "dificil")
            window.FindElement("-puntaje-").Update(jugador_estante.puntaje)
            window.FindElement("Terminar").Update(visible=True)
            primera = 0

        event, values = window.Read(timeout=10)
        tiempo_act = tiempo_int() - tiempo_ini
        tiempoR = tiempo - tiempo_act
        window.Maximize()
        if salir_juego(event):
            break
        if event == "Jugar":
            # Si toca jugar carga el estante del jugador con las fichas aleatorias, bloquea el tablero y guarda en una variable que ya inicio el juego
            arregloEstante = jugador_estante.get_estante()
            estante_ps(arregloEstante, window)
            tablero.bloquear_tablero(window)
            
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
                window.FindElement("-Turno-").Update(value="Turno de el jugador")
            else:
                window.FindElement("-Turno-").Update(value="Turno de la maquina")
            #Inicio el tiempo
            tiempo_ini = tiempo_int()

        elif juega:
            # Si ya se tocó el boton de jugar inicia a preguntar por los turnos y preparar el tablero para las jugadas

            if palabras_en_tablero == 0 and fichas_colocadas == 0:
                # si no hay palabras en el tablero y tampoco hay fichas colocadas solo desbloqueo el centro del tablero
                tablero.desbloquear_Pos(window, 7, 7)

            if no_termina_turno == False:
                # Si el turno del jugador terminó reseteo el contador de fichas colocadas
                fichas_colocadas = 0

            #El tiempo representado
            if tiempoR > 0:
                window.FindElement('-tiempo-').Update('{:02d}:{:02d}.{:02d}'.format((tiempoR // 100) // 60, (tiempoR // 100) % 60, tiempoR % 100))
            else:
                window.FindElement('-tiempo-').Update('00:00.00')

                    
            
            # --------------------------------------------TURNO JUGADOR---------------------------------------------
            if (event == "-cambiar_todas_fichas-") and  turno_Act==1:
                time.sleep(1)
                turno_Act = 2
                no_termina_turno= False
                jugador_estante.estante.cambiar_fichas(window)
                
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
                    
                    window.FindElement(event).Update(button_color=("black","green"))
                    
                    contador_clickeadas= ATRIL_JUGADOR.count("")
        
                if  contador_clickeadas == 0:
                    time.sleep(1)
                    turno_Act = 2
                    no_termina_turno= False
                    jugador_estante.estante.cambiar_fichas(window)
                    marcar_fichas=False
                    contador_clickeadas=-1
                    for i in range(7):
                    
                        window.FindElement(i).Update(button_color=("black", "white"))
                    
                        ATRIL_JUGADOR[i]=""
                        
                if event== "-confirmar_letras-":
                    time.sleep(1)
                    turno_Act = 2
                    no_termina_turno=False
                    marcar_fichas=False
                    jugador_estante.estante.cambiar_fichas(window,"marcadas")
                    for i in range(7):
                    
                        window.FindElement(i).Update(button_color=("black", "white"))
                    
                        ATRIL_JUGADOR[i]=""
                    window.FindElement("-confirmar_letras-").Update(disabled=True)
                    


            if (turno_Act == 1) and (no_termina_turno):
                # si es el turno del jugador y su turno aun no finaliza:
                if poder_guardar:
                    window.FindElement("Guardar").Update(visible=True)
                    poder_guardar = False

                if puede_cambiar_letras == 1:
                    window.FindElement("-cambiar_fichas-").Update(disabled=False)
                    window.FindElement("-cambiar_todas_fichas-").Update(disabled=False)
                
                
                
                if fichas_colocadas > 0:
                    # Si ya colocó una ficha aparece el boton para recuperarla
                    window.FindElement("-devolver_ficha-").Update(disabled=False)
                else:
                    window.FindElement("-devolver_ficha-").Update(disabled=True)

                if event in range(7) and puede_colocar==False:
                    # CLIKEA UNA FICHA:
                    
                    window.FindElement("-cambiar_fichas-").Update(disabled=True)
                    window.FindElement("-cambiar_todas_fichas-").Update(disabled=True)
                        
                    window.FindElement("-devolver_ficha-").Update(disabled=True)
                    window.FindElement("Guardar").Update(visible=False)
                    evento_ficha = event
                    ficha = str(estante[event])
                    ficha = ficha.split(
                        ","
                    )  # Tengo la ficha separada como (letra,valor)
                    jugador_estante.estante.quitar_Ficha_De_Estante(
                        evento_ficha, window
                    )
                    sigue = 1
                    puede_colocar = True
                    puede_cambias_letras=0
                if event == "-devolver_ficha-" and fichas_colocadas > 0:
                    puede_colocar = False
                    sigue = 0
                    jugador_estante.estante.retornar_Ficha_Al_Estante(
                        window, pos_fichas_estante[len(pos_fichas_estante) - 1]
                    )
                    pos = pos_ficha_anterior[len(pos_ficha_anterior) - 1]
                    if pos in POS_ESPECIALES[dificultad.replace("-", "")]["x2"]:
                        tablero.quitar_elemento(window, pos, "x2")
                    elif pos in POS_ESPECIALES[dificultad.replace("-", "")]["x2letra"]:
                        tablero.quitar_elemento(window, pos, "x2let")
                    elif pos in POS_ESPECIALES[dificultad.replace("-", "")]["x3"]:
                        tablero.quitar_elemento(window, pos, "x3")
                    elif pos in POS_ESPECIALES[dificultad.replace("-", "")]["x3letra"]:
                        tablero.quitar_elemento(window, pos, "x3let")
                    elif pos in POS_ESPECIALES[dificultad.replace("-", "")]["-2"]:
                        tablero.quitar_elemento(window, pos, "menos2")
                    elif pos in POS_ESPECIALES[dificultad.replace("-", "")]["-3"]:
                        tablero.quitar_elemento(window, pos, "menos3")
                    else:
                        tablero.quitar_elemento(window, pos)
                    tablero.tablero[pos[0]][pos[1]] = False
                    fichas_colocadas -= 1
                    ATRIL_JUGADOR[pos_fichas_estante[len(pos_fichas_estante) - 1]] = ""
                    pos_fichas_estante.pop()
                    pos_ficha_anterior.pop()
                    list(ficha_pos)[-1]
                    palabra_formada = palabra_formada[:-1]

                    window.finalize()

                # COLOCA LA FICHA EN EL TABLERO

                if sigue == 1:

                    if fichas_colocadas == 0 and palabras_en_tablero > 0:
                        # Si ya hay palabras formadas en el tablero y no coloqué fichas, desbloqueo todas las pos adyacentes a las palabras formadas
                        pos_adyacentes = tablero.Pos_Libres_Tablero()
                        for pos in pos_adyacentes:
                            tablero.desbloquear_Pos(window, pos[0], pos[1])

                    if fichas_colocadas == 1:
                        # Si ya colocó una ficha desbloqueo los lugares disponibles que esten adyacentes a la primera ficha colocada
                        pos_disponibles = hay_espacio(window, pos_ficha_anterior[0], tablero)
                        for pos in pos_disponibles:
                            tablero.desbloquear_Pos(window, pos[0], pos[1])

                    if fichas_colocadas > 1:
                        # Si ya colocó más de una ficha me fijo la direccion a la cual forma la palabra y controlo que no se le termine el tablero

                        if (
                            pos_ficha_anterior[0][0]
                            == pos_ficha_anterior[len(pos_ficha_anterior) - 1][0]
                        ):
                            # si en la lista de posiciones no cambió el primer valor (el valor de las filas) es porque la palabra se está formando de forma horizontal

                            if pos_ficha_anterior[0][1] < pos_ficha_anterior[
                                len(pos_ficha_anterior) - 1
                            ][1] and hay_espacio(
                                window,
                                pos_ficha_anterior[len(pos_ficha_anterior) - 1],
                                tablero,
                                "derecha",
                            ):
                                # si el valor de la columna de la primera letra colocada es menor al de la ultima letra colocada, la palabra se está formando hacia la derecha
                                tablero.desbloquear_Pos(
                                    window,
                                    pos_ficha_anterior[len(pos_ficha_anterior) - 1][0],
                                    pos_ficha_anterior[len(pos_ficha_anterior) - 1][1]
                                    + 1,
                                )

                            elif pos_ficha_anterior[0][1] > pos_ficha_anterior[
                                len(pos_ficha_anterior) - 1
                            ][1] and hay_espacio(
                                window,
                                pos_ficha_anterior[len(pos_ficha_anterior) - 1],
                                tablero,
                                "izquierda",
                            ):
                                # Si la columna de la ultima ficha colocada tiene un valor menor a la primera ficha colocada entonces la palabra se está formando hacia la izquierda
                                tablero.desbloquear_Pos(
                                    window,
                                    pos_ficha_anterior[0][0],
                                    pos_ficha_anterior[len(pos_ficha_anterior) - 1][1]
                                    - 1,
                                )

                            else:
                                # Si no tenia espacio a la izquierda o a la derecha entra a el else
                                sigue = 0
                                puede_colocar = False
                                sg.Popup("No hay más espacio en el tablero")
                                jugador_estante.estante.retornar_Ficha_Al_Estante(
                                    window, evento_ficha
                                )

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
                                # pregunto si se forma hacia abajo y si se puede formar
                                tablero.desbloquear_Pos(
                                    window,
                                    pos_ficha_anterior[len(pos_ficha_anterior) - 1][0]
                                    + 1,
                                    pos_ficha_anterior[len(pos_ficha_anterior) - 1][1],
                                )

                            elif pos_ficha_anterior[0][0] > pos_ficha_anterior[
                                len(pos_ficha_anterior) - 1
                            ][0] and hay_espacio(
                                window, pos_ficha_anterior[0], tablero, "arriba"
                            ):
                                # pregunto si se forma hacia arriba y si se puede formar
                                tablero.desbloquear_Pos(
                                    window,
                                    pos_ficha_anterior[len(pos_ficha_anterior) - 1][0]
                                    - 1,
                                    pos_ficha_anterior[0][1],
                                )

                            else:
                                # qué pasa si no se puede formar más la palabra
                                sigue = 0
                                puede_colocar = False
                                sg.Popup(
                                    "No hay más espacio en el tablero, confirme la"
                                    " palabra o intente formar otra"
                                )
                                jugador_estante.estante.retornar_Ficha_Al_Estante(
                                    window, evento_ficha
                                )

                    if (
                        puede_colocar
                        and not (event in range(7))
                        and isinstance(event, tuple)
                    ):
                        # si la variable puede colocar está en true, el evento no es el atril y el evento es una tupla, coloco la ficha
                        window.FindElement(event).Update(
                            text=ficha[0],
                            image_filename=(("imagenes/" + ficha[0] + ".png")),
                        )
                        tablero.bloquear_tablero(window)
                        ATRIL_JUGADOR[evento_ficha] = ficha[0]
                        # vuelvo a desbloquear el atril para que puedan seguir tomando fichas
                        jugador_estante.estante.desbloquear_pos_Estante(window)
                        # Me guardo las posiciones en las cuales colocó una ficha
                        pos_ficha_anterior.append(event)
                        # agrego la ficha junto a su posicion para luego ver si hay un multiplicador
                        ficha_pos.update({ficha[0]: event})
                        fichas_colocadas = fichas_colocadas + 1
                        sigue = 0
                        palabra_formada += ficha[0]
                        pos_fichas_estante.append(evento_ficha)
                        puede_colocar=False
                        puede_cambiar_letras=0
                        window.FindElement("-cambiar_fichas-").Update(disabled=True)
                        window.FindElement("-cambiar_todas_fichas-").Update(disabled=True)


                if fichas_colocadas == 2:
                    # Si ya colocó 2 fichas aparece el boton para confirmar palabra
                    window.FindElement("Confirmar Palabra").Update(disabled=False)

                if event == "Confirmar Palabra":

                    if confirmar_Palabra(palabra_formada, dificultad):
                        
                        no_agarro_letra=1
                        puede_cambiar_letras=1
                        
                        puntos_provisional = puntos.puntaje_palabra(
                            fichas_punt, palabra_formada, window
                        )
                        for pos in pos_ficha_anterior:
                            puntos_provisional = puntos.multipal(
                                pos[0],
                                pos[1],
                                dificultad,
                                puntos_provisional,
                                POS_ESPECIALES,
                                window,
                            )
                            tablero.tablero[pos[0]][pos[1]] = True
                        agregado = 0
                        for key in ficha_pos:
                            agregado = agregado + puntos.multilet(
                                ficha_pos[key],
                                key,
                                dificultad,
                                fichas_punt,
                                POS_ESPECIALES,
                                window,
                            )
                        puntos_provisional += agregado
                        jugador_estante.incrementar_puntaje(puntos_provisional, window)
                        poder_guardar = True
                        jugador_estante.estante.eliminar_fichas_estante()
                        jugador_estante.estante.agregar_fichas(fichas_colocadas, window)
                        sigue = 0
                        turno_Act = 2
                        palabras_en_tablero += 1
                        fichas_colocadas = 0
                        puede_colocar = False
                        no_termina_turno = False
                        window.FindElement("Confirmar Palabra").Update(disabled=True)
                        window.FindElement("-Turno-").Update(
                            value="Turno de la maquina"
                        )
                        for pos in range(len(ATRIL_JUGADOR)):
                            if ATRIL_JUGADOR[pos] != "":
                                ATRIL_JUGADOR[pos] = ""
                        pos_fichas_estante = []
                        palabra_formada = ""
                        # Vuelvo a desbloquear el estante para que siga jugando con las nuevas fichas
                        jugador_estante.estante.desbloquear_pos_Estante(window)
                    else:
                        
                        puede_cambiar_letras=1
                        no_agarro_letra=1
                        sg.Popup("No era una palabra")
                        puede_colocar = False
                        poder_guardar = True
                        window.FindElement("Confirmar Palabra").Update(disabled=True)
                        sigue = 0

                        for pos in pos_fichas_estante:
                            jugador_estante.estante.retornar_Ficha_Al_Estante(
                                window, pos
                            )
                            ATRIL_JUGADOR[pos] = ""
                        for pos in pos_ficha_anterior:
                            # Si la pos de las fichas utilizadas eran una casilla especial, vuelvo a colocar la imagen de la ficha especial en su lugar
                            if pos in POS_ESPECIALES[dificultad.replace("-", "")]["x2"]:
                                tablero.quitar_elemento(window, pos, "x2")
                            elif (
                                pos
                                in POS_ESPECIALES[dificultad.replace("-", "")][
                                    "x2letra"
                                ]
                            ):
                                tablero.quitar_elemento(window, pos, "x2let")
                            elif (
                                pos in POS_ESPECIALES[dificultad.replace("-", "")]["x3"]
                            ):
                                tablero.quitar_elemento(window, pos, "x3")
                            elif (
                                pos
                                in POS_ESPECIALES[dificultad.replace("-", "")][
                                    "x3letra"
                                ]
                            ):
                                tablero.quitar_elemento(window, pos, "x3let")
                            elif (
                                pos in POS_ESPECIALES[dificultad.replace("-", "")]["-2"]
                            ):
                                tablero.quitar_elemento(window, pos, "menos2")
                            elif (
                                pos in POS_ESPECIALES[dificultad.replace("-", "")]["-3"]
                            ):
                                tablero.quitar_elemento(window, pos, "menos3")
                            else:
                                tablero.quitar_elemento(window, pos)
                            tablero.tablero[pos[0]][pos[1]] = False

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
                        tiempo
                    )
                    guardar.main(datosg)
                
                if event == "Terminar":
                    sg.Popup("Se acabó la partida")
                    nombre=sg.popup_get_text("Ingresa tu nombre:")
                    jugador_estante.set_nombre(nombre)
                    sg.Popup("Nombre:",jugador_estante.nombre,"Puntuacion:", jugador_estante.puntaje)
                    try:
                        with open("guardado/top10.json", "r") as jsonFile:
                            top10 = json.load(jsonFile)
                    except Exception:
                        with open("guardado/top10vacio.json", "r") as jsonFile:
                            top10 = json.load(jsonFile)
                    minimo = 9999
                    minimon = 1
                    for a in range(9):
                        if int(top10[list(top10.keys())[a]]) < int(minimo):
                            minimo = top10[list(top10.keys())[a]]
                            minimon = a
                    top10[jugador_estante.nombre] = top10.pop(list(top10.keys())[minimon])
                    top10[jugador_estante.nombre] = jugador_estante.puntaje
                    top10s = sorted(top10.items(), key=lambda kv: kv[1])
                    top10s.reverse()
                    top10or = collections.OrderedDict(top10s)
                    config.guardar("guardado/top10.json",top10or)
                    break

            elif turno_Act == 2:
                sg.Popup(
                    "Ahora le toca a la maquina, clickea un boton del atril para"
                    " continuar"
                )
                time.sleep(1)
                turno_Act = 1
                no_termina_turno = True
                sigue = 1
                pos_ficha_anterior = []
                window.FindElement("-Turno-").Update(value="Turno de el jugador")
    window.Close()
