class Ficha:
    """
    Clase que crea una ficha. La inicializa con la letra y su valor
    """

    def __init__(self, letra, fichas_punt):
        # Inicializa una ficha, con la letra (string) y el diccionario con los valores
        self.letra = letra.upper()
        self.valor = fichas_punt

    def get_valor(self):
        # Devuelve el valor de la ficha
        return self.valor

    def get_letra(self):
        # Devuelve la letra de la ficha.
        return self.letra

    def __repr__(self):
        return self.letra + "," + str(self.valor)

    def __str__(self):
        aux = self.letra + "," + str(self.valor)
        return aux
