'''Trabajo Final'''
import PySimpleGUI as sg
from random import shuffle
import json
import random
import datetime, time
import os

#constante que representa el atril del jugador
ATRIL_JUGADOR=[[""] for i in range(7)]

TIEMPO_LIMITE_PARTIDA = datetime.datetime.now() + datetime.timedelta(seconds=60)

#Variable global con los valores - temporal
valores = {"A": 1,"B": 3,"C": 2,"D": 2,"E": 1,"F": 4,"G": 2,"H": 4,
            "I": 1,"J": 6,"K": 8,"L": 1,"LL": 8,"M": 3,"N": 1,"Ñ": 8,
            "O": 1,"P": 3,"Q": 8,"R": 1,"RR": 8,"S": 1,"T": 1,"U": 1,
            "V": 4,"W": 8,"X": 8,"Y": 4,"Z": 10}


def cargar():
    try:
        with open('datos.json', 'r') as jsonFile:
            datos = json.load(jsonFile)
        return datos
    except FileNotFoundError:
        sg.popup("No se encontró el archivo de configuracion, se procedera a crear uno...")
        with open('datos_default.json', 'r') as jsonFile:
            datos = json.load(jsonFile)
        return datos

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
    def __init__(self, fichas_cant):
        #Crea el atril y lo inicializa con 100 fichas por defecto
        self.atril = []
        self.inicializa_atril(fichas_cant)

    def agregar(self, letra, cantidad):
        #agrega una letra, la cantidad de veces que se indique, al atril
        for a in range(cantidad):
            self.atril.append(letra)
    def inicializa_atril(self, fichas_cant):
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
        self.agregar(Ficha("LL"), 1)
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
        
    def bloquear_Estante(self, window):
        for i in range(7):
            window.FindElement(i).Update(disabled=True)
    def desbloquear_Estante(self, window):
        for i in range(7):
            window.FindElement(i).Update(disabled=False)
       
    def quitar_Ficha_De_Estante(self, bot, window):
        ATRIL_JUGADOR[bot]=window.FindElement(bot).get_text()
        self.bloquear_Estante(self, window)
        window.FindElement(bot).Update(text="",button_color=("black", "orange"), visible=False)
    def retornar_Ficha_Al_Estante(self,pos,ficha,window):
        window.FindElement(pos).Update(text=ficha,button_color=("black","white"), visible=True)

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
   
    def agregar_elemento( self,element, window, *pos):
        self.tablero[pos[0]][pos[1]]= True
        window.FindElement((pos[0],pos[1])).Update(text=element)
        
    def bloquear_tablero(self, window):
        for m in range(15):
            for n in range(15):
                window.FindElement((m,n)).Update(disabled=True, button_color=("black","white"))
    def desbloquear_tablero(self, window):
        for m in range(15):
            for n in range(15):
                window.FindElement((m,n)).Update(disabled=False, button_color=("black","green"))

    def desbloquear_Pos(self,window,x,y):
        window.FindElement((x,y)).Update(disabled=False, button_color=("black","green"))

    def bloquear_Pos(self,window,x,y):
        window.FindElement((x,y)).Update(disabled= True,button_color=("black","white"))


def estante_ps(estante, window):
    i=0
    for x in estante:
       # print(estante[i].get_letra())
        window.FindElement(i).Update(estante[i].get_letra())
        i=i+1


