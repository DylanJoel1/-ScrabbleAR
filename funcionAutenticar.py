from pattern.es import parse, lexicon, split

def esPalabra(palabra):
	p = parse(palabra).split()
	for cada in p:
		for c in cada:
			if c[0] in lexicon:
				return True
			else:
				return False

pal = 'prueba'

if esPalabra(pal):
	print('pregunto qué tipo de palabra es')
else:
	print('devuelvo las fichas')
			
    
