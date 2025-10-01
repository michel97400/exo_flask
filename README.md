# Exercices Flask

Ce projet contient une série d'exercices pratiques pour apprendre Flask, un framework web Python.

## Description

Cette application Flask présente différents concepts fondamentaux :
- Routes de base et paramètres d'URL
- Templates Jinja2
- Formulaires et gestion des données POST
- API JSON
- Base de données SQLite
- Gestion d'erreurs personnalisées
- Blueprints

## Installation

1. Clonez ce repository
2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Lancement de l'application

```bash
python app.py
```

L'application sera disponible sur `http://localhost:5000`

## Exercices disponibles

### Exercice 1 : Route simple
- **URL** : `/hello`
- **Description** : Affiche "Hello world"

### Exercice 2 : HTML de base
- **URL** : `/contact`
- **Description** : Affiche du HTML avec titre et paragraphe

### Exercice 3 : Paramètres d'URL
- **URL** : `/user/<name>`
- **Description** : Salue l'utilisateur avec son nom

### Exercice 4 : Templates Jinja2
- **URL** : `/jinja`
- **Description** : Utilise un template HTML

### Exercice 5 : Formulaire
- **URL** : `/age`
- **Description** : Formulaire pour saisir l'âge

### Exercice 6 : Liste d'articles
- **URL** : `/articles`
- **Description** : Affiche une liste d'articles

### Exercice 8 : API JSON
- **URL** : `/api/ping`
- **Description** : Retourne une réponse JSON `{"ping": "pong"}`

### Exercice 9 : Base de données - Ajout
- **URL** : `/user`
- **Description** : Ajoute un utilisateur en base de données

### Exercice 10 : Base de données - Liste
- **URL** : `/list_users`
- **Description** : Affiche la liste des utilisateurs

### Exercice 12 : Paramètres de requête
- **URL** : `/search?q=<terme>`
- **Description** : Affiche le terme de recherche

## Structure du projet

```
exo_flask/
├── app.py              # Application principale
├── requirements.txt    # Dépendances Python
├── README.md          # Ce fichier
├── static/
│   └── style.css      # Feuilles de style CSS
└── templates/
    ├── base.html      # Template de base
    ├── index.html     # Page d'accueil
    ├── articles_page.html
    └── 404.html       # Page d'erreur 404
```

## Technologies utilisées

- **Flask 3.1.2** - Framework web Python
- **Jinja2** - Moteur de templates
- **SQLite** - Base de données
- **HTML/CSS** - Interface utilisateur

## Auteur

Projet d'exercices Flask pour l'apprentissage du développement web en Python.