package jeu;

import junit.framework.TestCase;

public class TennisTest extends TestCase
{

	Tennis jeu = new Tennis("Boris Becker", "Bjørn Borg");

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
		createScore(0, 2);

		String score = this.jeu.getScore();
		assertEquals("0,30", score);
	}

	public void testJoueur1gagneTroisPoints()
	{
		createScore(3, 0);
		String score = this.jeu.getScore();
		assertEquals("40,0", score);
	}

	public void testJoueurEgalite()
	{
		createScore(3, 3);

		String score = this.jeu.getScore();
		assertEquals("egalite", score);
	}

	public void testJoueur1GagneJeu()
	{
		createScore(4, 0);

		String score = this.jeu.getScore();
		assertEquals("Boris Becker wins", score);
	}

	public void testJoueur2GagneJeu()
	{
		createScore(1, 4);

		String score = this.jeu.getScore();
		assertEquals("Bjørn Borg wins", score);
	}

	public void testPlayersAreDuce4()
	{
		createScore(4, 4);
		String score = this.jeu.getScore();
		assertEquals("egalite", score);
	}

	public void testPlayerTwoAdvantage()
	{
		createScore(4, 5);

		String score = this.jeu.getScore();
		assertEquals("Advantage Bjørn Borg", score);
	}

	public void testPlayerOneAdvantage()
	{
		createScore(5, 4);

		String score = this.jeu.getScore();
		assertEquals("Advantage Boris Becker", score);
	}

	public void testPlayerTwoWins()
	{
		createScore(2, 4);
		String score = this.jeu.getScore();
		assertEquals("Bjørn Borg wins", score);
	}

	public void testPlayerTwoWinsAfterAdvantage()
	{
		createScore(6, 8);
		String score = this.jeu.getScore();
		assertEquals("Bjørn Borg wins", score);
	}

	public void testj1gagne()
	{
		createScore(8, 6);
		String score = this.jeu.getScore();
		assertEquals("Boris Becker wins", score);
	}

	private void createScore(final int J1, final int J2)
	{
		for (int i = 0; i < J1; i++) {
			this.jeu.j1score();
		}
		for (int i = 0; i < J2; i++) {
			this.jeu.j2score();
		}
	}

}