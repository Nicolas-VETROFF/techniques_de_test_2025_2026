# PLAN DE TESTS

## Architecture
    src/
        app/
        tests/

## Tests unitaires

### API
- [x] Renvoie pour chaque route les bonnes informations en JSON (bonnes clés, bons types, ...)
- [x] Renvoie les bons code HTTP (200, 400, 500)
- ...

#### Triangulator
- [x] Donne les bons Triangles (3 points / carré de points / 2 points / 3 points colinéaires)
  - Permet de savoir si la triangulation fonctionne correctement
- [x] Donne le bon nombre de triangles (3 points / carré de points / 2 points / 3 points colinéaires)
  - Permet de savoir si l'algorithme calcule correctement les triangles possibles : (1, 2, 0, 0)
- [x] Convertie correctement la triangulation en binaire (3 points)
  - Binaire correct contenant les points, le nombre de points et les triangles
- [x] Décode correctement le binaire (3 points en binaire)
  - Récupération de chaque point ET du nombre de points
- [x] Est idempotent (conversion + reconversion) : On doit retrouver les mêmes valeurs
- [x] Robustesse 
  - Erreur si le PointSetID ne correspond à aucun PointSet
  - Erreur si le PointSet récupéré est mal formé (tronqué / corrompu)
- ...

#### PointSet
- [x] Garde en mémoire le bon nombre de points et les bonnes coordonnées de chacun d'entre eux
  - Après création d'un pointSet, on vérifie si on peut récupérer le binaire sauvegardé
- [x] Convertie correctement l'ensemble des 3 points en binaire 
  - Binaire correct pour les coordonnées de points et leur nombre fourni en entrée (3 points)
- ...

#### PointSetManager
- [x] Retourne le bon PointSetID du PointSet nouvellement enregistré
- [x] Charge le bon PointSet en fonction du PointSetID
- [x] Cas ID inconnu
  - Doit renvoyer une erreur gérée par le programme (404)
- [x] Cas bdd inaccessible
  - Doit renvoyer une erreur gérée par le programme (500)
- ...

### Client
- ...

## Tests d'intégration

### API

#### Triangulator
- [x] Reçoit le bon PointSet du PointSetManager
- ...

### Client
- [ ] Reçoit le bon PointSetID du PointSetManager
- [ ] Reçoit les bons Triangles du Triangulator
- ...

...

## Test fonctionnel

Tester du PointSet envoyé par le client au Triangles finaux envoyés par Triangulator

## Tests de performance
INFO : Ces tests sont lancer à part, à cause du temps qu'ils peuvent prendre.
- [x] Rapidité du système pour trianguler (algorithme)
- [x] Rapidité du système à générer le binaire du PointSet
- [x] Rapidité du système à générer le binaire de Triangulator

## Tests de qualité et documentation
- [ ] Vérification de la qualité du code
  - Couverture de tests
  - ...
- [ ] Documentation complète