def datos(dificultad):
    if dificultad == "-facil-":
        valores = cargar()
        keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "LL", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "RR",]
        keysp = ["fpuntosa", "fpuntosb", "fpuntosc", "fpuntosd", "fpuntose", "fpuntosf", "fpuntosg", "fpuntosh", "fpuntosi", "fpuntosj", "fpuntosk", "fpuntosl", "fpuntosll", "fpuntosm", "fpuntosn", "fpuntos\u00f1", "fpuntoso", "fpuntosp", "fpuntosq", "fpuntosr", "fpuntoss", "fpuntost", "fpuntosu", "fpuntosv", "fpuntosw", "fpuntosx", "fpuntosy", "fpuntosz", "fpuntosrr"]
        keysc = ["fcantidada", "fcantidadb", "fcantidadc", "fcantidadd", "fcantidade", "fcantidadf", "fcantidadg", "fcantidadh", "fcantidadi", "fcantidadj", "fcantidadk", "fcantidadl", "fcantidadll", "fcantidadm", "fcantidadn", "fcantidad\u00f1", "fcantidado", "fcantidadp", "fcantidadq", "fcantidadr", "fcantidads", "fcantidadt", "fcantidadu", "fcantidadv", "fcantidadw", "fcantidadx", "fcantidady", "fcantidadz", "fcantidadrr"]
        fichas_cant = {y:valores[x] for x,y in zip(keysc, keys)}
        fichas_punt = {y:valores[x] for x,y in zip(keysp, keys)}
        return fichas_cant, fichas_punt
    elif dificultad == "-medio-":
        valores = cargar()
        keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "LL", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "RR",]
        keysp = ["mpuntosa", "mpuntosb", "mpuntosc", "mpuntosd", "mpuntose", "mpuntosf", "mpuntosg", "mpuntosh", "mpuntosi", "mpuntosj", "mpuntosk", "mpuntosl", "mpuntosll", "mpuntosm", "mpuntosn", "mpuntos\u00f1", "mpuntoso", "mpuntosp", "mpuntosq", "mpuntosr", "mpuntoss", "mpuntost", "mpuntosu", "mpuntosv", "mpuntosw", "mpuntosx", "mpuntosy", "mpuntosz", "mpuntosrr"]
        keysc = ["mcantidada", "mcantidadb", "mcantidadc", "mcantidadd", "mcantidade", "mcantidadf", "mcantidadg", "mcantidadh", "mcantidadi", "mcantidadj", "mcantidadk", "mcantidadl", "mcantidadll", "mcantidadm", "mcantidadn", "mcantidad\u00f1", "mcantidado", "mcantidadp", "mcantidadq", "mcantidadr", "mcantidads", "mcantidadt", "mcantidadu", "mcantidadv", "mcantidadw", "mcantidadx", "mcantidady", "mcantidadz", "mcantidadrr"]
        fichas_cant = {y:valores[x] for x,y in zip(keysc, keys)}
        fichas_punt = {y:valores[x] for x,y in zip(keysp, keys)}
        return fichas_cant, fichas_punt
    elif dificultad == "-dificil-":
        valores = cargar()
        keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "LL", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "RR",]
        keysp = ["dpuntosa", "dpuntosb", "dpuntosc", "dpuntosd", "dpuntose", "dpuntosf", "dpuntosg", "dpuntosh", "dpuntosi", "dpuntosj", "dpuntosk", "dpuntosl", "dpuntosll", "dpuntosm", "dpuntosn", "dpuntos\u00f1", "dpuntoso", "dpuntosp", "dpuntosq", "dpuntosr", "dpuntoss", "dpuntost", "dpuntosu", "dpuntosv", "dpuntosw", "dpuntosx", "dpuntosy", "dpuntosz", "dpuntosrr"]
        keysc = ["dcantidada", "dcantidadb", "dcantidadc", "dcantidadd", "dcantidade", "dcantidadf", "dcantidadg", "dcantidadh", "dcantidadi", "dcantidadj", "dcantidadk", "dcantidadl", "dcantidadll", "dcantidadm", "dcantidadn", "dcantidad\u00f1", "dcantidado", "dcantidadp", "dcantidadq", "dcantidadr", "dcantidads", "dcantidadt", "dcantidadu", "dcantidadv", "dcantidadw", "dcantidadx", "dcantidady", "dcantidadz", "dcantidadrr"]
        fichas_cant = {y:valores[x] for x,y in zip(keysc, keys)}
        fichas_punt = {y:valores[x] for x,y in zip(keysp, keys)}
        return fichas_cant, fichas_punt

def salir_juego(evento):
    if evento is None or evento == 'Salir':
        return True

