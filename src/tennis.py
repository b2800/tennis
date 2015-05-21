
class Tennis:

	def __init__(self, joueur1, joueur2):
	 	self.scores[joueur1] = Score()
	 	self.scores[joueur2] = Score()

	def MarquerPoint(self, joueur):
		self.scores[joueur].MarquerPoint()

	def PointsDuJoueur(self, joueur):
		return self.scores[joueur].RepresentationPoint()


class Score:

	def __init__(self):
	 	self.point = 0
	 	self.sets = []

	def MarquerPoint(self):
		self.point++

	def RepresentationPoint(self):
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


class Joueur:
	 def __init__(self, nomDuJoueur):
	 	self.nom = nomDuJoueur
