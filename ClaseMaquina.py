from ClaseEstante import Estante
import itertools as it
from funcionAutenticar import confirmar_Palabra

class Computadora:
    """ Por ahora este objeto solo posee la funcion de generar una palabra, la cual dependiendo las letras que posee la computadora genera un conjunto de las combinaciones
        posibles. En la misma funcion se llama a una funcion de un archivo que importo para devolver la palabra de las combinaciones que cumple con las condiciones del juego
     """

    def __init__(self, atril, puntaje=0, letras="", datos=None):
        if datos != None:
            datosA = datos["maquina"]
            self.puntaje = datosA["puntaje"]
            self.estante = Estante(atril, datosA)
            self.let = letras
        else:
            self.puntaje = puntaje
            self.let = letras
            self.estante = Estante(atril)

    def set_letras(self, letras):
        self.let = letras

    def incrementar_puntaje(self, agregado, window):
        # Incrementa el puntaje del jugador
        self.puntaje += agregado
        window["-puntajepc-"].update(self.puntaje)

    def get_puntaje(self):
        # Devuelve el puntaje de la maquina
        return self.puntaje

    # 	def pedirFichas:

    def get_estante(self):
        # Devuelve un arreglo con los elementos del estante, para poder representarlo en pysimplegui
        return self.estante.get_estante()

    def get_letras(self):
        return self.let

    def crearPalabra(self, DIFICULTAD):
        palabras = set()
        # uso un conjunto para no guardar palabras repetidas

        for i in range(2, len(self.let) + 1):
            palabras.update((map("".join, it.permutations(self.let, i))))
            # permutations me devuelve todas las permutaciones posibles con esas letras

        lista_aux = []
        for elem in palabras:
            # itero con los valores del conjuto secundario asi voy borrando los elementos que no sean palabras válidas
            if (confirmar_Palabra(elem, DIFICULTAD)):
                lista_aux.append(elem)

        if len(lista_aux) == 0:
            return ""

        palabra_larga = max(
            lista_aux, key=len
        )  # de todas las palabras validas me quedo con la más larga dado que es la que da mayor cantidad de puntos y es más seguro que sea una palabra segura

        return palabra_larga

    def pedir_fichas_nuevas(self,ATRIL_JUGADOR):
        self.let = ""
        for i in range(len(self.estante.estante)):
            self.estante.estante[i] = ""
        if self.estante.agregar_fichas(None, ATRIL_JUGADOR, "maquina") == False:
            return False

    def cambiar_letras(self, palabra, ATRIL_JUGADOR):
        for letra in palabra:
            #elimino las letras utilizadas de la variable con las letras disponibles
            if letra in self.let:
                self.let = self.let.replace(letra, "", 1)
            for i in range(len(self.estante.estante)):
                if letra in str(self.estante.estante[i]):
                    self.estante.estante[i] = ""
                    break
        if self.estante.agregar_fichas(None, ATRIL_JUGADOR, "maquina") == False:
            return False