def hay_espacio(window,lista_pos, direc="disponibles"): #Funcion que retorna si es válido o no colocar una ficha en la posición de la direccion asignada. En caso de no dar una direccion retorna una lista con todas las posiciones válidas que rodeen a la ultima ficha colocada.
    if direc== "disponibles":
        aux=[]
        if lista_pos[0] != 0:
            if window.FindElement((lista_pos[0]-1,lista_pos[1])).GetText() == "":
                aux.append([lista_pos[0]-1,lista_pos[1]])
        if lista_pos[0] != 15:    
            if window.FindElement((lista_pos[0]+1,lista_pos[1])).GetText() == "":
                aux.append([lista_pos[0]+1,lista_pos[1]])
        if lista_pos[1] != 0:
            if window.FindElement((lista_pos[0],lista_pos[1]-1)).GetText() == "":
                aux.append([lista_pos[0], lista_pos[1]-1])
        if lista_pos[1] != 15:
            if window.FindElement((lista_pos[0],lista_pos[1]+1)).GetText() == "":
                aux.append([lista_pos[0],lista_pos[1]+1])
        return aux
    elif direc== "derecha":
        if lista_pos[1] != 15:
            if window.FindElement((lista_pos[0],lista_pos[1]+1)).GetText() != "":
                return False
            return True
        else:
            return False
    elif direc=="izquierda":
        if lista_pos[1] !=0:
            if (window.FindElement((lista_pos[0],lista_pos[1]-1)).GetText() != ""):
                return False
            return True
        else:
            return False
    elif direc=="arriba":
        if lista_pos[0] !=0:
            if (window.FindElement((lista_pos[0]-1,lista_pos[1])).GetText() !=""):
                return False
            return True
        else:
            return False
    elif direc=="abajo":
        if lista_pos[0] !=15:
            if(window.FindElement((lista_pos[0]+1,lista_pos[1])).GetText() !=""):
                return False
            return True
        else:
            return False
            
            

def so():
    a = os.name
    if os.name == "nt":
        WIDTH  = 4
        HEIGHT = 2
        SW = 850
        SH = 800
        return WIDTH, HEIGHT, SW, SH
    elif os.name == "posix":
        WIDTH  = 1
        HEIGHT = 1
        SW = 650
        SH = 600
        return WIDTH, HEIGHT, SW, SH


