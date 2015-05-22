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

		self.assertEqual(Match.ListeDesSetsDuJoueur(federer)[0], 1)	# On vérifie la premiére case des sets, 
																	# qui correspond au nombre de jeux gagnés 
																	# dans le premier set

	def test_peut_avoir_un_avantage(self):
		federer = Joueur("federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		MarquerXPoints( Match, federer, 3)
		MarquerXPoints( Match, nadal, 4)

		self.assertEqual(Match.PointsDuJoueur(nadal), "Avantage")

	def test_peut_revenir_en_egalite(self):
		federer = Joueur("Federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		MarquerXPoints( Match, nadal, 3)
		MarquerXPoints( Match, federer, 4)
		MarquerXPoints( Match, nadal, 1)

		self.assertEqual( Match.PointsDuJoueur(nadal), "40")
		self.assertEqual( Match.PointsDuJoueur(federer), "40")

	def test_peut_gagner_un_jeu_avec_avantage(self):
		federer = Joueur("Federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		MarquerXPoints( Match, nadal, 3)
		MarquerXPoints( Match, federer, 5)

		self.assertEqual(Match.ListeDesSetsDuJoueur(federer)[0], 1)
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

		MarquerXPoints(Match, nadal, 4*5)
		MarquerXPoints(Match, federer, 4*5)
		MarquerXPoints(Match, nadal, 4)
		MarquerXPoints(Match, federer, 4) # Tie break ici

		Match.MarquerPoint(nadal) 

		self.assertEqual(Match.PointsDuJoueur(nadal), 1)

	def test_peut_gagner_un_set_simple_en_tie_break(self):
		federer = Joueur("Federer")
		nadal = Joueur("Nadal")
		Match = MatchDeTennis(federer, nadal)

		MarquerXPoints(Match, nadal, 4*5)
		MarquerXPoints(Match, federer, 4*5)
		MarquerXPoints(Match, nadal, 4)
		MarquerXPoints(Match, federer, 4) # Tie break ici

		MarquerXPoints(Match, federer, 7)

		self.assertEqual(Match.ListeDesSetsDuJoueur(federer)[0], 7)	
		self.assertEqual(Match.ListeDesSetsDuJoueur(nadal)[0], 6)


	def test_peut_gagner_un_match(self):
		return 0

def MarquerXPoints(match, joueur, nombre):
	for i in range(0, nombre):
		match.MarquerPoint(joueur)

if __name__ == '__main__':
	unittest.main()