import Tennis from tennis
import unittest

class TennisTest(unittest.TestCase):

	def test_peut_marquer_un_point(self):
		Match = Tennis()
		federer = Joueur("federer")
		nadal = Joueur("Nadal")

		Match.MarquerPoint(federer)

		self.assertEqual(Match.PointsDuJoueur(federer), "15");

	def test_peut_gagner_un_jeu(self):
		return 0


	def test_peut_provoquer_un_tie_break(self):
		return 0

	
	def test_peut_gagner_un_set(self):
		return 0

	def test_peut_gagner_un_match(self):
		return 0


	