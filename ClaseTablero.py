
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

    def quitar_elemento(self, window, pos, color=""):
        self.tablero[pos[0]][pos[1]] = False
        if color != "":
            window.FindElement(pos).Update(
                text="", image_filename="", image_size=(36, 38), button_color=("white", color)
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
