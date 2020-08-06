def split(palabra): 
    return [caracter for caracter in palabra]

def multilet(pos,key,dificultad,fichas_punt):
    agregado = 0
    if dificultad == "-facil-":
        if (pos[0],pos[1]) == (5,5):
            agregado = agregado + fichas_punt[key]
        #2
        if (pos[0],pos[1]) == (9,9):
            agregado = agregado + fichas_punt[key]
        #3
        if (pos[0],pos[1]) == (5,9):
            agregado = agregado + fichas_punt[key]
        #4
        if (pos[0],pos[1]) == (9,5):
            agregado = agregado + fichas_punt[key]
        #5
        if (pos[0],pos[1]) == (3,0):
            agregado = agregado + (fichas_punt[key]*2)
        if (pos[0],pos[1]) == (11,0):
            agregado = agregado + (fichas_punt[key]*2)
        if (pos[0],pos[1]) == (5,1):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (9,1):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (6,2):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (8,2):
            agregado = agregado + fichas_punt[key]
        #6
        if (pos[0],pos[1]) == (0,3):
            agregado = agregado + (fichas_punt[key]*2)
        if (pos[0],pos[1]) == (0,11):
            agregado = agregado + (fichas_punt[key]*2)
        if (pos[0],pos[1]) == (1,5):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (1,9):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (2,6):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (2,8):
            agregado = agregado + fichas_punt[key]
        #5
        if (pos[0],pos[1]) == (3,14):
            agregado = agregado + (fichas_punt[key]*2)
        if (pos[0],pos[1]) == (11,14):
            agregado = agregado + (fichas_punt[key]*2)
        if (pos[0],pos[1]) == (5,13):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (9,13):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (6,12):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (8,12):
            agregado = agregado + fichas_punt[key]
        #5
        if (pos[0],pos[1]) == (14,3):
            agregado = agregado + (fichas_punt[key]*2)
        if (pos[0],pos[1]) == (14,11):
            agregado = agregado + (fichas_punt[key]*2)
        if (pos[0],pos[1]) == (13,5):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (13,9):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (12,6):
            agregado = agregado + fichas_punt[key]
        if (pos[0],pos[1]) == (12,8):
            agregado = agregado + fichas_punt[key]
    elif dificultad == "-medio-":
        pass
    else:
        pass
    return agregado


def multipal(pos1,pos2,dificultad,punt):
    if dificultad == "-facil-":
        if (pos1,pos2) == (0,0):
            punt = punt*3
        elif (pos1,pos2) == (1,1):
            punt = punt*2
        elif (pos1,pos2) == (2,2):
            punt = punt*2
        elif (pos1,pos2) == (3,3):
            punt = punt - 3
        elif (pos1,pos2) == (4,4):
            punt = punt*2
        elif (pos1,pos2) == (6,6):
            punt = punt*2
        #2
        elif (pos1,pos2) == (14,14):
            punt = punt*3
        elif (pos1,pos2) == (13,13):
            punt = punt*2
        elif (pos1,pos2) == (12,12):
            punt = punt*2
        elif (pos1,pos2) == (11,11):
            punt = punt - 3
        elif (pos1,pos2) == (10,10):
            punt = punt*2
        elif (pos1,pos2) == (8,8):
            punt = punt*2
        #3
        elif (pos1,pos2) == (0,14):
            punt = punt*3
        elif (pos1,pos2) == (1,13):
            punt = punt*2
        elif (pos1,pos2) == (2,12):
            punt = punt*2
        elif (pos1,pos2) == (3,11):
            punt = punt - 3
        elif (pos1,pos2) == (4,10):
            punt = punt*2
        elif (pos1,pos2) == (6,8):
            punt = punt*2
        #4
        elif (pos1,pos2) == (14,0):
            punt = punt*3
        elif (pos1,pos2) == (13,1):
            punt = punt*2
        elif (pos1,pos2) == (12,2):
            punt = punt*2
        elif (pos1,pos2) == (11,3):
            punt = punt - 3
        elif (pos1,pos2) == (10,4):
            punt = punt*2
        elif (pos1,pos2) == (8,6):
            punt = punt*2
        #5
        elif (pos1,pos2) == (7,0):
            punt = punt*3
        elif (pos1,pos2) == (7,3):
            punt = punt-1
        #6
        elif (pos1,pos2) == (0,7):
            punt = punt*3
        elif (pos1,pos2) == (3,7):
            punt = punt-1
        #7
        elif (pos1,pos2) == (7,14):
            punt = punt*3
        elif (pos1,pos2) == (7,11):
            punt = punt-1
        #8
        elif (pos1,pos2) == (14,7):
            punt = punt*3
        elif (pos1,pos2) == (11,7):
            punt = punt-1
    elif dificultad == "-medio-":
        pass
    else:
        pass
    return punt


def puntaje_palabra (datos,palabra,window):
    pal = split(palabra)
    punt = 0
    window["-out-"].print("Palabra:" + palabra, text_color='black')
    for x in pal:
        try:
            window["-out-"].print("Letra:" + x + " Puntaje:" + datos[x], text_color='black')
        except Exception:
            pass
        punt += int(datos[x])
    return punt
