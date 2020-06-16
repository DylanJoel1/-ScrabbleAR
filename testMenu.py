import PySimpleGUI as sg

WIDTH  = 20
HEIGHT = 3
BUTTON_BORDER = 4
FUENTE = 'arial'

botones = [
			
			[sg.Button('JUGAR',button_color=('black','green'),size=(WIDTH, HEIGHT), border_width=BUTTON_BORDER, focus= True, font=FUENTE , key = '-comenzar-')],
			[sg.Button('Configuraciones',button_color=('black','green'), size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE     , key = '-config-')],
			[sg.Button('Cómo jugar',button_color=('black','green') ,size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE          , key = '-instrucc-')],
			[sg.Button('Top 10', button_color=('black','green'),size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE              , key = '-top10-')],
			[sg.Button('SALIR', button_color=('black','#ff4d4d'), size=(WIDTH, HEIGHT),border_width=BUTTON_BORDER,font=FUENTE,            key = '-salir-')]
]

layout = [	
			[sg.Text('Scrabble', font=('Helvetica', 20), text_color=('black'))],
			[sg.Column(botones)]
			] 

window = sg.Window('Scrabble', layout, size=(280,400))

while True:
	event, value = window.read()
	if (event is None or event == '-salir-'):
		break
	if event == '-comenzar-':
		sg.popup('comenzar')
	elif event == '-config-':
		sg.popup('configuracion')
	elif event == '-instrucc-':
		sg.popup('Instrucciones')
	elif event == '-top10-':
		sg.popup('top10')