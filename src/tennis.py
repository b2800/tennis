# -*- coding: utf-8 -*-

class MatchDeTennis:

	def __init__(self, joueur1, joueur2):
		self.joueur1 = joueur1
		self.joueur2 = joueur2
		self.gagnant = None

		self.scores = {}
		self.scores[joueur1] = Score()
		self.scores[joueur2] = Score()

	# /!\ 
	# La SEULE fonction a appeler de l'exterieur pour modifier le score.
	# Fait marquer au joueur donné un point, et fait les calculs nécessaires 
	# automatiquement.
	def MarquerPoint(self, joueur):
		if self.scores[joueur].GetTieBreak():
			self._MarquerPointEnTieBreak(joueur)
			return

		pointsAdverses = self.scores[self.JoueurAdverse(joueur)].GetPoints()
		pointsJoueur = self.scores[joueur].GetPoints()

		# Si avantage ou déja a 40, alors on gagne le jeu
		if pointsJoueur == 4 or ( pointsJoueur == 3 and pointsAdverses < 3):
			self._GagnerJeu(joueur)
			return

		# Si l'on est a 40 et l'adversaire a Avantage, on retourne a 40 - 40
		if pointsJoueur == 3 and pointsAdverses == 4:
			self.scores[self.JoueurAdverse(joueur)].DiminuerPoint()
			return

		# Si aucun cas particulier, on marque simplement un point
		self.scores[joueur].MarquerPoint()

	def PointsDuJoueur(self, joueur):
		return self.scores[joueur].RepresentationPoint()

	# Retourne le nombre de jeux gagnés dans chaque sets sous forme de tableau
	def ListeDesSetsDuJoueur(self, joueur):
		return self.scores[joueur].ListeDesSets()

	# Retourne le nombre de jeux gagnés dans le set demandé
	def SetNumeroXDuJoueur(self, joueur, n_set):
		return self.scores[joueur].ListeDesSets()[n_set-1]

	# Retourne le gagnant du match, ou None si le match n'est pas encore terminé
	def GetGagnant(self):
		return self.gagnant

	# Retourne le nombre de sets que le joueur ciblé à gagné. 
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

	## Fonctions utilitaires :
	## Ces fonctions n'ont aucun interet en dehors de cette classe
	## A n'utiliser qu'en interne uniquement	

	def _SetTieBreak(self, value):
		self.scores[self.joueur1].SetTieBreak(value)
		self.scores[self.joueur2].SetTieBreak(value)

	# Marque un point suivant les régles du Tie break. A ne pas appeler soi meme ! 
	def _MarquerPointEnTieBreak(self, joueur):
		self.scores[joueur].MarquerPoint()

		pointsJoueur = self.scores[joueur].GetPoints()
		pointsAdverse = self.scores[self.JoueurAdverse(joueur)].GetPoints()

		if pointsJoueur >= 7 and ( (pointsJoueur - pointsAdverse) >= 2):
			self._GagnerJeu(joueur)
			return

	# Modifie le nombre de jeux gagnés du joueur concerné pour ce set.
	# /!\ A ne pas appeler soi même
	def _GagnerJeu(self, joueur):
		self.scores[joueur].GagnerJeu()
		self.scores[self.JoueurAdverse(joueur)].ResetPoint()

		jeux_gagnes = self.scores[joueur].ListeDesSets()[-1] # Dernier element
		jeux_gagnes_joueur_adverse = self.scores[self.JoueurAdverse(joueur)].ListeDesSets()[-1]

		if jeux_gagnes == 6 and jeux_gagnes_joueur_adverse == 6:
			self._SetTieBreak(True)

		if (jeux_gagnes == 6 and jeux_gagnes_joueur_adverse < 5) or jeux_gagnes == 7:
			if not self._VerifierSiGagnant():
				self.scores[joueur].NotifierSetSuivant()
				self.scores[self.JoueurAdverse(joueur)].NotifierSetSuivant()
				self._SetTieBreak(False)

	# Retourne le joueur adverse du joueur donné en paramétre
	def JoueurAdverse(self, joueur):
		if joueur == self.joueur1:
			return self.joueur2
		else:
			return self.joueur1
	
	# Compare les scores afin de déterminer s'il y a eu un gagnant.
	# Appelé automatiquement a chaque fois qu'un set est potentiellement gagné.
	def _VerifierSiGagnant(self):
		nb_sets_joueur1 = self.NombreSetsGagnesDuJoueur(self.joueur1)
		nb_sets_joueur2 = self.NombreSetsGagnesDuJoueur(self.joueur2)

		if nb_sets_joueur1 == 3:
			self.gagnant = self.joueur1

		elif nb_sets_joueur2 == 3:
			self.gagnant = self.joueur2

		# Retourne True s'il y a eu un gagnant, False sinon
		return self.gagnant is not None


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

	def GagnerJeu(self):
		self.sets[-1] += 1 # Incrémente le dernier set en cours
		self.ResetPoint()

	def NotifierSetSuivant(self):
		self.sets.append(0)
		self.point = 0
		self.SetTieBreak(False)

	def ListeDesSets(self):
		return self.sets

	def SetTieBreak(self, value):
		self.tieBreak = value

	def GetTieBreak(self):
		return self.tieBreak


# Stocke les informations sur le joueur. Ici, uniquement le nom mais on pourrait
# imaginer par la suite un développement plus important.
class Joueur:
	def __init__(self, nomDuJoueur):
		self.nom = nomDuJoueur
