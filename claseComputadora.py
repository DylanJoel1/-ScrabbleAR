from itertools import permutations
from funcionAutenticar import confirmar_Palabra
class Computadora:
	
	def __init__(self, letras='leyendo'):
		self.let = letras
		
	
#	def pedirFichas:
	
	def crearPalabra(self):
		palabras = set()                                              #uso un conjunto para no guardar palabras repetidas
		
		for i in range(2,len(self.let)+1):                              #minimo las palabras son de 2 letras y va hasta n+1
			palabras.update((map("".join, permutations(self.let,i))))   #permutations me devuelve todas las permutaciones posibles con esas letras
		
		palabras=sorted(palabras,reverse = True)                        #ordeno el conjunto de mayor a menor	
		for i in palabras:
			if (confirmar_Palabra(i)):                                  #si la funcion devuelve true entonces es una palabra válida 
				return(i)
			#else:														#---Implementar que si no encuentra ninguna palabra posible (muy poco probable), la maquina pueda perder el turno para pedir fichas
				#pedirFichas
		
		
computadora = Computadora()

print(computadora.crearPalabra())

''' Por ahora este objeto solo posee la funcion de generar una palabra, la cual dependiendo las letras que posee la computadora genera un conjunto de las combinaciones
	posibles. En la misma funcion se llama a una funcion de un archivo que importo para devolver la palabra de las combinaciones que cumple con las condiciones del juego
	
	---Por Arreglar--- El metodo sorted en teoría me lo ordena de menor a mayor, y con "reverse = True" lo doy vuelta, para quedarme con la palabra de mayor longitud ya que 
	tiene más probabilidades de que sea una palabra válida y no algo como (ejemplo) "as", pero el sorted no lo ordena del todo bien, me puede quedar algo asi: ('12345', '123', '1234','12','1')
	  
'''
