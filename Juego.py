'''Trabajo Final'''
import PySimpleGUI as sg
from random import shuffle

ATRIL_JUGADOR=[[""] for i in range(7)]

#Variable global con los valores - temporal
valores = {"A": 1,"B": 3,"C": 2,"D": 2,"E": 1,"F": 4,"G": 2,"H": 4,
            "I": 1,"J": 6,"K": 8,"L": 1,"LL": 8,"M": 3,"N": 1,"Ñ": 8,
            "O": 1,"P": 3,"Q": 8,"R": 1,"RR": 8,"S": 1,"T": 1,"U": 1,
            "V": 4,"W": 8,"X": 8,"Y": 4,"Z": 10}

class Ficha:
    """
    Clase que crea una ficha. La inicializa con la letra y su valor
    """
    def __init__(self, letra):
        #Inicializa una ficha, con la letra (string) y el diccionario con los valores
        self.letra = letra.upper()
        self.valor = valores[self.letra]

    def get_valor(self):
        #Devuelve el valor de la ficha
        return self.valor

    def get_letra(self):
        #Devuelve la letra de la ficha.
        return self.letra
    def __repr__(self):
        return self.letra +"," +str(self.valor)    
    def __str__(self):
        aux= self.letra +"," +str(self.valor)
        return aux


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
        self.agregar(Ficha("A"), 11)
        self.agregar(Ficha("B"), 3)
        self.agregar(Ficha("C"), 4)
        self.agregar(Ficha("D"), 4)
        self.agregar(Ficha("E"), 11)
        self.agregar(Ficha("F"), 2)
        self.agregar(Ficha("G"), 2)
        self.agregar(Ficha("H" ), 2)
        self.agregar(Ficha("I" ), 6)
        self.agregar(Ficha("J" ), 2)
        self.agregar(Ficha("K" ), 1)
        self.agregar(Ficha("L" ), 4)
        self.agregar(Ficha("LL" ), 1)
        self.agregar(Ficha("M" ), 3)
        self.agregar(Ficha("N" ), 5)
        self.agregar(Ficha("Ñ" ), 1)
        self.agregar(Ficha("O" ), 8)
        self.agregar(Ficha("P" ), 2)
        self.agregar(Ficha("Q" ), 1)
        self.agregar(Ficha("R" ), 4)
        self.agregar(Ficha("RR" ), 1)
        self.agregar(Ficha("S" ), 7)
        self.agregar(Ficha("T" ), 4)
        self.agregar(Ficha("U" ), 6)
        self.agregar(Ficha("V" ), 2)
        self.agregar(Ficha("W" ), 1)
        self.agregar(Ficha("X" ), 1)
        self.agregar(Ficha("Y" ), 1)
        self.agregar(Ficha("Z" ), 1)
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
        
    def bloquear_Estante():
        for i in range(7):
            window.FindElement(i).Update(disabled=True)	
    def desbloquear_Estante():
        for i in range(7):
            window.FindElement(i).Update(disabled=False)
       
    def modificar_Estante(self,bot):
        ATRIL_JUGADOR[bot]=window.FindElement(bot).get_text()
        self.bloquear_Estante()
        window.FindElement(bot).Update(text="",button_color=("black", "orange"), visible=False)

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
        print('aaaaaaaaaaaaaaaaaaaa')
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

class Tablero:
	'''
		Clase que representa al tablero para poder modificarlo
	'''
	def __init__(self):
		self.tablero= [[False for j in range(15)]for i in range(15)]
	
	def mostrar_estado(self):
		aux=''
		for m in range(15):
			for n in range(15):
				aux+="|" + (str(self.tablero[m][n])) + "|"
			aux+='\n'
		print(aux)
		
	def agregar_elemento( self,element,*pos):
		self.tablero[pos[0]][pos[1]]= True
		window.FindElement((pos[0],pos[1])).Update(text=element)




atril = Atril()
j1 = Jugador(atril)
tablero= Tablero()


sigue=0
juega= False
ficha_clickeada=-1

layout2 =  [[sg.Button('', button_color=("black","#F8F8F8"), key=(i,j), size=(4,2), pad=(2,2)) for j in range(15)]  for i in range(15)]
layout2.append([sg.Text('Estante',	font=('arial',15)) ])
layout2.append([sg.Button('', button_color=("black","#F8F8F8"), key=(a), size=(4,2), pad=(2,2)) for a in range(7)])
layout2.append([sg.Button('Jugar',size=(8,2)), sg.Button('Salir',size=(8,2))])
window = sg.Window('ScrabbleAr', size=(850,800),element_justification='c').Layout(layout2)


def main():
    
    while True:
        event, values = window.Read()
        if event is None or event == 'Salir':
            break
        if event is 'Jugar':
            arregloEstante = j1.get_estante()
            estante_ps(arregloEstante)
            juega= True
        elif event in range(7) and juega:
            ficha_clickeada = event	
            estante= j1.get_estante()
            ficha=str(estante[event])
            ficha=ficha.split(",")
            Estante.modificar_Estante(Estante,ficha_clickeada)
            sigue=1
        elif (sigue==1):
            tablero.agregar_elemento(ficha[0],event[0],event[1])
            Estante.desbloquear_Estante()
            sigue=0
	    
	    
    window.Close()
