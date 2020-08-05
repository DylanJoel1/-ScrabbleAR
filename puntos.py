def split(palabra): 
    return [caracter for caracter in palabra] 


def puntaje_palabra (datos,palabra):
    pal = split(palabra)
    for x in pal:
        punt = punt + datos[x]
    return punt

puntaje_palabra