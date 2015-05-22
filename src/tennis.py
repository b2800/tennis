# -*- coding: utf-8 -*-

class MatchDeTennis:

	def __init__(self, joueur1, joueur2):
		self.joueur1 = joueur1
		self.joueur2 = joueur2

		self.scores = {}
		self.scores[joueur1] = Score()
		self.scores[joueur2] = Score()

	def MarquerPoint(self, joueur):
		if self.scores[joueur].GetTieBreak():
			self._MarquerPointEnTieBreak(joueur)
			return

		pointsAdverses = self.scores[self.JoueurAdverse(joueur)].GetPoints()
		pointsJoueur = self.scores[joueur].GetPoints()

		# Si les deux joueurs sont a 40; le joueur qui marque passe a avantage
		if pointsAdverses == 3 and pointsJoueur == 3:
			self.scores[joueur].MarquerPoint()
			return

		# Si avantage ou déja a 40, alors on gagne 
		# ( A ce stade, l'adversaire est nécessairement en dessous de 40)
		if pointsJoueur == 4 or ( pointsJoueur == 3 and pointsAdverses < 3):
			self._GagnerJeu(joueur)
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

	def NombreSetsGagnesDuJoueur(self, joueur):
		nb = 0
		nb_sets_joues = len(self.scores[joueur].ListeDesSets())

		for i in range(0, nb_sets_joues):
			jeux_joueur = self.scores[joueur].ListeDesSets()[i]
			jeux_adverse = self.scores[self.JoueurAdverse(joueur)].ListeDesSets()[i]

			if jeux_adverse == 6 or jeux_joueur == 6:
				if jeux_joueur - jeux_adverse >= 2:
					nb += 1

			if jeux_joueur == 7:
				nb += 1
		return nb

	def SetTieBreak(self, value):
		self.scores[self.joueur1].SetTieBreak(True)
		self.scores[self.joueur2].SetTieBreak(True)

	def _MarquerPointEnTieBreak(self, joueur):

		self.scores[joueur].MarquerPoint()

		pointsJoueur = self.scores[joueur].GetPoints()
		pointsAdverse = self.scores[self.JoueurAdverse(joueur)].GetPoints()

		if pointsJoueur >= 7 and ( (pointsJoueur - pointsAdverse) >= 2):
			self.scores[joueur].GagnerJeu()
			self.scores[self.JoueurAdverse(joueur)].ResetPoint()
			return

		

	def _GagnerJeu(self, joueur):
		self.scores[joueur].GagnerJeu()
		sets_gagnes = self.scores[joueur].ListeDesSets()[-1] # Dernier element
		sets_gagnes_joueur_adverse = self.scores[self.JoueurAdverse(joueur)].ListeDesSets()[-1]

		if sets_gagnes == 6 and sets_gagnes_joueur_adverse == 6:
			self.SetTieBreak(True)



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
		self.sets[-1] += 1 # Incrémente le dernier set en cours
		self.ResetPoint()

	def ListeDesSets(self):
		return self.sets

	def SetTieBreak(self, value):
		self.tieBreak = value

	def GetTieBreak(self):
		return self.tieBreak






class Joueur:
	def __init__(self, nomDuJoueur):
		self.nom = nomDuJoueur
