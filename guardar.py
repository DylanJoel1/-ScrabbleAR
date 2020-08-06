import PySimpleGUI as sg
import json
from config import guardar
import os
import sys
sys.path.insert(1, '/guardado')

def comprobar(window):
    try:
        with open("guardado/partida1.json", 'r'):
            window.FindElement('-g1-').Update(button_color=('black','grey'))
            window.FindElement('-bg1-').Update(visible=True)
    except FileNotFoundError:
        window.FindElement('-g1-').Update(button_color=('black','green'))
        window.FindElement('-bg1-').Update(visible=False)
    try:
        with open("guardado/partida2.json", 'r'):
            window.FindElement('-g2-').Update(button_color=('black','grey'))
            window.FindElement('-bg2-').Update(visible=True)
    except FileNotFoundError:
        window.FindElement('-g2-').Update(button_color=('black','green'))
        window.FindElement('-bg2-').Update(visible=False)
    try:
        with open("guardado/partida3.json", 'r'):
            window.FindElement('-g3-').Update(button_color=('black','grey'))
            window.FindElement('-bg3-').Update(visible=True)
    except FileNotFoundError:
        window.FindElement('-g3-').Update(button_color=('black','green'))
        window.FindElement('-bg3-').Update(visible=False)


def borrar(a):
    os.remove(a)


def main(datos):
    WIDTH  = 15
    HEIGHT = 3
    BUTTON_BORDER = 4
    FUENTE = 'arial'
    primera = 1

    botones = [
                [sg.B('Guardado 1',button_color=('black','green'),size=(WIDTH, HEIGHT), border_width=BUTTON_BORDER, focus= True, font=FUENTE , key = '-g1-'), sg.B("Borrar",button_color=('black','red'),size=(5, HEIGHT), border_width=BUTTON_BORDER, font=FUENTE , key = '-bg1-',visible=False)],
                [sg.B('Guardado 2',button_color=('black','green'), size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE, key = '-g2-'), sg.B("Borrar",button_color=('black','red'),size=(5, HEIGHT), border_width=BUTTON_BORDER, font=FUENTE , key = '-bg2-', visible=False)],
                [sg.B('Guardado 3',button_color=('black','green') ,size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE, key = '-g3-'), sg.B("Borrar",button_color=('black','red'),size=(5, HEIGHT), border_width=BUTTON_BORDER, font=FUENTE , key = '-bg3-', visible=False)],
                [sg.B('VOLVER', button_color=('black','#ff4d4d'), size=(20, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE,key = '-volver-')]
    ]

    layout = [	
                [sg.T('Guardar', font=('Helvetica', 30), text_color=('black'), border_width=30)],
                [sg.Column(botones,justification='c' )]
                ]

    window = sg.Window('Seleccione dificultad', layout, size=(400,500), element_justification='c')

    while True:
        if primera == 1:
            window.Finalize()
            comprobar(window)
            primera = 0
        event, values = window.read()
        if (event is None or event == '-volver-'):
            break
        if event == '-g1-':
            guardar("guardado/partida1.json",datos)
            comprobar(window)
        if event == '-g2-':
            guardar("guardado/partida2.json",datos)
            comprobar(window)
        if event == '-g3-':
            guardar("guardado/partida3.json",datos)
            comprobar(window)
        if event == '-bg1-':
            borrar("guardado/partida1.json")
            comprobar(window)
        if event == '-bg2-':
            borrar("guardado/partida2.json")
            comprobar(window)
        if event == '-bg3-':
            borrar("guardado/partida3.json")
            comprobar(window)

    window.close()