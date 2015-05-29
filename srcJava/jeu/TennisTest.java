package jeu;

import junit.framework.TestCase;

public class TennisTest extends TestCase
{

	Tennis jeu = new Tennis("nadal", "federer");

	public void testNouvellePartie0Partout()
	{
		String score = this.jeu.getScore();

		assertEquals("0 partout", score);
	}

	public void testJoueur1GagnePremierPoint()
	{
		this.jeu.j1score();

		String score = this.jeu.getScore();
		assertEquals("15,0", score);
	}

	public void testJoueur2GagneDeuxPoints()
	{
		creationScore(0, 2);

		String score = this.jeu.getScore();
		assertEquals("0,30", score);
	}

	public void testJoueur1gagneTroisPoints()
	{
		creationScore(3, 0);
		String score = this.jeu.getScore();
		assertEquals("40,0", score);
	}

	public void testJoueurEgalite()
	{
		creationScore(3, 3);

		String score = this.jeu.getScore();
		assertEquals("egalite", score);
	}

	public void testJoueur1GagneJeu()
	{
		creationScore(4, 0);

		String score = this.jeu.getScore();
		assertEquals("nadal wins", score);
	}

	public void testJoueur2GagneJeu()
	{
		creationScore(1, 4);

		String score = this.jeu.getScore();
		assertEquals("federer wins", score);
	}

	public void testJoueur40Partout()
	{
		creationScore(4, 4);
		String score = this.jeu.getScore();
		assertEquals("egalite", score);
	}

	public void testJoueur2Avantage()
	{
		creationScore(4, 5);

		String score = this.jeu.getScore();
		assertEquals("Advantage federer", score);
	}

	public void testJoueur1Avantage()
	{
		creationScore(5, 4);

		String score = this.jeu.getScore();
		assertEquals("Advantage nadal", score);
	}

	public void testJoueur2Gagne()
	{
		creationScore(2, 4);
		String score = this.jeu.getScore();
		assertEquals("federer wins", score);
	}

	public void testJoueur2GagneApresAvantage()
	{
		creationScore(6, 8);
		String score = this.jeu.getScore();
		assertEquals("federer wins", score);
	}

	public void testj1gagne()
	{
		creationScore(8, 6);
		String score = this.jeu.getScore();
		assertEquals("nadal wins", score);
	}

	private void creationScore(final int J1, final int J2)
	{
		for (int i = 0; i < J1; i++) {
			this.jeu.j1score();
		}
		for (int i = 0; i < J2; i++) {
			this.jeu.j2score();
		}
	}

}