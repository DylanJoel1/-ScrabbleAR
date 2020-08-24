import PySimpleGUI as sg


def Reglas():
    FUENTE = "arial"

    objetivo_layout = [
        [
            sg.T(
                "\n Objetivo del juego: Se deben acumular la mayor cantidad de puntos"
                " en el tiempo dado, los puntos se consiguen al formar palabras (con 2"
                " o más letras). Dependiendo de la dificultad asignada solo se pueden"
                " formar Sustantivos, verbos y adjetivos. En Facil se pueden formar Sustantivos,"
                " adjetivos y verbos, en Medio y dificil solo Adjetivos y Verbos."
                " Para comprobar en que dificultad estamos podemos ver el apartado de"
                " datos en la partida. Ademas una de las condiciones para ganar la partida"
                " es hacerlo dentro del tiempo estipulado, esto mismo se puede configurar"
                " y se encuentra representado en el apartado de datos dentro de la partida."
                " Para empezar la partida debemos darle al boton Jugar.",
                size=(100, 10),
                font=(FUENTE, 13),
                text_color="white",
            )
        ],
        [
            sg.Image("imagenes/02.png", pad=(1,1)), sg.Image("imagenes/03.png", pad=(1,1)), sg.Image("imagenes/01.png", pad=(1,1))
        ]
    ]

    inicio_layout = [
        [
            sg.T(
                    "\n Inicio de la partida: Al inicio de la partida se asigna de forma aleatoria quién va a ser el"
                    " que comienza a jugar, luego se le reparten 7 fichas al jugador y a la"
                    " computadora para que puedan empezar a formar palabras. La primera palabra"
                    " de todas tiene que iniciar en el centro del tablero, puede estar"
                    " orientada de forma horizontal o vertical. Luego de colocar todas"
                    " las letras para formar la palabra deseada se tendrá que dar"
                    " al boton Confirmar, el cual evaluara si la palabra formada"
                    " es correcta. En caso de serlo se pasara de turno y se sumaran"
                    " los puntos indicados para cada letra en el apartado de datos"
                    " de la partida. Si la palabra formada no es correcta se devolveran"
                    " las fichas introducidas al estante del jugador.",
                    size=(100, 5),
                    font=(FUENTE, 13),
                    text_color="white",
            )
        ],
        [
            sg.Image("imagenes/04.png", pad=(1,1))
        ]
    ]

    turno_layout = [
        [
            sg.T(
                    "\n Turnos: En cada turno"
                    " el jugador debe formar una palabra con las fichas de su atril, en"
                    " caso de no poder formar palabras puede cambiar todas o algunas por"
                    " otras fichas aleatorias de la bolsa, en caso de hacerlo el jugador"
                    " pierde el turno y podrá volver a formar palabras después del turno de"
                    " la computadora. En caso de necesitar guardar la partida, esto solo se"
                    " pordra ejecutar al inicio del turno del jugador.",
                    size=(100, 5),
                    font=(FUENTE, 13),
                    text_color="white",
            )
        ],
        [
            sg.Image("imagenes/05.png", pad=(1,1))
        ]
    ]

    tablero_layout = [
        [
            sg.T(
                    "\n Tablero: El tablero posee casillas especiales que"
                    " varían dependiendo de la dificultad asignada. En cada tablero hay"
                    " casillas que aumentan el valor de las fichas asi como otras reducen"
                    " el valor de la ficha. En el apartado de datos se especifica"
                    " cuales y como son las casillas especiales. En caso de que"
                    " la palabra formada se posicione por encima de una de estas"
                    " casillas especiales se calculara el bono o descuento a los"
                    " puntos del jugador.",
                    size=(100, 5),
                    font=(FUENTE, 13),
                    text_color="white",
            )
        ],
        [
            sg.Image("imagenes/06.png", pad=(1,1))
        ]
    ]

    fichas_layout = [
        [
            sg.T(
                    "\n Fichas: Cada ficha posee un valor único,"
                    " las fichas con las que sea más dificil formar palabras poseen un"
                    " valor superior a las demás. Hay una cantidad limitada de fichas"
                    " iguales en la bolsa. En el apartado de configuracion el usuario"
                    " puede cambiar a su gusto la cantidad de fichas y sus puntajes",
                    size=(100, 5),
                    font=(FUENTE, 13),
                    text_color="white",
            )
        ],
        [
            sg.Image("imagenes/07.png", pad=(1,1))
        ]
    ]

    layout_Reglas = [
        [
            sg.T(
                "Reglas ScrabbleAR",
                justification="center",
                font=(FUENTE, 20),
                size=(55, 0),
                background_color="#00FFFF",
                text_color="#000080",
            )
        ],
        [
            sg.TabGroup(
                [
                    [
                        sg.Tab("Objetivo", objetivo_layout, element_justification="center"),
                        sg.Tab("Inicio", inicio_layout, element_justification="center"),
                        sg.Tab("Turnos", turno_layout, element_justification="center"),
                        sg.Tab("Tablero", tablero_layout, element_justification="center"),
                        sg.Tab("Fichas", fichas_layout, element_justification="center"),
                    ]
                ]
            )
        ],
        [
            sg.B(
                "Volver", size=(8, 2), key="-volver-", button_color=("black", "#FA8072")
            )
        ],
    ]

    window = sg.Window("Reglas", layout_Reglas)
    while True:
        event, values = window.read()
        if event is None or event == "-volver-":
            break
    window.close()
