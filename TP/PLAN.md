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
- [ ] Donne le bon nombre de triangles
- [ ] Convertie correctement la triangulation en binaire
- [ ] Décode correctement le binaire (récupération des coordonées initiales)
- [ ] Convertion + Reconvertion (non-binaire -> binaire -> non-binaire) : On doit retrouver les mêmes valeurs
- [ ] Robustesse (binaire corrompu ou tronqué)
- ...

#### PointSet
- [ ] Garde en mémoire le bon nombre de points et les bonnes coordonées de chacun d'entre eux
- [ ] Convertie correctement l'ensemble des points en binaire (nombre point + coordonnées de tous les points)
- [ ] Robustesse (binaire corrompu ou tronqué)
- ...

#### PointSetManager
- [ ] Retourne le bon PointSetID du PointSet nouvellement enregistré
- [ ] Charge le bon PointSet en fonction du PointSetID
- [ ] Cas ID inconnu : doit renvoyer une erreur 404
- [ ] Cas bdd inaccessible : doit renvoyer une erreur 500
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
