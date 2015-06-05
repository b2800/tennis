# Tennis
Examen d'intégration continue ( 21/05/2015 )

Le repo regroupe les travaux des 2 groupes suivants :

Groupe Python
  - Xavier DEFER
  - Gilles RIVIERE

Groupe Java
  - Charles JUSSAN
  - Xavier PAQUET


##Application Java
### Commentaires
+ Note : 19
+ Points négatifs :
  - Certains tests sont redondant (Joueur1 gagne 3 points / Joueur2 gagne 2 points)
  - Certaines fonctions n'ont pas un nom explicite (jeu.j1Score pour faire marquer le joueur 1 par exemple)
+ Points positifs : 
  - Les fonctions sont bien découpées
  - Calcul du score lisible et propre ( pas de if imbriqués )

## Application en Python
### Commentaires 
+ Note : 19.5
+ Points négatifs :
  - Toutes les classes sont dans le même fichier
  - La classe joueur est inutile dans ce type d'implémentation
  - La syntaxe des tests pour vérifier les scores est lourde
  - Il faut faire plusieurs requêtes pour avoir le score complet (d'abord les points, puis les sets, et recommencer pour l'autre joueur)

### Lancer la suite de tests
Si vous avez Python d'installé, vous pouvez lancer les tests sur votre machine avec la commande 
``` python
python test.py
```
Si vous n'avez pas Python et que vous ne pouvez pas l'installer, vous pouvez lancer les tests en ligne à l'adresse suivante: 
http://goo.gl/uqp6u8
