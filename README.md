# Techniques de test 2025/2026

Le sujet du TP se trouve [ici](./TP/SUJET.md)

## Étudiant

Nom : VETROFF  
Prénom : Nicolas  
Groupe de TP : M1 ILSEN alternance  

## Remarques particulières

Pour lancer l'environnement python :
- Se mettre à la racine du projet
- `source env/bin/activate`

Pour utiliser l'application :
- Se mettre à la racine du projet
- `export FLASK_APP=src/app/app.py` (Linux) ou `set FLASK_APP=src/app/app.py` (Windows)
- `flask run`

Pour lancer les tests :
- Se mettre à la racine du projet
- `pytest -v`

Pour voir la couverture des tests :
- Se mettre à la racine du projet
- `coverage run -m pytest`
- `coverage report`
- `coverage html`

Générer la documentation :
- Se mettre à la racine du projet
- `pdoc3 --html --force --output docs src/app`
