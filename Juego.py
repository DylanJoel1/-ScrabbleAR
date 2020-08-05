'''Trabajo Final'''
import PySimpleGUI as sg
from random import shuffle
import json
import random
import datetime, time
import os
import puntos
from funcionAutenticar import confirmar_Palabra

#constante que representa el atril del jugador
ATRIL_JUGADOR=[[""] for i in range(7)]

TIEMPO_LIMITE_PARTIDA = datetime.datetime.now() + datetime.timedelta(seconds=60)

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
    def __init__(self, letra, fichas_punt):
        #Inicializa una ficha, con la letra (string) y el diccionario con los valores
        self.letra = letra.upper()
        self.valor = fichas_punt

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
    def __init__(self, fichas_cant, fichas_punt):
        #Crea el atril y lo inicializa con 100 fichas por defecto
        self.atril = []
        self.inicializa_atril(fichas_cant, fichas_punt)

    def agregar(self, letra, cantidad):
        #agrega una letra, la cantidad de veces que se indique, al atril
        for a in range(int(cantidad)):
            self.atril.append(letra)
    def inicializa_atril(self, fichas_cant, fichas_punt):
        #agrega las 100 fichas al atril y las mezcla (shuffle)
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
        #Imprime lo que contiene la variable que representa el tablero
        aux=''
        for m in range(15):
            for n in range(15):
                aux+="|" + (str(self.tablero[m][n])) + "|"
            aux+='\n'
        print(aux)
   
    def agregar_elemento( self,element, window, *pos):
        #Actualiza un boton del tablero con el texto que se le envíe 
        self.tablero[pos[0]][pos[1]]= True
        window.FindElement((pos[0],pos[1])).Update(text=element)
        
    def bloquear_tablero(self, window):
        #Bloquea todas las pos del tablero
        for m in range(15):
            for n in range(15):
                window.FindElement((m,n)).Update(disabled=True,button_color=("black","white") ,disabled_button_color=("black","white"))
    def desbloquear_tablero(self, window):
        #Desbloquea todas las pos del tablero
        for m in range(15):
            for n in range(15):
                window.FindElement((m,n)).Update(disabled=False, button_color=("black","green"))

    def desbloquear_Pos(self,window,x,y):
        #Desbloquea una pos en particular del tablero
        window.FindElement((x,y)).Update(disabled=False, button_color=("black","green"))

    def bloquear_Pos(self,window,x,y):
        #Bloquea una pos en particular del tablero
        window.FindElement((x,y)).Update(disabled= True,button_color=("black","white"),disabled_button_color=("black","white"))


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
    try:
        if os.name == "nt":
            WIDTH  = 4
            HEIGHT = 2
            SW = 850
            SH = 850
            return WIDTH, HEIGHT, SW, SH
        elif os.name == "posix":
            WIDTH  = 1
            HEIGHT = 1
            SW = 650
            SH = 600
            return WIDTH, HEIGHT, SW, SH
    except Exception:
        WIDTH  = 4
        HEIGHT = 2
        SW = 850
        SH = 850
        return WIDTH, HEIGHT, SW, SH

