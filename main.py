'''Trabajo Final'''
import PySimpleGUI as sg
from random import shuffle

#Variable global con los valores - temporal
valores = {"A": 1,"B": 3,"C": 2,"D": 2,"E": 1,"F": 4,"G": 2,"H": 4,
            "I": 1,"J": 6,"K": 8,"L": 1,"LL": 8,"M": 3,"N": 1,"Ñ": 8,
            "O": 1,"P": 3,"Q": 8,"R": 1,"RR": 8,"S": 1,"T": 1,"U": 1,
            "V": 4,"W": 8,"X": 8,"Y": 4,"Z": 10}

class Ficha:
    """
    Clase que crea una ficha. La inicializa con la letra y su valor
    """
    def __init__(self, letra, valores):
        #Inicializa una ficha, con la letra (string) y el diccionario con los valores
        self.letra = letra.upper()
        self.valor = valores[self.letra]

    def get_valor(self):
        #Devuelve el valor de la ficha
        return self.valor

    def get_letra(self):
        #Devuelve la letra de la ficha.
        return self.letra


class Atril:
    """
    Clase que crea el atril con 100 fichas por defecto
    """
    def __init__(self):
        #Crea el atril y lo inicializa con 100 fichas por defecto
        self.atril = []
        self.inicializa_atril()

    def agregar(self, letra, cantidad):
        #agrega una letra, la cantidad de veces que se indique, al atril
        for a in range(cantidad):
            self.atril.append(letra)

    def inicializa_atril(self):
        #agrega las 100 fichas al atril y las mezcla (shuffle)
        self.agregar(Ficha("A", valores), 11)
        self.agregar(Ficha("B", valores), 3)
        self.agregar(Ficha("C", valores), 4)
        self.agregar(Ficha("D", valores), 4)
        self.agregar(Ficha("E", valores), 11)
        self.agregar(Ficha("F", valores), 2)
        self.agregar(Ficha("G", valores), 2)
        self.agregar(Ficha("H", valores), 2)
        self.agregar(Ficha("I", valores), 6)
        self.agregar(Ficha("J", valores), 2)
        self.agregar(Ficha("K", valores), 1)
        self.agregar(Ficha("L", valores), 4)
        self.agregar(Ficha("LL", valores), 1)
        self.agregar(Ficha("M", valores), 3)
        self.agregar(Ficha("N", valores), 5)
        self.agregar(Ficha("Ñ", valores), 1)
        self.agregar(Ficha("O", valores), 8)
        self.agregar(Ficha("P", valores), 2)
        self.agregar(Ficha("Q", valores), 1)
        self.agregar(Ficha("R", valores), 4)
        self.agregar(Ficha("RR", valores), 1)
        self.agregar(Ficha("S", valores), 7)
        self.agregar(Ficha("T", valores), 4)
        self.agregar(Ficha("U", valores), 6)
        self.agregar(Ficha("V", valores), 2)
        self.agregar(Ficha("W", valores), 1)
        self.agregar(Ficha("X", valores), 1)
        self.agregar(Ficha("Y", valores), 1)
        self.agregar(Ficha("Z", valores), 1)
        shuffle(self.atril)

    def quitar_ficha(self):
        #Quita una letra del atril y se la da al usuario
        return self.atril.pop()

    def cant_letras(self):
        #Devuelve la cantidad de letras que quedan en el atril
        return len(self.atril)


#Las columnas eran una prueba, al final las deje ahi porq si puedo acceder a sus keys, el problema es que entre columnas hay un gran espacio en blanco :c
columna_1 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='0,14', size=(1,1))],
]

columna_2 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='1,14', size=(1,1))],
]

columna_3 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='2,14', size=(1,1))],
]

columna_4 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='3,14', size=(1,1))],
]

columna_5 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='4,14', size=(1,1))],
]

columna_6 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='5,14', size=(1,1))],
]

columna_7 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='6,14', size=(1,1))],
]

columna_8 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='7,14', size=(1,1))],
]

columna_9 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='8,14', size=(1,1))],
]

columna_10 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='9,14', size=(1,1))],
]

columna_11 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='10,14', size=(1,1))],
]

columna_12 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='11,14', size=(1,1))]
]

columna_13 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='12,14', size=(1,1))]
]

columna_14 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='13,14', size=(1,1))]
]

columna_15 = [
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,0', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,1', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,2', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,3', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,4', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,5', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,6', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,7', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,8', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,9', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,10', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,11', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,12', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,13', size=(1,1))],
    [sg.Button('', button_color=("black","#F8F8F8"), key='14,14', size=(1,1))]
]

#No se puede poner los botones como en layout2 de esta manera, hay que usar el append como hice en el layout2, o no se como hacerlo

layout1 = [
    [sg.Text('ScrabbleAr Grupo 27', justification='left')],
    [sg.Column(columna_1)],
    [sg.Button('Jugar'), sg.Button('Salir')]
]
#Se me trabo la cabeza con acceder a las keys de los botones
a = b = 15
layout2 =  [[sg.Button('a', button_color=("black","#F8F8F8"), key=(int(i),int(j)), size=(1,1), pad=(0,0)) for j in range(a)]  for i in range(b)]

layout2.append([sg.Button('Jugar'), sg.Button('Salir')])
#layout2.append([sg.Column(columna_1)])
window = sg.Window('ScrabbleAr').Layout(layout2)
#el print es solo porq estaba probando
print(window.Element('10,10'))

while True:
    event, values = window.Read()
    if event is None or event == 'Salir':
        break
    if event is 'Jugar':
        window.Element('12,12').Update('x')
window.Close()
