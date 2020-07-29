import PySimpleGUI as sg
import json


def guardar (datos):
    with open('datos.json', 'w') as jsonFile:
        json.dump(datos,jsonFile)


FUENTE= "arial"

columnaf1 = [
    [sg.T("       P      C", justification="left", size=(9,1))],
    [sg.T("A", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosa", default_text="12"), sg.Input(size=(2,1), key="fcantidada")],
    [sg.T("B", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosb"), sg.Input(size=(2,1), key="fcantidadb")],
    [sg.T("C", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosc"), sg.Input(size=(2,1), key="fcantidadc")],
    [sg.T("D", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosd"), sg.Input(size=(2,1), key="fcantidadd")],
    [sg.T("E", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntose"), sg.Input(size=(2,1), key="fcantidade")],
    [sg.T("F", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosf"), sg.Input(size=(2,1), key="fcantidadf")],
    [sg.T("G", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosg"), sg.Input(size=(2,1), key="fcantidadg")],
    [sg.T("H", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosh"), sg.Input(size=(2,1), key="fcantidadh")],
    [sg.T("I", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosi"), sg.Input(size=(2,1), key="fcantidadi")],
    [sg.T("J", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosj"), sg.Input(size=(2,1), key="fcantidadj")],
    [sg.T("K", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosk"), sg.Input(size=(2,1), key="fcantidadk")],
    [sg.T("L", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosl"), sg.Input(size=(2,1), key="fcantidadl")],
    [sg.T("LL", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosll"), sg.Input(size=(2,1), key="fcantidadll")],
    [sg.T("M", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosm"), sg.Input(size=(2,1), key="fcantidadm")]
    
]

columnaf2 = [
    [sg.T("       P      C", justification="left", size=(9,1))],
    [sg.T("N", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosn"), sg.Input(size=(2,1), key="fcantidadn")],
    [sg.T("Ñ", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosñ"), sg.Input(size=(2,1), key="fcantidadñ")],
    [sg.T("O", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntoso"), sg.Input(size=(2,1), key="fcantidado")],
    [sg.T("P", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosp"), sg.Input(size=(2,1), key="fcantidadp")],
    [sg.T("Q", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosq"), sg.Input(size=(2,1), key="fcantidadq")],
    [sg.T("R", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosr"), sg.Input(size=(2,1), key="fcantidadr")],
    [sg.T("S", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntoss"), sg.Input(size=(2,1), key="fcantidads")],
    [sg.T("T", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntost"), sg.Input(size=(2,1), key="fcantidadt")],
    [sg.T("U", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosu"), sg.Input(size=(2,1), key="fcantidadu")],
    [sg.T("V", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosv"), sg.Input(size=(2,1), key="fcantidadv")],
    [sg.T("W", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosw"), sg.Input(size=(2,1), key="fcantidadw")],
    [sg.T("X", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosx"), sg.Input(size=(2,1), key="fcantidadx")],
    [sg.T("Y", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosy"), sg.Input(size=(2,1), key="fcantidady")],
    [sg.T("Z", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosz"), sg.Input(size=(2,1), key="fcantidadz")]
]

columnam1 = [
    [sg.T("       P      C", justification="left", size=(9,1))],
    [sg.T("A", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosa"), sg.Input(size=(2,1), key="mcantidada")],
    [sg.T("B", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosb"), sg.Input(size=(2,1), key="mcantidadb")],
    [sg.T("C", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosc"), sg.Input(size=(2,1), key="mcantidadc")],
    [sg.T("D", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosd"), sg.Input(size=(2,1), key="mcantidadd")],
    [sg.T("E", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntose"), sg.Input(size=(2,1), key="mcantidade")],
    [sg.T("F", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosf"), sg.Input(size=(2,1), key="mcantidadf")],
    [sg.T("G", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosg"), sg.Input(size=(2,1), key="mcantidadg")],
    [sg.T("H", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosh"), sg.Input(size=(2,1), key="mcantidadh")],
    [sg.T("I", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosi"), sg.Input(size=(2,1), key="mcantidadi")],
    [sg.T("J", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosj"), sg.Input(size=(2,1), key="mcantidadj")],
    [sg.T("K", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosk"), sg.Input(size=(2,1), key="mcantidadk")],
    [sg.T("L", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosl"), sg.Input(size=(2,1), key="mcantidadl")],
    [sg.T("LL", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosll"), sg.Input(size=(2,1), key="mcantidadll")],
    [sg.T("M", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosm"), sg.Input(size=(2,1), key="mcantidadm")]
    
]

columnam2 = [
    [sg.T("       P      C", justification="left", size=(9,1))],
    [sg.T("N", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosn"), sg.Input(size=(2,1), key="mcantidadn")],
    [sg.T("Ñ", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosñ"), sg.Input(size=(2,1), key="mcantidadñ")],
    [sg.T("O", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntoso"), sg.Input(size=(2,1), key="mcantidado")],
    [sg.T("P", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosp"), sg.Input(size=(2,1), key="mcantidadp")],
    [sg.T("Q", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosq"), sg.Input(size=(2,1), key="mcantidadq")],
    [sg.T("R", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosr"), sg.Input(size=(2,1), key="mcantidadr")],
    [sg.T("S", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntoss"), sg.Input(size=(2,1), key="mcantidads")],
    [sg.T("T", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntost"), sg.Input(size=(2,1), key="mcantidadt")],
    [sg.T("U", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosu"), sg.Input(size=(2,1), key="mcantidadu")],
    [sg.T("V", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosv"), sg.Input(size=(2,1), key="mcantidadv")],
    [sg.T("W", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosw"), sg.Input(size=(2,1), key="mcantidadw")],
    [sg.T("X", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosx"), sg.Input(size=(2,1), key="mcantidadx")],
    [sg.T("Y", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosy"), sg.Input(size=(2,1), key="mcantidady")],
    [sg.T("Z", justification="left", size=(2,1)), sg.Input(size=(2,1), key="mpuntosz"), sg.Input(size=(2,1), key="mcantidadz")]
]

columnad1 = [
    [sg.T("       P      C", justification="left", size=(9,1))],
    [sg.T("A", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosa"), sg.Input(size=(2,1), key="dcantidada")],
    [sg.T("B", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosb"), sg.Input(size=(2,1), key="dcantidadb")],
    [sg.T("C", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosc"), sg.Input(size=(2,1), key="dcantidadc")],
    [sg.T("D", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosd"), sg.Input(size=(2,1), key="dcantidadd")],
    [sg.T("E", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntose"), sg.Input(size=(2,1), key="dcantidade")],
    [sg.T("F", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosf"), sg.Input(size=(2,1), key="dcantidadf")],
    [sg.T("G", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosg"), sg.Input(size=(2,1), key="dcantidadg")],
    [sg.T("H", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosh"), sg.Input(size=(2,1), key="dcantidadh")],
    [sg.T("I", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosi"), sg.Input(size=(2,1), key="dcantidadi")],
    [sg.T("J", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosj"), sg.Input(size=(2,1), key="dcantidadj")],
    [sg.T("K", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosk"), sg.Input(size=(2,1), key="dcantidadk")],
    [sg.T("L", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosl"), sg.Input(size=(2,1), key="dcantidadl")],
    [sg.T("LL", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosll"), sg.Input(size=(2,1), key="dcantidadll")],
    [sg.T("M", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosm"), sg.Input(size=(2,1), key="dcantidadm")]
    
]

columnad2 = [
    [sg.T("       P      C", justification="left", size=(9,1))],
    [sg.T("N", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosn"), sg.Input(size=(2,1), key="dcantidadn")],
    [sg.T("Ñ", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosñ"), sg.Input(size=(2,1), key="dcantidadñ")],
    [sg.T("O", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntoso"), sg.Input(size=(2,1), key="dcantidado")],
    [sg.T("P", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosp"), sg.Input(size=(2,1), key="dcantidadp")],
    [sg.T("Q", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosq"), sg.Input(size=(2,1), key="dcantidadq")],
    [sg.T("R", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosr"), sg.Input(size=(2,1), key="dcantidadr")],
    [sg.T("S", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntoss"), sg.Input(size=(2,1), key="dcantidads")],
    [sg.T("T", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntost"), sg.Input(size=(2,1), key="dcantidadt")],
    [sg.T("U", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosu"), sg.Input(size=(2,1), key="dcantidadu")],
    [sg.T("V", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosv"), sg.Input(size=(2,1), key="dcantidadv")],
    [sg.T("W", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosw"), sg.Input(size=(2,1), key="dcantidadw")],
    [sg.T("X", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosx"), sg.Input(size=(2,1), key="dcantidadx")],
    [sg.T("Y", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosy"), sg.Input(size=(2,1), key="dcantidady")],
    [sg.T("Z", justification="left", size=(2,1)), sg.Input(size=(2,1), key="dpuntosz"), sg.Input(size=(2,1), key="dcantidadz")]
]

facil_layout = [
    [sg.T("Facil", justification="center", font=(FUENTE,20), size=(55,1),background_color="#00FFFF",text_color="#000080")],
    [sg.Column(columnaf1), sg.Column(columnaf2)]
]

medio_layout = [
    [sg.T("Medio", justification="center", font=(FUENTE,20), size=(55,1),background_color="#00FFFF",text_color="#000080" )],
    [sg.Column(columnam1), sg.Column(columnam2)]
]

dificil_layout = [
    [sg.T("Dificil", justification="center", font=(FUENTE,20), size=(55,1),background_color="#00FFFF",text_color="#000080" )],
    [sg.Column(columnad1), sg.Column(columnad2)]
]

layout_Config = [	
			[sg.T("Configuración", justification="center", font=(FUENTE,20), size=(55,1),background_color="#00FFFF",text_color="#000080" )],
			[sg.TabGroup([[sg.Tab('Facil', facil_layout), sg.Tab('Medio', medio_layout), sg.Tab('Dificil', dificil_layout)]])],
			[sg.B("Guardar", size=(8,2), key="-guardar-", button_color=("black","#FA8072")), sg.B("Volver", size=(8,2), key="-volver-", button_color=("black","#FA8072"))]
			
			]

window= sg.Window("Configuracion",layout_Config)

def Config():
    while True:
        event, values = window.read()
        if (event is None or event == '-salir-'):
            break
        if event == '-guardar-':
            datos = {
                'dpuntosa' : values['dpuntosa'], 'dpuntosb' : values['dpuntosb'], 'dpuntosc' : values['dpuntosc'], 'dpuntosd' : values['dpuntosd'],
                'dpuntose' : values['dpuntose'], 'dpuntosf' : values['dpuntosf'], 'dpuntosg' : values['dpuntosg'], 'dpuntosh' : values['dpuntosh'], 'dpuntosi' : values['dpuntosi'], 
                'dpuntosj' : values['dpuntosj'], 'dpuntosk' : values['dpuntosk'], 'dpuntosl' : values['dpuntosl'], 'dpuntosll' : values['dpuntosll'], 'dpuntosm' : values['dpuntosm'], 
                'dpuntosn' : values['dpuntosn'], 'dpuntosñ' : values['dpuntosñ'], 'dpuntoso' : values['dpuntoso'], 'dpuntosp' : values['dpuntosp'], 'dpuntosq' : values['dpuntosq'], 
                'dpuntosr' : values['dpuntosr'], 'dpuntoss' : values['dpuntoss'], 'dpuntost' : values['dpuntost'], 'dpuntosu' : values['dpuntosu'], 'dpuntosv' : values['dpuntosv'], 
                'dpuntosw' : values['dpuntosw'], 'dpuntosx' : values['dpuntosx'], 'dpuntosy' : values['dpuntosy'], 'dpuntosz' : values['dpuntosz'], 

                'dcantidada' : values['dcantidada'], 'dcantidadb' : values['dcantidadb'], 'dcantidadc' : values['dcantidadc'], 'dcantidadd' : values['dcantidadd'], 
                'dcantidade' : values['dcantidade'], 'dcantidadf' : values['dcantidadf'], 'dcantidadg' : values['dcantidadg'], 'dcantidadh' : values['dcantidadh'], 'dcantidadi' : values['dcantidadi'], 
                'dcantidadj' : values['dcantidadj'], 'dcantidadk' : values['dcantidadk'], 'dcantidadl' : values['dcantidadl'], 'dcantidadll' : values['dcantidadll'], 'dcantidadm' : values['dcantidadm'], 
                'dcantidadn' : values['dcantidadn'], 'dcantidadñ' : values['dcantidadñ'], 'dcantidado' : values['dcantidado'], 'dcantidadp' : values['dcantidadp'], 'dcantidadq' : values['dcantidadq'], 
                'dcantidadr' : values['dcantidadr'], 'dcantidads' : values['dcantidads'], 'dcantidadt' : values['dcantidadt'], 'dcantidadu' : values['dcantidadu'], 'dcantidadv' : values['dcantidadv'], 
                'dcantidadw' : values['dcantidadw'], 'dcantidadx' : values['dcantidadx'], 'dcantidady' : values['dcantidady'], 'dcantidadz' : values['dcantidadz'],


                'fpuntosa' : values['fpuntosa'], 'fpuntosb' : values['fpuntosb'], 'fpuntosc' : values['fpuntosc'], 'fpuntosd' : values['fpuntosd'], 
                'fpuntose' : values['fpuntose'], 'fpuntosf' : values['fpuntosf'], 'fpuntosg' : values['fpuntosg'], 'fpuntosh' : values['fpuntosh'], 'fpuntosi' : values['fpuntosi'], 
                'fpuntosj' : values['fpuntosj'], 'fpuntosk' : values['fpuntosk'], 'fpuntosl' : values['fpuntosl'], 'fpuntosll' : values['fpuntosll'], 'fpuntosm' : values['fpuntosm'], 
                'fpuntosn' : values['fpuntosn'], 'fpuntosñ' : values['fpuntosñ'], 'fpuntoso' : values['fpuntoso'], 'fpuntosp' : values['fpuntosp'], 'fpuntosq' : values['fpuntosq'], 
                'fpuntosr' : values['fpuntosr'], 'fpuntoss' : values['fpuntoss'], 'fpuntost' : values['fpuntost'], 'fpuntosu' : values['fpuntosu'], 'fpuntosv' : values['fpuntosv'], 
                'fpuntosw' : values['fpuntosw'], 'fpuntosx' : values['fpuntosx'], 'fpuntosy' : values['fpuntosy'], 'fpuntosz' : values['fpuntosz'], 

                'fcantidada' : values['fcantidada'], 'fcantidadb' : values['fcantidadb'], 'fcantidadc' : values['fcantidadc'], 'fcantidadd' : values['fcantidadd'], 
                'fcantidade' : values['fcantidade'], 'fcantidadf' : values['fcantidadf'], 'fcantidadg' : values['fcantidadg'], 'fcantidadh' : values['fcantidadh'], 'fcantidadi' : values['fcantidadi'], 
                'fcantidadj' : values['fcantidadj'], 'fcantidadk' : values['fcantidadk'], 'fcantidadl' : values['fcantidadl'], 'fcantidadll' : values['fcantidadll'], 'fcantidadm' : values['fcantidadm'], 
                'fcantidadn' : values['fcantidadn'], 'fcantidadñ' : values['fcantidadñ'], 'fcantidado' : values['fcantidado'], 'fcantidadp' : values['fcantidadp'], 'fcantidadq' : values['fcantidadq'], 
                'fcantidadr' : values['fcantidadr'], 'fcantidads' : values['fcantidads'], 'fcantidadt' : values['fcantidadt'], 'fcantidadu' : values['fcantidadu'], 'fcantidadv' : values['fcantidadv'], 
                'fcantidadw' : values['fcantidadw'], 'fcantidadx' : values['fcantidadx'], 'fcantidady' : values['fcantidady'], 'fcantidadz' : values['fcantidadz'],


                'mpuntosa' : values['mpuntosa'], 'mpuntosb' : values['mpuntosb'], 'mpuntosc' : values['mpuntosc'], 'mpuntosd' : values['mpuntosd'], 
                'mpuntose' : values['mpuntose'], 'mpuntosf' : values['mpuntosf'], 'mpuntosg' : values['mpuntosg'], 'mpuntosh' : values['mpuntosh'], 'mpuntosi' : values['mpuntosi'], 
                'mpuntosj' : values['mpuntosj'], 'mpuntosk' : values['mpuntosk'], 'mpuntosl' : values['mpuntosl'], 'mpuntosll' : values['mpuntosll'], 'mpuntosm' : values['mpuntosm'], 
                'mpuntosn' : values['mpuntosn'], 'mpuntosñ' : values['mpuntosñ'], 'mpuntoso' : values['mpuntoso'], 'mpuntosp' : values['mpuntosp'], 'mpuntosq' : values['mpuntosq'], 
                'mpuntosr' : values['mpuntosr'], 'mpuntoss' : values['mpuntoss'], 'mpuntost' : values['mpuntost'], 'mpuntosu' : values['mpuntosu'], 'mpuntosv' : values['mpuntosv'], 
                'mpuntosw' : values['mpuntosw'], 'mpuntosx' : values['mpuntosx'], 'mpuntosy' : values['mpuntosy'], 'mpuntosz' : values['mpuntosz'], 

                'mcantidada' : values['mcantidada'], 'mcantidadb' : values['mcantidadb'], 'mcantidadc' : values['mcantidadc'], 'mcantidadd' : values['mcantidadd'], 
                'mcantidade' : values['mcantidade'], 'mcantidadf' : values['mcantidadf'], 'mcantidadg' : values['mcantidadg'], 'mcantidadh' : values['mcantidadh'], 'mcantidadi' : values['mcantidadi'], 
                'mcantidadj' : values['mcantidadj'], 'mcantidadk' : values['mcantidadk'], 'mcantidadl' : values['mcantidadl'], 'mcantidadll' : values['mcantidadll'], 'mcantidadm' : values['mcantidadm'], 
                'mcantidadn' : values['mcantidadn'], 'mcantidadñ' : values['mcantidadñ'], 'mcantidado' : values['mcantidado'], 'mcantidadp' : values['mcantidadp'], 'mcantidadq' : values['mcantidadq'], 
                'mcantidadr' : values['mcantidadr'], 'mcantidads' : values['mcantidads'], 'mcantidadt' : values['mcantidadt'], 'mcantidadu' : values['mcantidadu'], 'mcantidadv' : values['mcantidadv'], 
                'mcantidadw' : values['mcantidadw'], 'mcantidadx' : values['mcantidadx'], 'mcantidady' : values['mcantidady'], 'mcantidadz' : values['mcantidadz']

            }
            guardar(datos)
    window.close