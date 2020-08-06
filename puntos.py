def split(palabra): 
    return [caracter for caracter in palabra] 


def puntaje_palabra (datos,palabra,window):
    pal = split(palabra)
    punt = 0
    for x in pal:
        window["-out-"].print("Letra:" + x + " Puntaje:" + datos[x], text_color='green')
        punt += int(datos[x])
    return punt