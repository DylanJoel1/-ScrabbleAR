from pattern.es import parse, lexicon, split,spelling


TIPO= {'adj':["AO", "JJ","AQ","DI","DT"],'sus':["NC", "NN", "NCS","NCP", "NNS","NP", "NNP","W"],'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG",  "VSI","VSN", "VSP","VSS"  ]}


#FUNCIONES
        
def es_Palabra(p):       
	if(p[0][0][0] in lexicon.keys() and p[0][0][0] in spelling.keys()):
		return True
	else:
		return False



def tipo_Palabra(pal, dif, admitidos = ''):     #En la funcion analizo si la palabra existe en el diccionario, al cual accedo dependiendo la clave que le corresponde a la dificultad
	if(dif == 'facil'):
		return True
	elif(dif == 'medio'):                       #En caso de ser la dificultad "medio", pregunto por solo 2 tipo de palabras en el diccionario
		if ((pal in TIPO[admitidos[0]]) or (pal in TIPO[admitidos[1]])):
			return True
	else:                                       #En caso de ser dificil la palabra debe ser de un tipo generado aleatoriamente
		if (pal in TIPO[admitidos[0]]):
			return True
	return False
		
	
	
# "PROGRAMA PRIN"



def confirmar_Palabra(pal, DIFICULTAD, condicion_Dificultad):
	pal = pal.lower() 								 #----NOTA---- Si (pal='') tira error, siempre debe tener algo.
	p=parse(pal).split()
	if es_Palabra(p):                                                                     
		if(tipo_Palabra(p[0][0][1], DIFICULTAD, condicion_Dificultad)):        #Si la palabra existe y cumple con su condicion dependiendo su dificultad sigue el juego
			return True
	else:
		return False
	

			
