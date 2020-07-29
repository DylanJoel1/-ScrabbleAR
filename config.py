import PySimpleGUI as sg

FUENTE= "arial"

columnaf1 = [
    [sg.T("       P      C", justification="left", size=(9,1))],
    [sg.T("A", justification="left", size=(2,1)), sg.Input(size=(2,1), key="fpuntosa"), sg.Input(size=(2,1), key="fcantidada")],
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
			[sg.B("Volver", size=(8,2), key="-volver-", button_color=("black","#FA8072"))]
			
			]

window= sg.Window("Configuracion",layout_Config)

def Config():
	event, value = window.read()
	window.close()