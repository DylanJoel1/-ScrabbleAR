import PySimpleGUI as sg
import Juego

def main():
    WIDTH  = 20
    HEIGHT = 3
    BUTTON_BORDER = 4
    FUENTE = 'arial'

    botones = [			
                [sg.B('Fácil',button_color=('black','green'),size=(WIDTH, HEIGHT), border_width=BUTTON_BORDER, focus= True, font=FUENTE , key = '-facil-')],
                [sg.B('Medio',button_color=('black','green'), size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE     , key = '-medio-')],
                [sg.B('Difícil',button_color=('black','green') ,size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE          , key = '-dificil-')],
                [sg.B('VOLVER', button_color=('black','#ff4d4d'), size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE,             key = '-volver-')]
    ]

    layout = [	
                [sg.T('Dificultad', font=('Helvetica', 30), text_color=('black'), border_width=30)],
                [sg.Column(botones,justification='c' )]
                ]

    window = sg.Window('Seleccione dificultad', layout, size=(400,500), element_justification='c')

    while True:
        event, values = window.read()
        if (event is None or event == '-volver-'):
            break
        if event == '-facil-':
            Juego.main("-facil-")
        if event == '-medio-':
            Juego.main("-medio-")
        if event == '-dificil-':
            Juego.main("-dificil-")

    window.close()