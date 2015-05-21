
class Tennis:

	def __init__(self, joueur1, joueur2):
		self.scores = {}
		self.joueur1 = joueur1
		self.joueur2 = joueur2

		self.scores[joueur1] = Score()
		self.scores[joueur2] = Score()

	def MarquerPoint(self, joueur):
		self.scores[joueur].MarquerPoint()

	def PointsDuJoueur(self, joueur):
		return self.scores[joueur].RepresentationPoint()

	def ListeDesSetsDuJoueur(self, joueur):
		return self.scores[joueur].ListeDesSets()

	def SetsGagnesPourLeJoueur(self, joueur):
		sets_joueur = self.scores[joueur].ListeDesSets()
		sets_opposant = self.scores[JoueurOpposant(joueur)].ListeDesSets()


	def JoueurOpposant(self, joueur):
		if joueur == self.joueur1:
			return self.joueur2
		else:
			return self.joueur1



class Score:

	def __init__(self):
		self.point = 0
		self.sets = [0]

	def MarquerPoint(self):
		self.point += 1
		if self.point == 4:
			self._GagnerJeu()
			self.point = 0

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

	def ListeDesSets(self):
		return self.sets

	def _GagnerJeu(self):
		index_dernier_set = len(self.sets) - 1
		print(index_dernier_set)
		self.sets[index_dernier_set] += 1
		print(self.sets[0])




class Joueur:
	def __init__(self, nomDuJoueur):
		self.nom = nomDuJoueur
