
from ClaseFicha import Ficha

TAMAÑO_ESTANTE = 7

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

    def cambiar_fichas(self, window, ATRIL_JUGADOR="", cant="todas"):
        if cant == "todas":
            for i in range(TAMAÑO_ESTANTE):
                aux = self.atril.quitar_ficha
                if aux == None:
                    return False
                self.estante[i] = aux
                window.FindElement(i).Update(
                    text=self.estante[i].get_letra(),
                    image_filename=(
                        "imagenes/" + self.estante[i].get_letra() + ".png"),

                )
        elif cant == "marcadas":
            for i in range(TAMAÑO_ESTANTE):
                if ATRIL_JUGADOR[i] != "":
                    aux = self.atril.quitar_ficha
                    if aux == None:
                        return False
                    self.estante[i] = aux
                    window.FindElement(i).Update(
                        text=self.estante[i].get_letra(),
                        image_filename=(
                            "imagenes/" + self.estante[i].get_letra() + ".png"),

                    )

    def agregar_fichas(self, window, ATRIL_JUGADOR="", turno="jugador"):

        if turno == "jugador":
            # agrega la cantidad de fichas que se le envían por parametro al estante del jugador.
            aux = []
            for i in range(len(ATRIL_JUGADOR)):
                if ATRIL_JUGADOR[i] != "":
                    aux += [i]
            for pos in aux:
                var_aux = self.atril.quitar_ficha()
                if var_aux == None:
                    return False
                self.estante[pos] = var_aux
                window.FindElement(pos).Update(
                    text=self.estante[pos].get_letra(),
                    image_filename=(
                        "imagenes/" + self.estante[pos].get_letra() + ".png"),
                )
        elif turno == "maquina":

            for i in range(len(self.estante)):
                if self.estante[i] == "":
                    var_aux = self.atril.quitar_ficha()
                    if var_aux == None:
                        return False
                    self.estante[i] = var_aux

    def eliminar_fichas_estante(self,ATRIL_JUGADOR="" ,pos=""):
        # Elimina la ficha del estante, no solo de la interfaz
        if pos == "":
            for i in range(len(ATRIL_JUGADOR)):
                if ATRIL_JUGADOR[i] != "":
                    self.estante[i] = ""
        else:
            if ATRIL_JUGADOR[pos] != "":
                self.estante[pos] = ""

    def no_tiene_fichas(self):

        elementos = self.estante.count("")
        if elementos == 7:
            return True
        else:
            return False

    def inicializar(self):
        # Añade las primeras 7 fichas al estante
        for _ in range(7):
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

    def desbloquear_pos_Estante(self, window, ATRIL_JUGADOR):
        # desbloquea el estante
        for i in range(7):
            if ATRIL_JUGADOR[i] == "":
                window.FindElement(i).Update(disabled=False)

    def quitar_Ficha_De_Estante(self, bot, window, ATRIL_JUGADOR):
        # quita de la interfaz una ficha del estante
        ATRIL_JUGADOR[bot] = window.FindElement(bot).get_text()
        window.FindElement(bot).Update(
            text="", image_size=(36, 38), image_filename="", disabled=True
        )

    def retornar_Ficha_Al_Estante(self, window, pos_estante, ATRIL_JUGADOR):
        # devuelve una ficha del tablero al estante
        self.estante[pos_estante] = ATRIL_JUGADOR[pos_estante]

        if ATRIL_JUGADOR[pos_estante] == "":
            window.FindElement(pos_estante).Update(
                image_filename="", visible=True, image_size=(36, 38),
                disabled=True
            )
        else:
            window.FindElement(pos_estante).Update(
                text=ATRIL_JUGADOR[pos_estante],
                image_filename=(
                    ("imagenes/" + ATRIL_JUGADOR[pos_estante].upper() + ".png")
                ),
                visible=True,
                disabled=False
            )
        ATRIL_JUGADOR[pos_estante] == ""
