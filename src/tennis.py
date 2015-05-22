# -*- coding: utf-8 -*-

class MatchDeTennis:

	def __init__(self, joueur1, joueur2):
		self.joueur1 = joueur1
		self.joueur2 = joueur2

		self.scores = {}
		self.scores[joueur1] = Score()
		self.scores[joueur2] = Score()

	def MarquerPoint(self, joueur):
		pointsAdverses = self.scores[self.JoueurAdverse(joueur)].GetPoints()
		pointsJoueur = self.scores[joueur].GetPoints()

		# Si les deux joueurs sont a 40; le joueur qui marque passe a avantage
		if pointsAdverses == 3 and pointsJoueur == 3:
			self.scores[joueur].MarquerPoint()
			return

		# Si avantage ou déja a 40, alors on gagne 
		# ( A ce stade, l'adversaire est nécessairement en dessous de 40)
		if pointsJoueur == 4 or ( pointsJoueur == 3 and pointsAdverses < 3):
			self.scores[joueur].GagnerJeu()
			self.scores[self.JoueurAdverse(joueur)].ResetPoint()
			return

		if pointsJoueur == 3 and pointsAdverses == 4:
			self.scores[self.JoueurAdverse(joueur)].DiminuerPoint()
			return

		# Si aucun cas particulier, on marque simplement un point
		self.scores[joueur].MarquerPoint()

	def JoueurAdverse(self, joueur):
		if joueur == self.joueur1:
			return self.joueur2
		else:
			return self.joueur1

	def PointsDuJoueur(self, joueur):
		return self.scores[joueur].RepresentationPoint()

	def ListeDesSetsDuJoueur(self, joueur):
		return self.scores[joueur].ListeDesSets()


class Score:

	def __init__(self):
		self.point = 0
		self.sets = [0]
		self.tieBreak = False

	def RepresentationPoint(self):
		if self.tieBreak:
			return self.point

		if(self.point == 0):
			return "0"

		if(self.point == 1):
			return "15"

		if(self.point == 2):
			return "30"

		if(self.point == 3):
			return "40"
		
		if(self.point == 4):
			return "Avantage"

	def MarquerPoint(self):
		self.point += 1

	def DiminuerPoint(self):
		self.point -= 1

	def ResetPoint(self):
		self.point = 0

	def GetPoints(self):
		return self.point

	def SetNumero(self, X):
		return self.sets[X]

	def GagnerJeu(self):
		index_dernier_set = len(self.sets) - 1

		self.sets[index_dernier_set] += 1

		self.ResetPoint()

	def ListeDesSets(self):
		return self.sets






class Joueur:
	def __init__(self, nomDuJoueur):
		self.nom = nomDuJoueur
