# Blog API - TAF 1 (INF222)

Cette API Backend a été développée avec **FastAPI** et **SQLite** dans le cadre de l'UE INF222. Elle permet de gérer un système d'articles de blog avec des fonctionnalités de création, lecture, mise à jour, suppression (CRUD) et recherche.

## Fonctionnalités
- **Gestion des articles** : Création, affichage détaillé, modification et suppression.
- **Recherche avancée** : Recherche par mot-clé dans le titre ou le contenu.
- **Filtrage** : Possibilité de filtrer les articles par catégorie, auteur ou date.
- **Validation** : Contrôle strict des entrées (titre et auteur obligatoires).
- **Documentation automatique** : Interface interactive avec Swagger UI.

## Technologies utilisées
- **Langage** : Python 3.10+
- **Framework** : FastAPI
- **Base de données** : SQLite (via SQLAlchemy ORM)
- **Serveur** : Uvicorn

## Installation et Lancement

### 1. Prérequis
Assurez-vous d'avoir Python installé sur votre machine.

### 2. Installation des dépendances
Ouvrez un terminal dans le dossier du projet et exécutez la commande suivante :
   ```bash
   python3 -m pip install fastapi uvicorn sqlalchemy

### 3. Lancement de l'application

Pour démarrer le serveur localement :
   ```bash
   python3 -m uvicorn main:app --reload
  
Le serveur sera disponible sur: http://127.0.0.1:8000

## Utilisation de l'API

### Documentation Interactive (Swagger)
Accédez à la documentation complète et testez les endpoints directement depuis votre navigateur :
http://127.0.0.1:8000/docs

**Principaux Endpoints**

**Méthode,Endpoint,Description**

POST, /api/articles/, Créer un nouvel article
GET, /api/articles/, Liste tous les articles (Filtres dispos)
GET, /api/articles/{id}, Récupérer un article par son ID
GET, /api/articles/search, Rechercher (ex: ?query=python)
PUT, /api/articles/{id}, Modifier un article existant
DELETE, /api/articles/{id}, Supprimer un article

### Structue du Projet

blog-api/
├── main.py          # Point d'entrée de l'application
├── database.py      # Configuration SQLite et Session
├── models.py        # Modèles de la base de données (SQLAlchemy)
├── schemas.py       # Schémas de validation (Pydantic)
├── routers/
│   └── articles.py  # Logique des routes et contrôleurs
└── blog.db          # Base de données SQLite (générée au lancement)

### Auteur
**Nom** : SAKOUE NESTRIDE
**Matrucule** : 24H2445
**Filiere** : INFORMATIQUE
