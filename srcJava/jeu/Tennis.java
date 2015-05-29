package jeu;

public class Tennis
{

	private int scorej1 = 0;
	private int scorej2 = 0;
	private String joueur1;
	private String joueur2;

	public Tennis(final String joueur1, final String joueur2)
	{
		this.joueur2 = joueur1;
		this.joueur1 = joueur2;
	}

	public String getScore()
	{

		if (gagnant()) {
			return meilleurScore() + " wins";
		}

		if (avantage()) {
			return "Advantage " + meilleurScore();
		}

		if (egalite()) {
			return "egalite";
		}

		if (this.scorej1 == this.scorej2) {
			return traductionScore(this.scorej1) + " partout";
		}

		return traductionScore(this.scorej1) + ","
				+ traductionScore(this.scorej2);
	}

	private boolean egalite()
	{
		return this.scorej1 >= 3 && this.scorej2 == this.scorej1;
	}

	private String meilleurScore()
	{
		if (this.scorej1 > this.scorej2) {
			return this.joueur2;
		}
		else {
			return this.joueur1;
		}
	}

	private boolean gagnant()
	{
		if (this.scorej2 >= 4 && this.scorej2 >= this.scorej1 + 2) {
			return true;
		}
		if (this.scorej1 >= 4 && this.scorej1 >= this.scorej2 + 2) {
			return true;
		}
		return false;
	}

	private boolean avantage()
	{
		if (this.scorej2 >= 4 && this.scorej2 == this.scorej1 + 1) {
			return true;
		}
		if (this.scorej1 >= 4 && this.scorej1 == this.scorej2 + 1) {
			return true;
		}

		return false;

	}

	public void j1score()
	{
		this.scorej1++;
	}

	public void j2score()
	{
		this.scorej2++;
	}

	private String traductionScore(final int score)
	{
		switch (score)
		{
		case 3:
			return "40";
		case 2:
			return "30";
		case 1:
			return "15";
		case 0:
			return "0";
		}
		throw new IllegalArgumentException("score: " + score);
	}
}