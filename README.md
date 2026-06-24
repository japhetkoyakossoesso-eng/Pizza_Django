# 🍕 PizzaDjango

J'ai développé cette application web avec **Django** pour gérer le catalogue complet d'une pizzeria et exposer ses données à travers une **API** robuste. Le projet est entièrement fonctionnel, testé en local, et actuellement déployé en production sur **PythonAnywhere**.

---

## 💡 Le Projet en quelques mots

**PizzaDjango** est une application web back-end qui simule le système de gestion d'une pizzeria. L'objectif principal était de créer un système capable de stocker un catalogue de pizzas en base de données et de le rendre accessible non pas sous forme de site web classique, mais sous forme de **données brutes exploitables par d'autres applications**.

### 🔧 Les 3 briques clés que j'ai mises en place :

1. **Le Modèle de Données (`menu/models.py`)** : J'ai modélisé ce qu'est une pizza en programmation orientée objet (son nom, ses ingrédients, son prix). Django traduit automatiquement ce code Python en tables SQL dans ma base de données `db.sqlite3`.
2. **L'API (Application Programming Interface)** : C'est la grande force du projet. Au lieu de concevoir des pages HTML/CSS pour les humains, j'ai créé un point d'accès (`/api/`) qui distribue le menu au format **JSON**. Cela permet de connecter ce même back-end à une application mobile iOS/Android ou à des bornes de commande !
3. **Le Déploiement Cloud** : Le projet ne tourne pas juste sur ma machine. Je l'ai configuré et déployé sur un serveur distant (**PythonAnywhere**) avec une gestion personnalisée du fichier WSGI pour le rendre accessible en ligne H24.

---

## 🔄 Le flux des données (Comment ça marche ?)

Lorsqu'une application cliente appelle mon projet, voici le chemin parcouru par la donnée :

```text
 Un utilisateur (ou une appli mobile) tape l'adresse `/api/`
       │
       ▼
 Le fichier `pizza/urls.py` intercepte la demande
       │
       ▼
 Il passe le relais à `api_urls.py` (le guichet de l'API)
       │
       ▼
 L'API va chercher les données des pizzas dans l'application `menu`
       │
       ▼
 L'application `menu` extrait les pizzas du frigo (`db.sqlite3`)
       │
       ▼
 Les pizzas sont renvoyées sous forme de données propres (JSON) ! 🍕


Structure de mon Répertoire

Voici l'organisation finale des fichiers que j'ai mis en place pour ce projet :

Plaintext
/home/japhetkoyakossoesso/PizzaDjango/pizza/   <-- Mon répertoire racine (contient manage.py)
├── pizza/                                     <-- Dossier de configuration (settings.py, urls.py)
├── menu/                                      <-- App Django de gestion du menu (models.py, migrations/)
│   └── migrations/                            <-- Historique des versions de ma base de données
├── api_urls.py                                <-- Mon routage spécifique pour l'API
└── db.sqlite3                                 <-- Ma base de données SQLite locale


🛠️ Comment j'installe et lance le projet en local

1. Environnement virtuel & Dépendances
Sur ma machine, je me positionne dans le répertoire racine et j'active mon environnement virtuel avant d'installer Django :
Bash
python3 -m venv .venv
source .venv/bin/activate
pip install django
2. Initialisation de la base de données
Pour générer les tables SQL à partir de mes modèles et appliquer les dernières modifications (comme la mise à jour des clés primaires avec BigAutoField), j'exécute :
Bash
python manage.py makemigrations
python manage.py migrate
3. Exécution
Je lance mon serveur de développement avec la commande :
Bash
python manage.py runserver
L'application devient alors accessible en local sur http://127.0.0.1:8000/.

🌐 Ma Configuration de Déploiement (PythonAnywhere)
Pour rendre mon application accessible en ligne, je l'ai hébergée sur PythonAnywhere. J'ai configuré le fichier WSGI de mon serveur de production (_wsgi.py) pour qu'il pointe directement sur mon projet en éliminant les conflits de modules :
Python
import os
import sys

# Mon chemin absolu vers le projet
path = '/home/japhetkoyakossoesso/PizzaDjango/pizza'
if path not in sys.path:
    sys.path.append(path)

# Chargement de mes settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'pizza.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
