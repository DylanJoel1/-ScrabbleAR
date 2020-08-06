def split(palabra): 
    return [caracter for caracter in palabra]

def multilet(pos,key,dificultad,fichas_punt,POS_ESPECIALES):
    agregado = 0
    if dificultad == "-facil-":
        for p in POS_ESPECIALES["facil"]["x2letra"]:
            if p == (pos[0],pos[1]):
                agregado = agregado + fichas_punt[key]
        for p in POS_ESPECIALES["facil"]["x3letra"]:
            if p == (pos[0],pos[1]):
                agregado = agregado + (fichas_punt[key]*2)
    elif dificultad == "-medio-":
        for p in POS_ESPECIALES["medio"]["x2letra"]:
            if p == (pos[0],pos[1]):
                agregado = agregado + fichas_punt[key]
        for p in POS_ESPECIALES["medio"]["x3letra"]:
            if p == (pos[0],pos[1]):
                agregado = agregado + (fichas_punt[key]*2)
    else:
        for p in POS_ESPECIALES["dificil"]["x2letra"]:
            if p == (pos[0],pos[1]):
                agregado = agregado + fichas_punt[key]
        for p in POS_ESPECIALES["dificil"]["x3letra"]:
            if p == (pos[0],pos[1]):
                agregado = agregado + (fichas_punt[key]*2)
    return agregado


def multipal(pos1,pos2,dificultad,punt,POS_ESPECIALES):
    if dificultad == "-facil-":
        for p in POS_ESPECIALES["facil"]["x2"]:
            if p == (pos1,pos2):
                punt = punt*2
        for p in POS_ESPECIALES["facil"]["x3"]:
            if p == (pos1,pos2):
                punt = punt*3
        for p in POS_ESPECIALES["facil"]["-2"]:
            if p == (pos1,pos2):
                punt = punt -2
        for p in POS_ESPECIALES["facil"]["-3"]:
            if p == (pos1,pos2):
                punt = punt -3
    elif dificultad == "-medio-":
        for p in POS_ESPECIALES["medio"]["x2"]:
            if p == (pos1,pos2):
                punt = punt*2
        for p in POS_ESPECIALES["medio"]["x3"]:
            if p == (pos1,pos2):
                punt = punt*3
        for p in POS_ESPECIALES["medio"]["-2"]:
            if p == (pos1,pos2):
                punt = punt -2
        for p in POS_ESPECIALES["medio"]["-3"]:
            if p == (pos1,pos2):
                punt = punt -3
    else:
        for p in POS_ESPECIALES["dificil"]["x2"]:
            if p == (pos1,pos2):
                punt = punt*2
        for p in POS_ESPECIALES["dificil"]["x3"]:
            if p == (pos1,pos2):
                punt = punt*3
        for p in POS_ESPECIALES["dificil"]["-2"]:
            if p == (pos1,pos2):
                punt = punt -2
        for p in POS_ESPECIALES["dificil"]["-3"]:
            if p == (pos1,pos2):
                punt = punt -3
    return punt


def puntaje_palabra (datos,palabra,window):
    pal = split(palabra)
    punt = 0
   # window["-out-"].print("Palabra:" + palabra, text_color='black')
    for x in pal:
        try:
            window["-out-"].print("Letra:" + x + " Puntaje:" + datos[x], text_color='black')
        except Exception:
            pass
        punt += int(datos[x])
    return punt
