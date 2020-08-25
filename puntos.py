#Variables globales para la perdida por falta de fichas en el atril
estantejglobal = None
estantecglobal = None
fichas_punt_global = None

def split(palabra):
    return [caracter for caracter in palabra]


def multilet(pos, key, dificultad, fichas_punt, POS_ESPECIALES, window, quien):
    # Se aplican los multiplicadores si alguna letra de la palabra esta sobre alguno de estos
    agregado = 0
    try:
        if dificultad == "-facil-":
            for p in POS_ESPECIALES["facil"]["x2letra"]:                
                if p == (pos[0], pos[1]):
                    agregado = agregado + int(fichas_punt[key])
                    print("x2letra: ",p)
                    window[quien].print(
                        "Multiplicador de letra x2: "+key, text_color="black"
                    )
            for p in POS_ESPECIALES["facil"]["x3letra"]:
                if p == (pos[0], pos[1]):
                    agregado = agregado + (int(fichas_punt[key])*2)
                    print("x3letra: ",p)
                    window[quien].print(
                        "Multiplicador de letra x3: " +key, text_color="black"
                    )
        elif dificultad == "-medio-":
            for p in POS_ESPECIALES["medio"]["x2letra"]:
                if p == (pos[0], pos[1]):
                    agregado = agregado + int(fichas_punt[key])
                    window[quien].print(
                        "Multiplicador de letra x2", text_color="black"
                    )
            for p in POS_ESPECIALES["medio"]["x3letra"]:
                if p == (pos[0], pos[1]):
                    agregado = agregado + (int(fichas_punt[key]) * 2)
                    window[quien].print(
                        "Multiplicador de letra x3", text_color="black"
                    )
        else:
            for p in POS_ESPECIALES["dificil"]["x2letra"]:
                if p == (pos[0], pos[1]):
                    agregado = agregado + int(fichas_punt[key])
                    window[quien].print(
                        "Multiplicador de letra x2", text_color="black"
                    )
            for p in POS_ESPECIALES["dificil"]["x3letra"]:
                if p == (pos[0], pos[1]):
                    agregado = agregado + (int(fichas_punt[key]) * 2)
                    window[quien].print(
                        "Multiplicador de letra x3", text_color="black"
                    )
        return agregado
    except Exception:
        return agregado


def multipal(pos1, pos2, dificultad, punt, POS_ESPECIALES, window, quien):
    # Se aplican los multiplicadores/descuentos si la palabra esta sobre alguno de estos
    try:
        if dificultad == "-facil-":
            for p in POS_ESPECIALES["facil"]["x2"]:
                if p == (pos1, pos2):
                    punt = punt * 2
                    window[quien].print(
                        "Multiplicador de palabra x2", text_color="black"
                    )
            for p in POS_ESPECIALES["facil"]["x3"]:
                if p == (pos1, pos2):
                    punt = punt * 3
                    window[quien].print(
                        "Multiplicador de palabra x3", text_color="black"
                    )
            for p in POS_ESPECIALES["facil"]["-2"]:
                if p == (pos1, pos2):
                    punt = punt - 2
                    window[quien].print("Descuento de palabra -2", text_color="black")
            for p in POS_ESPECIALES["facil"]["-3"]:
                if p == (pos1, pos2):
                    punt = punt - 3
                    window[quien].print("Descuento de palabra -3", text_color="black")
        elif dificultad == "-medio-":
            for p in POS_ESPECIALES["medio"]["x2"]:
                if p == (pos1, pos2):
                    punt = punt * 2
                    window[quien].print(
                        "Multiplicador de palabra x2", text_color="black"
                    )
            for p in POS_ESPECIALES["medio"]["x3"]:
                if p == (pos1, pos2):
                    punt = punt * 3
                    window[quien].print(
                        "Multiplicador de palabra x3", text_color="black"
                    )
            for p in POS_ESPECIALES["medio"]["-2"]:
                if p == (pos1, pos2):
                    punt = punt - 2
                    window[quien].print("Descuento de palabra -2", text_color="black")
            for p in POS_ESPECIALES["medio"]["-3"]:
                if p == (pos1, pos2):
                    punt = punt - 3
                    window[quien].print("Descuento de palabra -3", text_color="black")
        else:
            for p in POS_ESPECIALES["dificil"]["x2"]:
                if p == (pos1, pos2):
                    punt = punt * 2
                    window[quien].print(
                        "Multiplicador de palabra x2", text_color="black"
                    )
            for p in POS_ESPECIALES["dificil"]["x3"]:
                if p == (pos1, pos2):
                    punt = punt * 3
                    window[quien].print(
                        "Multiplicador de palabra x3", text_color="black"
                    )
            for p in POS_ESPECIALES["dificil"]["-2"]:
                if p == (pos1, pos2):
                    punt = punt - 2
                    window[quien].print("Descuento de palabra -2", text_color="black")
            for p in POS_ESPECIALES["dificil"]["-3"]:
                if p == (pos1, pos2):
                    punt = punt - 3
                    window[quien].print("Descuento de palabra -3", text_color="black")
        return punt
    except Exception:
        return punt


def puntaje_palabra(datos, palabra, window, quien):
    # Define el puntaje de cada letra de la palabra
    pal = split(palabra)
    punt = 0
    try:
        window[quien].print("Palabra:" + palabra, text_color="black")
    except Exception:
        pass
    for x in pal:
        try:
            window[quien].print(
                "Letra:" + x + " Puntaje:" + datos[x], text_color="black"
            )
        except Exception:
            pass
        punt += int(datos[x])
    return punt
