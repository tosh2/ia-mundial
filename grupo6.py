#!/usr/bin/env python3

# Grupo 8 - IA Junio 2018
# ./grupo6.py

import math

def fase_grupos(name):
	if name == "FRA": return [["AUS",2,1],["PER",1,0],["DIN",0,0]]; 	   	
	elif name == "ARG": return [["ISL",1,1],["CRO",0,3],["NIG",2,1]];

	elif name == "URU": return [["EGY",1,0],["ARA",1,0],["RUS",3,0]];		
	elif name == "POR": return [["ESP",3,3],["MAR",1,0],["IRA",1,1]];

	elif name == "ESP": return [["POR",3,3],["IRA",1,0],["MAR",2,2]];		
	elif name == "RUS": return [["ARA",5,0],["EGY",3,1],["URU",0,3]];

	elif name == "CRO": return [["NIG",2,0],["ARG",3,0],["ISL",2,1]];
	elif name == "DIN": return [["PER",1,0],["AUS",1,1],["FRA",0,0]];
	
	elif name == "BRA": return [["SUI",1,1],["COS",2,0],["SER",2,0]];
	elif name == "MEX": return [["ALE",1,0],["KOR",2,1],["SUE",0,3]];

	elif name == "BEL": return [["PAN",3,0],["TUN",5,2],["ING",1,0]];
	elif name == "JAP": return [["COL",2,1],["SEN",2,2],["POL",0,1]];

	elif name == "SUE": return [["KOR",1,0],["ALE",1,2],["MEX",3,0]];
	elif name == "SUI": return [["BRA",1,1],["SER",2,1],["COS",2,2]];

	elif name == "COL": return [["JAP",1,2],["POL",3,0],["SEN",1,0]];	
	elif name == "ING":	return [["TUN",2,0],["PAN",6,1],["BEL",0,1]];	
	
def quiniela(lista_octavos):
	lista = lista_octavos
	while lista:
		partido = lista[0]
		grupo1 = fase_grupos(partido[0])
		grupo2 = fase_grupos(partido[1])
		
		goles_a_favor_equipo1 = 0.0
		goles_a_favor_equipo2 = 0.0
		
		while(grupo1):
			goles_a_favor_equipo1 += grupo1.pop(0)[1]
			
		while(grupo2):
			goles_a_favor_equipo2 += grupo2.pop(0)[1]
		
		print(partido[0] + " " + str(int(round(goles_a_favor_equipo1/3))) +"-"+ str(int(round(goles_a_favor_equipo2/3))) + " " + partido[1])
		
		lista.pop(0)

quiniela([['FRA','ARG'],['URU','POR'],['ESP','RUS'],['CRO','DIN'],['BRA','MEX'],['BEL','JAP'],['SUE','SUI'],['COL','ING']])
	








