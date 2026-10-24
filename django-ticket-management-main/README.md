# Gestion des tickets IT

Application web de support informatique développée avec Django. Elle permet aux utilisateurs de déclarer leurs problèmes, de suivre leur état et de consulter les demandes, tandis que les équipes de support peuvent les prendre en charge et les affecter.

Le projet centralise les demandes dans une liste commune et fournit un tableau de bord récapitulatif. Il vise à remplacer le suivi dispersé des incidents par un espace simple où retrouver le créateur, le statut et l'assignation de chaque ticket.

## Fonctionnalités

- **Authentification** : connexion et déconnexion avec un compte Django. L'adresse e-mail est l'identifiant du compte ; aucune inscription publique n'est proposée.
- **Création de tickets** : saisie d'un titre et d'une description. Le créateur et la date de création sont enregistrés automatiquement.
- **Suivi** : consultation des tickets et de leurs détails, notamment le créateur et la personne assignée.
- **Statuts** : `Nouvelle`, `En cours` et `Résolue`.
- **Assignation** : un ticket peut être affecté à un utilisateur ou rester non assigné.
- **Rôles** : les comptes disposent d'un rôle parmi `employe`, `technicien` et `responsable`. Dans la liste, les employés ne voient que leurs propres tickets ; les autres rôles voient tous les tickets.
- **Tableau de bord** : affichage du nombre total de tickets et du nombre de tickets par statut.
- **Administration Django** : gestion des comptes et des objets enregistrés depuis l'interface d'administration.

Les pages de tickets et le tableau de bord nécessitent une connexion. Les rôles sont enregistrés et utilisés pour filtrer la liste ; dans l'implémentation actuelle, la modification du statut et de l'assignation n'est pas restreinte à un rôle particulier. Les comptes se créent depuis l'administration Django ou la ligne de commande, et non depuis une page d'inscription.

L'application `audit` contient un modèle de journal d'audit, mais l'enregistrement d'événements n'est pas encore intégré aux vues.

## Technologies

- **Python** et **Django 5.2.18**
- **Base de données** :
  - SQLite par défaut pour un démarrage local sans configuration supplémentaire ;
  - PostgreSQL en option, sélectionné à l'aide de `DATABASE_URL` ou des variables `POSTGRES_*`.
- **Bibliothèques Python** : `psycopg2-binary` (connexion PostgreSQL), `python-dotenv` (chargement du fichier `.env`), `whitenoise` (fichiers statiques) et `gunicorn` (serveur WSGI).
- **Interface** : templates Django et Bootstrap 5.3.3, avec Bootstrap Icons chargés depuis jsDelivr.
- **Tests** : tests Django, exécutables avec la commande `manage.py test`.

Les ressources Bootstrap et Bootstrap Icons étant chargées depuis un CDN, leur affichage nécessite un accès réseau depuis le navigateur.

## Installation et lancement local

### Prérequis

- Python compatible avec Django 5.2 (Python 3.10 ou supérieur recommandé).
- `pip`.
- Pour PostgreSQL uniquement : une instance PostgreSQL accessible et configurée.

### 1. Ouvrir le dossier du projet

Depuis un terminal, placez-vous dans le dossier qui contient `manage.py` :

```powershell
cd chemin\vers\django-ticket-management-main
```

### 2. Créer et activer un environnement virtuel

Sous Windows PowerShell :

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

Sous macOS ou Linux :

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurer la base de données

Sans configuration supplémentaire, le projet utilise SQLite et crée le fichier `db.sqlite3` à la racine du projet lors des migrations.

Pour PostgreSQL, créez un fichier `.env` à côté de `manage.py`, puis renseignez les paramètres de votre instance. Vous pouvez partir de `.env.example`, en remplaçant les valeurs d'exemple :

```dotenv
SECRET_KEY=remplacez-par-une-cle-locale
DEBUG=True
POSTGRES_DB=ticket_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=votre_mot_de_passe
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Les variables `POSTGRES_*` font basculer la configuration sur PostgreSQL. Vous pouvez également définir `DATABASE_URL` avec une URL PostgreSQL ; lorsqu'elle est renseignée, elle est prioritaire. Ne conservez pas les identifiants d'exemple et n'utilisez pas `DEBUG=True` en production.

### 5. Appliquer les migrations

```bash
python manage.py migrate
```

### 6. Créer un compte administrateur

```bash
python manage.py createsuperuser
```

Le modèle utilisateur utilise l'adresse e-mail comme identifiant. Après connexion à `/admin/`, vous pouvez gérer les comptes et leur attribuer un rôle.

### 7. Lancer le serveur de développement

```bash
python manage.py runserver
```

Ouvrez ensuite :

- `http://127.0.0.1:8000/accounts/login/` pour vous connecter ;
- `http://127.0.0.1:8000/dashboard/` pour le tableau de bord ;
- `http://127.0.0.1:8000/tickets/` pour la liste des tickets ;
- `http://127.0.0.1:8000/admin/` pour l'administration.

### Exécuter les tests

```bash
python manage.py test
```

## Structure du projet

```text
.
├── apps/
│   ├── accounts/      # Modèle utilisateur personnalisé et routes de connexion
│   ├── audit/         # Modèle de journal d'audit
│   ├── dashboard/     # Vue et routes du tableau de bord
│   └── tickets/       # Modèle, formulaires, vues et routes des tickets
├── config/            # Paramètres Django, routes racine, ASGI et WSGI
├── templates/         # Templates Django partagés et pages de l'application
├── staticfiles/       # Fichiers statiques collectés, notamment ceux de Django Admin
├── tests/             # Tests transversaux du projet
├── manage.py          # Commandes d'administration Django
└── requirements.txt   # Dépendances Python
```

Les migrations propres à chaque application se trouvent dans son sous-dossier `migrations/`. Les templates de tickets et du tableau de bord sont regroupés dans `templates/tickets/` et `templates/dashboard/`.
