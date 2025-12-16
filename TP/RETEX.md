# Retour sur expérience

Lors de ce TP, j'ai eu, en premier lieu, besoin de me familiariser avec python et ses outils (flask, pytest, coverage, pdoc3).
La méthode TDD (Test Driven Development) a été utilisée pour tester l'application sans l'implémenter.

L'un des points où j'ai eu du mal est la réflexion même sur les tests à mettre en place sans avoir une idée claire de l'implémentation. C'est un aspect assez difficile à maîtriser car on a tendance à vouloir implémenter avant de concevoir les tests unitaires.

Malgré cette manière de faire, j'ai constaté que j'avais tout de même oublié de tester des cas évidents d'erreur que j'ai du rectifier après avoir commencer à implémenter le corps de l'application.

Ensuite, j'ai eu du mal à comprendre comment fonctionnait le mock et comment il devait être utilisé en python. Aussi, il était compliqué de savoir le temps convenable pour les tests de performance de l'application. Surtout pour les larges et moyens ensembles de points à trianguler. Ainsi, les temps choisis furent arbitraire pour 1000 et 10000 points à trianguler. 

Mais je pense que le fait de créer les tests avant toute implémentation a été très utile pour m'assurer que mon code fonctionnait correctement par la suite. Cela permet aussi de ne pas se confronter à des biais lorsque l'on implémente le code avant de créer les tests. On oublie généralement de tester les cas limites et les cas d'erreur lorsque l'on implémente le code avant de tester car, avec cette approche, on ne veut pas que les tests passent (du moins au début) puisque nous n'avons pas implémenté le code.