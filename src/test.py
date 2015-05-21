# -*- coding: utf-8 -*-

from tennis import Tennis
from tennis import Joueur
import unittest

class TennisTest(unittest.TestCase):

	def test_peut_marquer_un_point(self):

		federer = Joueur("federer")
		nadal = Joueur("Nadal")
		Match = Tennis(federer, nadal)
		
		Match.MarquerPoint(federer)

		self.assertEqual(Match.PointsDuJoueur(federer), "15")

	def test_peut_gagner_un_jeu_simple(self):

		federer = Joueur("federer")
		nadal = Joueur("Nadal")
		Match = Tennis(federer, nadal)

		Match.MarquerPoint(federer)
		Match.MarquerPoint(federer)
		Match.MarquerPoint(federer)
		Match.MarquerPoint(federer)

		self.assertEqual(Match.ListeDesSetsDuJoueur(federer)[0], 1)	# On vérifie la premiére case des sets, 
																	# qui correspond au nombre de jeux gagnés 
																	# dans le premier set

	def test_peut_marquer_un_point_en_tie_break(self):
		return 0

	
	def test_peut_gagner_un_set(self):
		return 0

	def test_peut_gagner_un_match(self):
		return 0

if __name__ == '__main__':
	unittest.main()