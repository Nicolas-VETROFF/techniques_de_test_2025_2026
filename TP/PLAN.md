# PLAN DE TESTS

## Architecture
    src/
        app/
        tests/

## Tests unitaires

### API
- [ ] Renvoie pour chaque route les bonnes informations en JSON (bonnes clés, bons types, ...)
- [ ] Renvoie les bons code HTTP (200, 400, 500)
- ...

#### Triangulator
- [ ] Donne les bons Triangles (3 points / carré de points / 2 points / 3 points colinéaires)
  - Permet de savoir si la triangulation fonctionne correctement
- [ ] Donne le bon nombre de triangles (3 points / carré de points / 2 points / 3 points colinéaires)
  - Permet de savoir si l'algorithme calcule correctement les triangles possibles : (1, 2, 0, 0)
- [ ] Convertie correctement la triangulation en binaire (3 points)
  - Binaire correct contenant les points, le nombre de points et les triangles
- [ ] Décode correctement le binaire (3 points en binaire)
  - Récupération de chaque point ET du nombre de points
- [ ] Est idempotent (conversion + reconversion) : On doit retrouver les mêmes valeurs
- [ ] Robustesse 
  - Erreur si le PointSetID ne correspond à aucun PointSet
  - Erreur si le PointSet récupéré est mal formé (tronqué / corrompu)
- ...

#### PointSet
- [ ] Garde en mémoire le bon nombre de points et les bonnes coordonnées de chacun d'entre eux
  - Après création d'un pointSet, on vérifie si on peut récupérer le binaire sauvegardé
- [ ] Convertie correctement l'ensemble des points en binaire 
  - Binaire correct contenant les points et le nombre de points
- ...

#### PointSetManager
- [ ] Retourne le bon PointSetID du PointSet nouvellement enregistré
- [ ] Charge le bon PointSet en fonction du PointSetID
- [ ] Cas ID inconnu
  - Doit renvoyer une erreur gérée par le programme (404)
- [ ] Cas bdd inaccessible
  - Doit renvoyer une erreur gérée par le programme (500)
- ...

### Client
- ...

## Tests d'intégration

### API

#### Triangulator
- [ ] Reçoit le bon PointSet du PointSetManager
- ...

### Client
- [ ] Reçoit le bon PointSetID du PointSetManager
- [ ] Reçoit les bones Triangles du Triangulator
- ...

...

## Test fonctionnel

Tester du PointSet envoyé par le client au Triangles finaux envoyés par Triangulator

## Tests de performance
INFO : Ces tests sont lancer à part à cause du temps que ces tests peuvent prendre
- [ ] Rapidité du système pour trianguler (algorithme)
- [ ] Rapidité du système à générer le binaire du PointSet
- [ ] Rapidité du système à générer le binaire de Triangulator

## Tests de qualité et documentation
- [ ] Vérification de la qualité du code
- [ ] Documentation complète
