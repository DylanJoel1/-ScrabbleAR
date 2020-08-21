import PySimpleGUI as sg


def Reglas():
    FUENTE = "arial"

    layout_Reglas = [
        [
            sg.T(
                "Reglas ScrabbleAR",
                justification="center",
                font=(FUENTE, 20),
                size=(55, 2),
                background_color="#00FFFF",
                text_color="#000080",
            )
        ],
        [
            sg.T(
                "\n\n Objetivo del juego: Se deben acumular la mayor cantidad de puntos"
                " en el tiempo dado, los puntos se consiguen al formar palabras (con 2"
                " o más letras). Dependiendo de la dificultad asignada solo se pueden"
                " formar Sustantivos, verbos y adjetivos.\n\nInicio de la partida: Al"
                " inicio de la partida se asigna de forma aleatoria quién va a ser el"
                " que comienza a jugar, luego se le reparten 7 fichas al jugador y a la"
                " máquina para que puedan empezar a formar palabras. La primera palabra"
                " de todas tiene que iniciar en el centro del tablero, puede estar"
                " orientada de forma horizontal o vertical.\n\n Turnos: En cada turno"
                " el jugador debe formar una palabra con las fichas de su atril, en"
                " caso de no poder formar palabras puede cambiar todas o algunas por"
                " otras fichas aleatorias de la bolsa, en caso de hacerlo el jugador"
                " pierde el turno y podrá volver a formar palabras después del turno de"
                " la máquina\n\n Tablero: El tablero posee casillas especiales que"
                " varían dependiendo de la dificultad asignada. En cada tablero hay"
                " casillas que aumentan el valor de las fichas asi como otras reducen"
                " el valor de la ficha. \n\n Fichas: Cada ficha posee un valor único,"
                " las fichas con las que sea más dificil formar palabras poseen un"
                " valor superior a las demás. Hay una cantidad limitada de fichas"
                " iguales en la bolsa.",
                size=(100, 20),
                font=(FUENTE, 13),
                text_color="#000080",
            )
        ],
        [
            sg.B(
                "Volver", size=(8, 2), key="-volver-", button_color=("black", "#FA8072")
            )
        ],
    ]

    window = sg.Window("Reglas", layout_Reglas)
    e, v = window.read()
    window.close()
