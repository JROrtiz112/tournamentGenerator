
"""
Proyecto: Organizador de torneos.
Programador: José Roberto Ortiz Salazar
correo: jrobertoortiz112@gmail.com
fecha: 12/16/2016
"""

import random
class Tournament:
	def __init__(self,pName,pRounds,pAmountContenders):
		self.name=pName
		self.rounds=pRounds
		self.amountContenders=pAmountContenders
		self.listContenders=[]
		self.calendar=[]

		for i in range(pRounds):
			self.calendar.append([])

	def addContestant(self,pName):
		if len(self.listContenders)<self.amountContenders:
			self.listContenders.append([pName,0,0,0,0,0,0]) #Name,Matches played,Matches won,Matches Tied,Matches lost,goals,points
			return "Jugador "+pName+" ingresado."
		else:
			return "Error: El limite de jugadores ha sido alcanzado."
	def getTournamentName(self):
		return self.name

	def getListContenders(self):
		return self.listContenders

	def getAmountContenders(self):
		return self.amountContenders

	def getTournamentInfo(self):
		return "Torneo: "+self.name+".\n"+"Cantidad de jugadores: "+str(self.amountContenders)+"\n"+"Cantidad de Rondas: "+str(self.rounds)+"\n"

	def getCalendar(self):
		return self.calendar

	def getContender(self,pName):
		for i in range(len(self.listContenders)):
			if self.listContenders[i][0]==pName:
				return self.listContenders[i]

	def getMatch(self,pLocal,pVisitor):
		for i in range(len(self.calendar)):
			for j in range(len(self.calendar[i])):
				if self.calendar[i][j][0]==pLocal and self.calendar[i][j][3]==pVisitor:
					return self.calendar[i][j]

	def generateEncounters(self):
		encounters=[]
		for i in range(len(self.listContenders)):
			for j in range(len(self.listContenders)):
				if i!=j:
					match=[self.listContenders[i][0],"NULL","NULL",self.listContenders[j][0]]
					encounters.append(match)
		return encounters

	def notSchedule(self,pMatch):
		for i in range(len(self.calendar)):
			for j in range(len(self.calendar[i])):
				if self.calendar[i][j]==pMatch:
					return False
		return True

	def nameInRound(self,pName,pRound):
		for j in range(len(self.calendar[pRound])):
			if self.calendar[pRound][j][0]==pName or self.calendar[pRound][j][3]==pName:
				return True
		return False

	def generateCalendar(self):
		matches=self.generateEncounters()
		for j in range(self.rounds):
			contendersUsed=[]
			for i in range(len(matches)):
				if len(self.calendar[j])<(self.amountContenders//2):
					if matches[i] not in self.calendar[j] and matches[i][0] not in contendersUsed and matches[i][3] not in contendersUsed and self.notSchedule(matches[i]):# and not self.nameInRound(matches[i][0],j) and not self.nameInRound(matches[i][3],j):
						contendersUsed.append(matches[i][0])
						contendersUsed.append(matches[i][3])
						self.calendar[j].append(matches[i])
		return self.calendar

	def adjustTable(self,pName,pResult,pGoals): #pResult=1 won/ 0 lost/ 2 tied
		x=self.getContender(pName)
		x[1]+=1									#Adds the played match
		x[5]+=pGoals
		if pResult==0:
			x[4]+=1
		else:
			if pResult==1:
				x[2]+=1
				x[6]+=3
			else:
				x[3]+=1
				x[6]+=1

	def determineResult(self,pLocal,pVisitor):
		if pLocal>pVisitor:
			return (1,0)
		else:
			if pLocal==pVisitor:
				return (2,2)
			else:
				return (0,1)

	def setMatch(self,pLocal,pLGoals,pVisitor,pVGoals):
		x=self.getMatch(pLocal,pVisitor)
		x[1]=pLGoals
		x[2]=pVGoals
		print(x[1],x[2])
		result=self.determineResult(pLGoals,pVGoals)
		self.adjustTable(pLocal,result[0],pLGoals-pVGoals)
		self.adjustTable(pVisitor,result[1],pVGoals-pLGoals)
		return "Marcador actualizado.\n"
	
	def burbuja(self,lista):
		for i in range(len(lista)-1):
			for j in range(len(lista)-1):
				if lista[j+1]<lista[j]:
					aux=lista[j]
					lista[j]=lista[j+1]
					lista[j+1]=aux
		return lista

	def generatePositionalTable(self):
		listScores=[]
		newListScores=[]
		for i in range(len(self.listContenders)):
			listScores.append((self.listContenders[i][6],self.listContenders[i][5],i))
			newListScores.append((self.listContenders[i][6],self.listContenders[i][5],i))
		self.burbuja(listScores)
		listScores.reverse()
		for j in range(len(listScores)):
			listScores[j]=self.listContenders[listScores[j][2]]
		return listScores