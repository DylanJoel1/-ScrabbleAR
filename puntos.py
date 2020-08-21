def split(palabra):
    return [caracter for caracter in palabra]


def multilet(pos, key, dificultad, fichas_punt, POS_ESPECIALES, window):
    # Se aplican los multiplicadores si alguna letra de la palabra esta sobre alguno de estos
    agregado = 0
    try:
        if dificultad == "-facil-":
            for p in POS_ESPECIALES["facil"]["x2letra"]:
                if p == (pos[0], pos[1]):
                    agregado = agregado + fichas_punt[key]
                    window["-out-"].print(
                        "Multiplicador de letra x2", text_color="black"
                    )
            for p in POS_ESPECIALES["facil"]["x3letra"]:
                if p == (pos[0], pos[1]):
                    agregado = agregado + (fichas_punt[key] * 2)
                    window["-out-"].print(
                        "Multiplicador de letra x3", text_color="black"
                    )
        elif dificultad == "-medio-":
            for p in POS_ESPECIALES["medio"]["x2letra"]:
                if p == (pos[0], pos[1]):
                    agregado = agregado + fichas_punt[key]
                    window["-out-"].print(
                        "Multiplicador de letra x2", text_color="black"
                    )
            for p in POS_ESPECIALES["medio"]["x3letra"]:
                if p == (pos[0], pos[1]):
                    agregado = agregado + (fichas_punt[key] * 2)
                    window["-out-"].print(
                        "Multiplicador de letra x3", text_color="black"
                    )
        else:
            for p in POS_ESPECIALES["dificil"]["x2letra"]:
                if p == (pos[0], pos[1]):
                    agregado = agregado + fichas_punt[key]
                    window["-out-"].print(
                        "Multiplicador de letra x2", text_color="black"
                    )
            for p in POS_ESPECIALES["dificil"]["x3letra"]:
                if p == (pos[0], pos[1]):
                    agregado = agregado + (fichas_punt[key] * 2)
                    window["-out-"].print(
                        "Multiplicador de letra x3", text_color="black"
                    )
        return agregado
    except Exception:
        return 0


def multipal(pos1, pos2, dificultad, punt, POS_ESPECIALES, window):
    # Se aplican los multiplicadores/descuentos si la palabra esta sobre alguno de estos
    try:
        if dificultad == "-facil-":
            for p in POS_ESPECIALES["facil"]["x2"]:
                if p == (pos1, pos2):
                    punt = punt * 2
                    window["-out-"].print(
                        "Multiplicador de palabra x2", text_color="black"
                    )
            for p in POS_ESPECIALES["facil"]["x3"]:
                if p == (pos1, pos2):
                    punt = punt * 3
                    window["-out-"].print(
                        "Multiplicador de palabra x3", text_color="black"
                    )
            for p in POS_ESPECIALES["facil"]["-2"]:
                if p == (pos1, pos2):
                    punt = punt - 2
                    window["-out-"].print("Descuento de palabra -2", text_color="black")
            for p in POS_ESPECIALES["facil"]["-3"]:
                if p == (pos1, pos2):
                    punt = punt - 3
                    window["-out-"].print("Descuento de palabra -3", text_color="black")
        elif dificultad == "-medio-":
            for p in POS_ESPECIALES["medio"]["x2"]:
                if p == (pos1, pos2):
                    punt = punt * 2
                    window["-out-"].print(
                        "Multiplicador de palabra x2", text_color="black"
                    )
            for p in POS_ESPECIALES["medio"]["x3"]:
                if p == (pos1, pos2):
                    punt = punt * 3
                    window["-out-"].print(
                        "Multiplicador de palabra x3", text_color="black"
                    )
            for p in POS_ESPECIALES["medio"]["-2"]:
                if p == (pos1, pos2):
                    punt = punt - 2
                    window["-out-"].print("Descuento de palabra -2", text_color="black")
            for p in POS_ESPECIALES["medio"]["-3"]:
                if p == (pos1, pos2):
                    punt = punt - 3
                    window["-out-"].print("Descuento de palabra -3", text_color="black")
        else:
            for p in POS_ESPECIALES["dificil"]["x2"]:
                if p == (pos1, pos2):
                    punt = punt * 2
                    window["-out-"].print(
                        "Multiplicador de palabra x2", text_color="black"
                    )
            for p in POS_ESPECIALES["dificil"]["x3"]:
                if p == (pos1, pos2):
                    punt = punt * 3
                    window["-out-"].print(
                        "Multiplicador de palabra x3", text_color="black"
                    )
            for p in POS_ESPECIALES["dificil"]["-2"]:
                if p == (pos1, pos2):
                    punt = punt - 2
                    window["-out-"].print("Descuento de palabra -2", text_color="black")
            for p in POS_ESPECIALES["dificil"]["-3"]:
                if p == (pos1, pos2):
                    punt = punt - 3
                    window["-out-"].print("Descuento de palabra -3", text_color="black")
        return punt
    except Exception:
        return punt


def puntaje_palabra(datos, palabra, window):
    # Define el puntaje de cada letra de la palabra
    pal = split(palabra)
    punt = 0
    try:
        window["-out-"].print("Palabra:" + palabra, text_color="black")
    except Exception:
        pass
    for x in pal:
        try:
            window["-out-"].print(
                "Letra:" + x + " Puntaje:" + datos[x], text_color="black"
            )
        except Exception:
            pass
        punt += int(datos[x])
    return punt