def main(dificultad):
    
    w,h,sw,sh = so()
    fichas_cant, fichas_punt = datos(dificultad)
    atril = Atril(fichas_cant,fichas_punt)
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
    palabra_formada=''
    
    
    
    
    
    layout2 =  [[sg.B   ('', button_color=("black","#F8F8F8"), key=(i,j), size=(w,h), pad=(2,2)) for j in range(15)]  for i in range(15)]
    layout2.append([sg.T('Estante',	font=('arial',15)) ])
    layout2.append([sg.B('', button_color=("black","#F8F8F8"), key=(a), size=(w,h), pad=(2,2)) for a in range(7)])
    layout2.append([sg.B('Confirmar Palabra', visible=False,size=(14,2),button_color=("black","green"))])
    layout2.append([sg.B('Jugar',size=(8,2)), sg.Button('Salir',size=(8,h))])
    
    window = sg.Window('ScrabbleAr', size=(sw,sh),element_justification='c').Layout(layout2)
    
    while True:
        event, values = window.Read()
        if(salir_juego(event)):
            break
        if event == 'Jugar':                                  
            #Si toca jugar carga el estante del jugador con las fichas aleatorias, bloquea el tablero y guarda en una variable que ya inicio el juego
            arregloEstante = jugador_estante.get_estante()
            estante_ps(arregloEstante, window)
            tablero.bloquear_tablero(window)
            window.FindElement('Jugar').Update(visible=False)
            juega= True
        elif juega:
            #Si ya se tocó el boton de jugar inicia a preguntar por los turnos y preparar el tablero para las jugadas
            
            palabras_en_tablero = 0

            if (palabras_en_tablero==0 and fichas_colocadas==0 ):  
               #si no hay palabras en el tablero y tampoco hay fichas colocadas solo desbloqueo el centro del tablero
               tablero.desbloquear_Pos(window,7,7)
            if (no_termina_turno== False):
                fichas_colocadas= 0
           #TURNO JUGADOR
           

            if (turno_Act == "jugador") and (no_termina_turno):   #si es el turno del jugador y su turno aun no finaliza...
                
                
                
            #CLIKEA UNA FICHA
                
                if event in range(7):
                    evento_ficha=event
                    estante= jugador_estante.get_estante()
                    ficha= str(estante[event])
                    ficha= ficha.split(",") #Tengo la ficha separada como (letra,valor)
                    Estante.quitar_Ficha_De_Estante(Estante,evento_ficha, window)
                    sigue = 1
                    puede_colocar= True
           
           #COLOCA LA FICHA EN EL TABLERO
           
                if (sigue==1):
                    
                    if fichas_colocadas==0 and palabras_en_tablero > 0:
                        pass
                        
                   
                    if fichas_colocadas == 1 :  
                        pos_disponibles= hay_espacio(window,pos_ficha_anterior[0])
                        for pos in pos_disponibles:
                            tablero.desbloquear_Pos(window,pos[0],pos[1])
                    
                    if fichas_colocadas > 1:
                        
                        if pos_ficha_anterior[0][0] == pos_ficha_anterior[len(pos_ficha_anterior)-1][0]:   
                            #si en la lista de posiciones no cambió el primer valor (el valor de las filas) es porque la palabra se está formando de forma horizontal
                            if(pos_ficha_anterior[0][1] < pos_ficha_anterior[len(pos_ficha_anterior)-1][1] and hay_espacio(window,pos_ficha_anterior[len(pos_ficha_anterior)-1],"derecha")): 
                                #si el valor de la columna de la primera letra colocada es menor al de la ultima letra colocada, la palabra se está formando hacia la derecha
                                tablero.desbloquear_Pos(window,pos_ficha_anterior[len(pos_ficha_anterior)-1][0],pos_ficha_anterior[len(pos_ficha_anterior)-1][1]+1)
                            elif pos_ficha_anterior[0][1] > pos_ficha_anterior[len(pos_ficha_anterior)-1][1] and hay_espacio(window,pos_ficha_anterior[0],"izquierda"):
                                #Si la columna de la ultima ficha colocada tiene un valor menor a la primera ficha colocada entonces la palabra se está formando hacia la izquierda
                                tablero.desbloquear_Pos(window, pos_ficha_anterior[0][0],pos_ficha_anterior[0][1]-1)
                            else: 
                                #Si no tenia espacio a la izquierda o a la derecha entra a el else
                                sigue=0
                                puede_colocar=False
                                Estante.retornar_Ficha_Al_Estante(Estante,evento_ficha,ficha[0],window)
                       
                       
                       
                        #elif pos_ficha_anterior[0][1] == pos_ficha_anterior[len(pos_ficha_anterior)-1][1]:
                        else:
                            #Si entra en este else es porque el valor de la columna de la primera ficha colocada y la ultima no cambió, por lo tanto la palabra se forma de manera vertical
                            if pos_ficha_anterior[0][0] < pos_ficha_anterior[len(pos_ficha_anterior)-1][0] and hay_espacio(window,pos_ficha_anterior[len(pos_ficha_anterior)-1],"abajo"): 
                                #pregunto si se forma hacia abajo y si se puede formar        
                                tablero.desbloquear_Pos(window, pos_ficha_anterior[len(pos_ficha_anterior)-1][0]+1,pos_ficha_anterior[len(pos_ficha_anterior)-1][1])            
                            elif pos_ficha_anterior[0][0] > pos_ficha_anterior[len(pos_ficha_anterior)-1][0] and hay_espacio(window,pos_ficha_anterior[0],"arriba"):  
                                #pregunto si se forma hacia arriba y si se puede formar          
                                tablero.desbloquear_Pos(window,pos_ficha_anterior[0][0]-1,pos_ficha_anterior[0][1])        
                            else: 
                                #qué pasa si no se puede formar más la palabra          
                                sigue=0
                                puede_colocar=False
                                Estante.retornar_Ficha_Al_Estante(Estante, evento_ficha, ficha[0], window)
                   
                   
                    if puede_colocar and not( event in range(7)) and isinstance(event, tuple): 
                        #si la variable puede colocar está en true, el evento no es el atril y el evento es una tupla, coloco la ficha
                        
                        window.FindElement(event).Update(text=ficha[0])
                        tablero.bloquear_tablero(window)
                        
                        #vuelvo a desbloquear el atril para que puedan seguir tomando fichas
                        
                        Estante.desbloquear_Estante(Estante,window)  
                        pos_ficha_anterior.append(event)
                        fichas_colocadas=fichas_colocadas + 1
                        sigue=0  
                        palabra_formada+= ficha[0]
                
                if fichas_colocadas == 2:
                    #Si ya colocó 2 fichas aparece el boton para confirmar palabra
                    window.FindElement('Confirmar Palabra').Update(visible=True)
                if event == 'Confirmar Palabra':

                    #Si toca el boton de confirmar palabra:
                    if (confirmar_Palabra(palabra_formada, "facil")):
                        for pos in pos_ficha_anterior:
                            tablero.tablero[pos[0]][pos[1]]=True
                        puntaje_jugador= puntaje_jugador + puntos.puntaje_palabra(fichas_punt,palabra_formada) #Dante: agregue el puntaje, falta representarlo en el tablero
                        tablero.mostrar_estado()
                        sigue=0
                        turno_Act="Maquina"
                        palabras_en_tablero+=1
                        fichas_colocadas=0
                        puede_colocar=False
                        no_termina_turno=False
                        window.FindElement('Confirmar Palabra').Update(visible=False)
                    else:
                        sg.Popup("No era una palabra aaa")
            
            elif (turno_Act=="maquina"):
                sg.Popup("Ahora le toca a la maquina")
                
                    


    window.Close()
