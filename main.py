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


class Estante:
    """
    Clase que crea el estante del jugador. Agrega fichas del atril al estante.
    """
    def __init__(self, atril):
        #Inicializa el estante del jugador.
        self.estante = []
        self.atril = atril
        self.inicializar()

    def agregar_estante(self):
        #Agrega una ficha al estante quitando esa misma del atril
        self.estante.append(self.atril.quitar_ficha())

    def inicializar(self):
        #Añade las primeras 7 fichas al estante
        for i in range(7):
            self.agregar_estante()

    def quitar_estante(self, ficha):
        #Quita una ficha del estante
        self.estante.remove(ficha)

    def cant_estante(self):
        #Devuelve la cantidad de fichas que hay en el estante
        return len(self.estante)

    def get_estante(self):
        #Devuelve un arreglo con los elementos del estante, para poder representarlo en pysimplegui
        return self.estante

class Jugador:
    """
    Clase que crea una instancia de Jugador. Crea su estante y agrega su nombre.
    """
    def __init__(self, atril):
        #Inicializa un Jugador con su estante.
        self.nombre = ""
        self.puntaje = 0
        self.estante = Estante(atril)

    def incrementar_puntaje(self, agregado):
        #Incrementa el puntaje del jugador
        self.puntaje += agregado

    def get_puntaje(self):
        #Devuelve el puntaje del jugador
        return self.puntaje

    def set_nombre(self, nombre):
        #Setea el nombre del jugador
        self.nombre = nombre

    def get_nombre(self):
        #Devuelve el nombre del jugador
        return self.nombre

    def get_estante(self):
        #Devuelve un arreglo con los elementos del estante, para poder representarlo en pysimplegui
        return self.estante.get_estante()

def estante_ps(estante):
    i=0
    for x in estante:
        print(estante[i].get_letra())
        window.FindElement(i).Update(estante[i].get_letra())
        i=i+1

atril = Atril()
j1 = Jugador(atril)

layout2 =  [[sg.Button('', button_color=("black","#F8F8F8"), key=(i,j), size=(1,1), pad=(0,0)) for j in range(15)]  for i in range(15)]
layout2.append([sg.Text('Estante')])
layout2.append([sg.Button('', button_color=("black","#F8F8F8"), key=(a), size=(1,1), pad=(0,0)) for a in range(7)])
layout2.append([sg.Button('Jugar'), sg.Button('Salir')])
window = sg.Window('ScrabbleAr').Layout(layout2)

while True:
    event, values = window.Read()
    if event is None or event == 'Salir':
        break
    if event is 'Jugar':
        #Imprimo el estante en la pantalla
        window.FindElement((1,1)).Update('x')
        arregloEstante = j1.get_estante()
        estante_ps(arregloEstante)
window.Close()