def main(dificultad):
    
    w,h,sw,sh = so()
    fichas_cant, fichas_punt = datos(dificultad)
    atril = Atril(fichas_cant)
    jugador_estante = Jugador(atril)
    tablero= Tablero()
    
    sigue=0
    juega= False
    
    turno_opciones=["jugador","maquina"]
 #  turno_Act= random.choice(turno_opciones) #Genero de forma aleatoria quien inicia a jugar
    turno_Act="jugador"
    tomo_ficha= False
    puede_colocar= False
    no_termina_turno= True
    pos_ficha_anterior=[]
    fichas_colocadas= 0
    
    
    
    
    
    
    layout2 =  [[sg.Button('', button_color=("black","#F8F8F8"), key=(i,j), size=(w,h), pad=(2,2)) for j in range(15)]  for i in range(15)]
    layout2.append([sg.Text('Estante',	font=('arial',15)) ])
    layout2.append([sg.Button('', button_color=("black","#F8F8F8"), key=(a), size=(w,h), pad=(2,2)) for a in range(7)])
    layout2.append([sg.Button('Jugar',size=(8,2)), sg.Button('Salir',size=(8,h))])
    
    window = sg.Window('ScrabbleAr', size=(sw,sh),element_justification='c').Layout(layout2)
    
    while True:
        event, values = window.Read()
        if(salir_juego(event)): #si toco salir o clikeo la x finaliza el while True
            break
        if event == 'Jugar':                                  #Si toca jugar carga el estante del jugador con las fichas aleatorias, bloquea el tablero y guarda en una variable que ya inicio el juego
            arregloEstante = jugador_estante.get_estante()
            estante_ps(arregloEstante, window)
            tablero.bloquear_tablero(window)
            juega= True
        elif juega:											#Si ya se tocó el boton de jugar inicia a preguntar por los turnos y preparar el tablero para las jugadas
            palabras_en_tablero = 0

            if (palabras_en_tablero==0):  #si no hay palabras en el tablero solo desbloqueo el centro para que se inicie a jugar
               tablero.desbloquear_Pos(window,7,7)

           #TURNO JUGADOR
           
            if (no_termina_turno== False):
                fichas_colocadas= 0
           


            if (turno_Act == "jugador") and (no_termina_turno):   #si es el turno del jugador y su turno aun no finaliza...
                
                
                
            #CLIKEA EL ATRIL
                
                if event in range(7):
                    evento_ficha=event
                    estante= jugador_estante.get_estante()
                    ficha= str(estante[event])
                    ficha= ficha.split(",") #Tengo la ficha separada como (letra,valor)
                    Estante.quitar_Ficha_De_Estante(Estante,evento_ficha, window)
                    sigue = 1
                    puede_colocar= True
           
           #COLOCA EN TABLERO
           
                if (sigue==1):
                    if fichas_colocadas == 1 : #Si ya coloqué una ficha y no habian palabras en el tablero desbloqueo hacia los 4 lados, dado que hay espacio
                        pos_disponibles= hay_espacio(window,pos_ficha_anterior[0])
                        for pos in pos_disponibles:
                            tablero.desbloquear_Pos(window,pos[0],pos[1])
                    
                    if fichas_colocadas > 1:
                        
                        if pos_ficha_anterior[0][0] == pos_ficha_anterior[1][0]:#si en la lista de posiciones, no cambió el primer valor es porque la palabra se está formando de forma horizontal
                            if(pos_ficha_anterior[0][1] < pos_ficha_anterior[1][1] and hay_espacio(window,pos_ficha_anterior[1],"derecha")): #si el valor de la columna de la primera letra es menor al de la segunda, la palabra va hacia la derecha
                                tablero.desbloquear_Pos(window,pos_ficha_anterior[0][0],pos_ficha_anterior[1][1]+1)
                            elif pos_ficha_anterior[0][1] > pos_ficha_anterior[1][1] and hay_espacio(window,pos_ficha_anterior[0],"izquierda"):
                                tablero.desbloquear_Pos(window, pos_ficha_anterior[0][0],pos_ficha_anterior[0][1]-1)
                            else: #Si entra al else es porque no habia espacio para la izq o la derecha, por lo tanto tiene que tocar el boton de confirmar palabra
                                sigue=0
                                puede_colocar=False
                                Estante.retornar_Ficha_Al_Estante(Estante,evento_ficha,ficha[0],window)
                        elif pos_ficha_anterior[0][1] == pos_ficha_anterior[1][1]:
                            if pos_ficha_anterior[0][0] < pos_ficha_anterior[1][0] and hay_espacio(window,pos_ficha_anterior[1],"abajo"):          
                                tablero.desbloquear_Pos(window, pos_ficha_anterior[1][0]+1,pos_ficha_anterior[1][1])            
                            elif pos_ficha_anterior[0][0] > pos_ficha_anterior[1][0] and hay_espacio(window,pos_ficha_anterior[0],"arriba"):            
                                tablero.desbloquear_Pos(window,pos_ficha_anterior[0][0]-1,pos_ficha_anterior[0][1])        
                            else:           
                                sigue=0
                                puede_colocar=False
                                Estante.retornar_Ficha_Al_Estante(Estante, evento_ficha, ficha[0], window)
                   
                   
                    if puede_colocar and not( event in range(7)): 
                        window.FindElement(event).Update(text=ficha[0])
                        tablero.bloquear_tablero(window)
                        fichas_colocadas=fichas_colocadas + 1
                        pos_ficha_anterior.append(event)
                        print(pos_ficha_anterior)
                        Estante.desbloquear_Estante(Estante,window)  
                        sigue=0  


    window.Close()
