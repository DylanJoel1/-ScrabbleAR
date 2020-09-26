from ClaseEstante import Estante

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