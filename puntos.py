def split(palabra): 
    return [caracter for caracter in palabra] 


def puntaje_palabra (datos,palabra):
    pal = split(palabra)
    punt = 0
    for x in pal:
        punt += int(datos[x])
    return punt