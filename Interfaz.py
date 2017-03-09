"""
Proyecto: Organizador de torneos.
Programador: José Roberto Ortiz Salazar
correo: jrobertoortiz112@gmail.com
fecha: 12/16/2016
"""

from classTorneo import *
import pickle

global listTournaments
listTournaments=[]

def pickTournament(pTournamentName):
	for i in range(len(listTournaments)):
		if listTournaments[i].getTournamentName()==pTournamentName:
			return listTournaments[i]

def adminTournament(pTournament):
	listOptions=["1","2","3","4","5","6","7"]
	print("Elija una opción:\n1. Agregar jugador.\n2. Generar calendario.\n3. Ver calendario\n4. Agregar marcador.\n5. Ver tabla de posiciones.\n6. Volver al menu principal\n7. Salir")
	option=input("Digite el número de la opción que desea: ")
	if option in listOptions:
		if option==listOptions[0]:
			name=input("Ingrese el nombre: ")
			print("\n"+pTournament.addContestant(name)+"\n")
			return adminTournament(pTournament)
		else:
			if option==listOptions[1]:
				pTournament.generateCalendar()
				pTournament.generateCalendar()
				print("\nCalendario generado.\n")
				return adminTournament(pTournament)
			else:
				if option==listOptions[2]:
					print("\nEncuentros:\n")
					x=pTournament.getCalendar()
					calendar=""
					for i in range(len(x)):
						for j in range(len(x[i])):
							for k in range(len(x[i][j])):
								if x[i][j][k]!="NULL":
									calendar+=str(x[i][j][k])+"\t"
								else:
									calendar+="0\t"
							calendar+="\n"
						calendar+="\n"
					print(calendar)
					return adminTournament(pTournament)
				else:
					if option==listOptions[3]:
						print("\nIngrese los siguientes datos:\n")
						w=input("Local: ")
						x=int(input("Goles: "))
						print("\n")
						y=input("Visitante: ")
						z=int(input("Goles: "))
						print("\n")
						print(pTournament.setMatch(w,x,y,z)+"\n")
						return adminTournament(pTournament)
					else:
						if option==listOptions[4]:
							x=pTournament.generatePositionalTable()
							positionalTable="\nNombre"+"\t"+"PJ"+"\t"+"PG"+"\t"+"PE"+"\t"+"PP"+"\t"+"GA"+"\t"+"GR"+"\t"+"GD"+"\t"+"PTS\n"
							for i in range(len(x)):
								for j in range(len(x[i])):
									positionalTable+=str(x[i][j])+"\t"
								positionalTable+="\n"
							print(positionalTable)
							return adminTournament(pTournament)
						else:
							if option==listOptions[5]:
								return mainMenu()
							else:
								x=input("Está seguro que desea salir? S/N: ")
								if x=="S" or x=="s":
									return 0
								else:
									if x=="N" or x=="n":
										return adminTournament(pTournament)
									else:
										print("\nError: las opciones válidas corresponden a los números del 1 al 7.\n")
										return adminTournament(pTournament)
	else:
		print("Error: las opciones válidas corresponden a los números del 1 al 4.\n")
		return adminTournament(pTournament)

def nameTaken(pTName):
	for i in range(len(listTournaments)):
		if listTournaments==pTName:
			return True
	return False

def tournamentMenu():
	print("Ingrese los siguientes datos.\n")
	tournamentName=input("Nombre del torneo: ")
	while True:
		if nameTaken(tournamentName):
			print("ERROR: El nombre ya ha sido usado.\n")
			tournamentName=input("Nombre del torneo: ")
		else:
			#return 0
			break
	amountPlayers=int(input("Cantidad de jugadores: "))
	rounds=(amountPlayers*2)-2
	tournament=Tournament(tournamentName,rounds,amountPlayers)
	listTournaments.append(tournament)
	return adminTournament(tournament)

def saveTournaments():
	file=open("torneos.txt","wb")
	pickle.dump(listTournaments,file)
	file.close()

def loadTournaments():
	file=open("torneos.txt","rb")
	listTournaments=pickle.load(file)
	file.close()

def mainMenu():
	listOptions=["1","2","3","4","5"]
	print("Elija una opción:\n1. Nuevo Torneo.\n2. Guardar Torneos.\n3. Cargar Torneos.\n4. Continuar Torneo\n5. Salir.\n")
	option=input("Digite el número de la opción que desea: ")

	if option in listOptions:
		if option==listOptions[0]:
			return tournamentMenu()
		else:
			if option==listOptions[1]:
				saveTournaments()
				mainMenu()
			else:
				if option==listOptions[2]:
					loadTournaments()
					mainMenu()
				else:
					if option==listOptions[3]:
						tournament=input("Escriba el nombre del torneo: ")
						tournament=pickTournament(tournament)
						adminTournament(tournament)
					else:
						msg=input("Está seguro que desea salir? S/N: ")
						if msg=="S" or msg=="s":
							#break
							return 0
						else:
							if msg=="N" or msg=="n":
								mainMenu()
							else:
								print("ERROR: Respuesta incorrecta, debe ingresar S o N.\n")
								mainMenu()
	else:
		print("Error: las opciones válidas corresponden a los números del 1 al 4.\n")
		return mainMenu()

mainMenu()
