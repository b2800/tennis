# -*- coding: utf-8 -*-

# jbdusseaut@arpinum.fr

from tennis import MatchDeTennis
from tennis import Joueur
import unittest

class TennisTest(unittest.TestCase):

	def test_peut_marquer_un_point(self):
		federer = Joueur("federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		Match.MarquerPoint(federer)
		self.assertEqual(Match.PointsDuJoueur(federer), "15")

	def test_peut_gagner_un_jeu_simple(self):
		federer = Joueur("federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		MarquerXPoints( Match, federer, 4)

		# On vérifie que federer a bien gagné 1 jeu lors du premier set
		self.assertEqual(Match.SetNumeroXDuJoueur(federer, 1), 1)	

	def test_peut_avoir_un_avantage(self):
		federer = Joueur("federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		MarquerXPoints(Match, federer, 3)
		MarquerXPoints(Match, nadal, 4)

		self.assertEqual(Match.PointsDuJoueur(nadal), "Avantage")

	def test_peut_revenir_en_egalite(self):
		federer = Joueur("Federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		MarquerXPoints(Match, nadal, 3)
		MarquerXPoints(Match, federer, 4)
		MarquerXPoints(Match, nadal, 1)

		self.assertEqual(Match.PointsDuJoueur(nadal), "40")
		self.assertEqual(Match.PointsDuJoueur(federer), "40")

	def test_peut_gagner_un_jeu_avec_avantage(self):
		federer = Joueur("Federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		MarquerXPoints(Match, nadal, 3)
		MarquerXPoints(Match, federer, 5)

		self.assertEqual(Match.SetNumeroXDuJoueur(federer, 1), 1)
		self.assertEqual(Match.PointsDuJoueur(federer), "0")
		self.assertEqual(Match.PointsDuJoueur(nadal), "0")

	def test_peut_gagner_un_set_simple(self):
		federer = Joueur("Federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		MarquerXPoints( Match, nadal, 4*6)

		self.assertEqual(Match.NombreSetsGagnesDuJoueur(nadal), 1)

	def test_peut_marquer_un_point_en_tie_break(self):
		federer = Joueur("Federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		self.ProvoquerUnTieBreak(Match, nadal, federer)

		Match.MarquerPoint(nadal) 

		# En tie break, marquer une fois correspond a 1 point et non a 15 
		self.assertEqual(Match.PointsDuJoueur(nadal), 1)

	def test_peut_gagner_un_set_simple_en_tie_break(self):
		federer = Joueur("Federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		self.ProvoquerUnTieBreak(Match, nadal, federer)

		MarquerXPoints(Match, federer, 7)

		self.assertEqual(Match.ListeDesSetsDuJoueur(federer)[0], 7)	
		self.assertEqual(Match.ListeDesSetsDuJoueur(nadal)[0], 6)

	def test_peut_gagner_un_set_long_en_tie_break(self):
		federer = Joueur("Federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		self.ProvoquerUnTieBreak(Match, nadal, federer)

		MarquerXPoints(Match, federer, 6)	# 6-0
		MarquerXPoints(Match, nadal, 7)		# 6-7
		MarquerXPoints(Match, federer, 2)	# 8-7
		MarquerXPoints(Match, nadal, 3)		# 8-10

		self.assertEqual(Match.ListeDesSetsDuJoueur(federer)[0], 6)	
		self.assertEqual(Match.ListeDesSetsDuJoueur(nadal)[0], 7)

	def test_peut_gagner_un_match_simple(self):

		federer = Joueur("Federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)
 
		# Gagne 3 sets
		MarquerXPoints(Match, nadal, 4*6)
		MarquerXPoints(Match, nadal, 4*6)
		MarquerXPoints(Match, nadal, 4*6)

		self.assertEqual(Match.GetGagnant(), nadal)

	def test_peut_gagner_un_match_avec_tie_break(self):
		federer = Joueur("Federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		MarquerXPoints(Match, nadal, 4*6) # Gagne un set normal
		self.ProvoquerUnTieBreak(Match, nadal, federer)
		MarquerXPoints(Match, nadal, 7) #Gagne le set en Tie-Break
		MarquerXPoints(Match, nadal, 4*6) # Gagne un set normal

		self.assertEqual(Match.GetGagnant(), nadal)

	# Attention, ne fonctionne qu'au tout début d'un set quand personne 
	# n'a encore marqué de points 
	def ProvoquerUnTieBreak(self, match, joueur1, joueur2):
		MarquerXPoints(match, joueur1, 4*5)
		MarquerXPoints(match, joueur2, 4*5)
		MarquerXPoints(match, joueur1, 4)
		MarquerXPoints(match, joueur2, 4) # Tie break ici

		# Les deux joueurs doivent avoir gagné 6 jeux au dernier set pour être en tie-break
		self.assertEqual(match.ListeDesSetsDuJoueur(joueur1)[-1], 6)
		self.assertEqual(match.ListeDesSetsDuJoueur(joueur2)[-1], 6)

def MarquerXPoints(match, joueur, nombre):
	for i in range(0, nombre):
		match.MarquerPoint(joueur)

if __name__ == '__main__':
	unittest.main()