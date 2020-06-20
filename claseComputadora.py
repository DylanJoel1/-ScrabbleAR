import itertools as it
from funcionAutenticar import confirmar_Palabra



#CONSTANTES PARA TESTEAR


DIFICULTAD = 'dificil'  

condicion_Dificultad = ["verb", "verb"]


class Computadora:
	
	def __init__(self, letras='ekigañv'):
		self.let = letras
		
	
#	def pedirFichas:

   		
	
	def crearPalabra(self):
		palabras = set()                                                   #uso un conjunto para no guardar palabras repetidas
		
		for i in range(2,len(self.let)+1):                                 #minimo las palabras son de 2 letras y va hasta n+1
			palabras.update((map("".join, it.permutations(self.let,i))))   #permutations me devuelve todas las permutaciones posibles con esas letras
		
		conj_aux= palabras.copy()										   #creo un conjunto secundario con los valores del primero								
		
		for elem in conj_aux:											   #itero con los valores del conjuto secundario asi voy borrando los elementos que no sean palabras válidas
			if ((confirmar_Palabra(elem,DIFICULTAD, condicion_Dificultad))==False):
				palabras.remove(elem)
		
		# if (palabras==none):
			# self.pedirFichas()
			
		palabra_larga = max (palabras, key =len)						   #de todas las palabras validas me quedo con la más larga dado que es la que da mayor cantidad de puntos y es más seguro que sea una palabra segura
		
		return(palabra_larga)


		
#computadora = Computadora()

#print(computadora.crearPalabra())

''' Por ahora este objeto solo posee la funcion de generar una palabra, la cual dependiendo las letras que posee la computadora genera un conjunto de las combinaciones
	posibles. En la misma funcion se llama a una funcion de un archivo que importo para devolver la palabra de las combinaciones que cumple con las condiciones del juego
	
	  
'''
