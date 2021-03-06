from pattern.es import parse, lexicon, split, spelling


TIPO = {
    "adj": ["AO", "JJ", "AQ", "DI", "DT"],
    "sus": ["NC", "NN", "NCS", "NCP", "NNS", "NP", "NNP", "W"],
    "verb": [
        "VAG",
        "VBG",
        "VAI",
        "VAN",
        "MD",
        "VAS",
        "VMG",
        "VMI",
        "VB",
        "VMM",
        "VMN",
        "VMP",
        "VBN",
        "VMS",
        "VSG",
        "VSI",
        "VSN",
        "VSP",
        "VSS",
    ],
}


def es_Palabra(
    p,
):  # Funcion que pregunta si la palabra se encuentra en los diccionarios de pattern
    if p in lexicon.keys() and p in spelling.keys():
        return True
    else:
        return False


def tipo_Palabra(
    pal, dif
):  # la funcion pregunta si el tipo de palabra se encuentra en mi diccionario "TIPO", para asegurarse dependiendo de la dificultad que sea una palabra correcta
    if dif == "-facil-":
        return True
    elif (
        dif == "-medio-"
    ):  # En caso de ser la dificultad "medio", pregunto por solo 2 tipo de palabras en el diccionario
        
        if (pal in TIPO["verb"]) or (pal in TIPO["adj"]):
            return True
            
    else:  # En caso de ser dificil la palabra debe ser de un tipo generado aleatoriamente
        if (pal in TIPO["verb"]) or (pal in TIPO["adj"]):
            return True
    return False


# "PROGRAMA PRIN"


def confirmar_Palabra(pal, DIFICULTAD):
    pal = pal.lower()
    p = parse(pal).split()
    if es_Palabra(p[0][0][0]):
        if tipo_Palabra(
            p[0][0][1], DIFICULTAD
        ):  # Si la palabra existe y cumple con su condicion dependiendo su dificultad sigue el juego
            return True
    else:
        return False
        


