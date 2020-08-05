import PySimpleGUI as sg
import json
from config import guardar
import os
import Juego

def comprobar(window):
    try:
        with open("partida1.json", 'r'):
            window.FindElement('-c1-').Update(button_color=('black','green'))

    except FileNotFoundError:
        window.FindElement('-c1-').Update(button_color=('black','grey'))

    try:
        with open("partida2.json", 'r'):
            window.FindElement('-c2-').Update(button_color=('black','green'))

    except FileNotFoundError:
        window.FindElement('-c2-').Update(button_color=('black','grey'))

    try:
        with open("partida3.json", 'r'):
            window.FindElement('-c3-').Update(button_color=('black','green'))

    except FileNotFoundError:
        window.FindElement('-c3-').Update(button_color=('black','grey'))


def c(a):
    try:
        with open(a, 'r') as jsonFile:
            datos = json.load(jsonFile)
            return datos
    except FileNotFoundError:
        sg.Popup("No se encontro el archivo")


def borrar(a):
    os.remove(a)


def main():
    WIDTH  = 20
    HEIGHT = 3
    BUTTON_BORDER = 4
    FUENTE = 'arial'
    primera = 1

    botones = [
                [sg.B('Cargar 1',button_color=('black','green'),size=(WIDTH, HEIGHT), border_width=BUTTON_BORDER, focus= True, font=FUENTE , key = '-c1-')],
                [sg.B('Cargar 2',button_color=('black','green'), size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE, key = '-c2-')],
                [sg.B('Cargar 3',button_color=('black','green') ,size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE, key = '-c3-')],
                [sg.B('VOLVER', button_color=('black','#ff4d4d'), size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE,key = '-volver-')]
    ]

    layout = [	
                [sg.T('Cargar', font=('Helvetica', 30), text_color=('black'), border_width=30)],
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
        if event == '-c1-':
            datos = c("partida1.json")
            Juego.main(None, datos)
        if event == '-c2-':
            datos = c("partida2.json")
            Juego.main(None, datos)
        if event == '-c3-':
            datos = c("partida3.json")
            Juego.main(None, datos)

    window.close()