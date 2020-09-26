from random import shuffle
import puntos
import PySimpleGUI as sg
from ClaseFicha import Ficha

class Atril:


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
        for _ in range(int(cantidad)):
            self.atril.append(letra)

    def inicializa_atril(self, fichas_cant, fichas_punt):
        # agrega las fichas al atril y las mezcla (shuffle)
        for x in puntos.keys:
            self.agregar(
                Ficha(str(x), fichas_punt[str(x)]), fichas_cant[str(x)])
        shuffle(self.atril)

    def quitar_ficha(self):
        """
            Quita una ficha del atril y la retorna.
            En caso de que no queden fichas, retorna None
        """
        if self.atril == []:
            sg.Popup("Se acabaron las fichas")
            return None
        else:
            return self.atril.pop()

    def cant_letras(self):
        # Devuelve la cantidad de letras que quedan en el atril
        return len(self.atril)
