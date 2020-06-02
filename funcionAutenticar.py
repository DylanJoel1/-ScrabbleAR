from pattern.es import parse, lexicon, split

#CONSTANTES PARA TESTEAR

TIPO= {'adj':["AO", "JJ","AQ","DI","DT"],'sus':["NC", "NN", "NCS","NCP", "NNS","NP", "NNP","W"],'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG",  "VSI","VSN", "VSP","VSS"  ]}

DIFICULTAD = 'medio'  

condicion_Dificultad = ["adj", "sus"]

#FUNCIONES
        
def es_Palabra(p):       
	if(p[0][0][0] in lexicon):
		return True
	else:
		return False



def tipo_Palabra(pal, dif, admitidos = ''):     #En la funcion analizo si la palabra existe en el diccionario, al cual accedo dependiendo la clave que le corresponde a la dificultad
	if(dif == 'facil'):	
		if(pal in str(TIPO.values())):          #pregunto si la palabra está en el diccionario de adj, sus y verb dado que la dificultad fácil admite todo
			return True
		else:
			return False
	elif(dif == 'medio'):                       #En caso de ser la dificultad "medio", pregunto por solo 2 tipo de palabras en el diccionario
		if ((pal in TIPO[admitidos[0]]) or (pal in TIPO[admitidos[1]])):
			return True
		else:
			return False
	else:                                       #En caso de ser dificil la palabra debe ser de un tipo generado aleatoriamente
		if (pal in TIPO[admitidos[0]]):
			return True
		else:
			return False
		
	
	
# "PROGRAMA PRIN"

pal = 'perro'.lower() 								 #----NOTA---- Si (pal='') tira error, siempre debe tener algo.
p=parse(pal).split()                                 #Me guardo en p la palabra junto con sus caracteristicas



if es_Palabra(p):                                                                       
	if(tipo_Palabra(p[0][0][1], DIFICULTAD, condicion_Dificultad)):        #Si la palabra existe y cumple con su condicion dependiendo su dificultad sigue el juego
		print('La palabra CUMPLE con las condiciones de la dificultad.')
	else:
		print('La palabra NO CUMPLE con las condiciones de la dificultad, implementar devolver fichas al jugador')
else:
	print('la palabra no existe, implementar devolver fichas al jugador ')
			
