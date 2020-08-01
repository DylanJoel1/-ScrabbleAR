import PySimpleGUI as sg

def main():
    layout = [	
                [sg.T('Top 10', font=('Helvetica', 30), text_color=('black'), border_width=30)],
                [sg.B("Pos.",button_color=('black','grey'), size=(8,1), pad=(0,0)), sg.B("Nombre",button_color=('black','grey'), size=(14,1), pad=(0,0)), sg.B("Puntos",button_color=('black','grey'), size=(8,1), pad=(0,0))],
                [sg.T("1", size=(8,1), justification="center", pad=(0,0)), sg.T("Vacio", size=(14,1), justification="center", pad=(0,0), key="nombre1"), sg.T("0", size=(8,1), justification="center", pad=(0,0), key="puntos1")],
                [sg.T("2", size=(8,1), justification="center", pad=(0,0)), sg.T("Vacio", size=(14,1), justification="center", pad=(0,0), key="nombre2"), sg.T("0", size=(8,1), justification="center", pad=(0,0), key="puntos2")],
                [sg.T("3", size=(8,1), justification="center", pad=(0,0)), sg.T("Vacio", size=(14,1), justification="center", pad=(0,0), key="nombre3"), sg.T("0", size=(8,1), justification="center", pad=(0,0), key="puntos3")],
                [sg.T("4", size=(8,1), justification="center", pad=(0,0)), sg.T("Vacio", size=(14,1), justification="center", pad=(0,0), key="nombre4"), sg.T("0", size=(8,1), justification="center", pad=(0,0), key="puntos4")],
                [sg.T("5", size=(8,1), justification="center", pad=(0,0)), sg.T("Vacio", size=(14,1), justification="center", pad=(0,0), key="nombre5"), sg.T("0", size=(8,1), justification="center", pad=(0,0), key="puntos5")],
                [sg.T("6", size=(8,1), justification="center", pad=(0,0)), sg.T("Vacio", size=(14,1), justification="center", pad=(0,0), key="nombre6"), sg.T("0", size=(8,1), justification="center", pad=(0,0), key="puntos6")],
                [sg.T("7", size=(8,1), justification="center", pad=(0,0)), sg.T("Vacio", size=(14,1), justification="center", pad=(0,0), key="nombre7"), sg.T("0", size=(8,1), justification="center", pad=(0,0), key="puntos7")],
                [sg.T("8", size=(8,1), justification="center", pad=(0,0)), sg.T("Vacio", size=(14,1), justification="center", pad=(0,0), key="nombre8"), sg.T("0", size=(8,1), justification="center", pad=(0,0), key="puntos8")],
                [sg.T("9", size=(8,1), justification="center", pad=(0,0)), sg.T("Vacio", size=(14,1), justification="center", pad=(0,0), key="nombre9"), sg.T("0", size=(8,1), justification="center", pad=(0,0), key="puntos9")],
                [sg.T("10", size=(8,1), justification="center", pad=(0,0)), sg.T("Vacio", size=(14,1), justification="center", pad=(0,0), key="nombre10"), sg.T("0", size=(8,1), justification="center", pad=(0,0), key="puntos10")],
                [sg.B("Restaurar a por defecto", size=(20,2), key="-default-", button_color=("black","#FA8072")), sg.B("Volver", size=(8,2), key="-volver-", button_color=("black","#FA8072"))]
                ]

    window = sg.Window('Top 10', layout, size=(400,500), element_justification='c')

    while True:
        event, values = window.read()
        if (event is None or event == '-volver-'):
            break

    window.close()