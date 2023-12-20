## ocr_devapp_pyth_12

# Scenario
Ce projet consiste à créer un Crm utilisable en ligne de commande pour le compte d'une societe fictive Epic Event

# Installation de PostGre Sql:
Installation
Utiliser Homebrew
La méthode la plus simple pour installer PostgreSQL sur un Mac est d'utiliser Homebrew, un gestionnaire de paquets pour MacOS.

Ouvrir le Terminal: Trouvez l'application Terminal dans votre dossier Applications ou utilisez Spotlight pour la rechercher.

Installer Homebrew (si vous ne l'avez pas déjà) : Exécutez la commande suivante dans le Terminal :


`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
Installer PostgreSQL : Après avoir installé Homebrew, exécutez cette commande pour installer PostgreSQL :

`brew install postgresql`
Démarrer le service PostgreSQL : Pour démarrer PostgreSQL, utilisez cette commande :

`brew services start postgresql`
Vérification de l'installation
Pour vérifier que PostgreSQL a été installé correctement, exécutez la commande suivante dans le Terminal :

`psql --version`
Cette commande affichera la version de PostgreSQL installée sur votre machine

Configuration initiale
Créer un utilisateur PostgreSQL
Accéder à PostgreSQL : Tapez `psql postgres`dans le Terminal

`Créer un nouvel utilisateur : Remplacez your_username par le nom d'utilisateur de votre choix :`

`CREATE ROLE your_username WITH LOGIN PASSWORD 'your_password';`
Donner les privilèges nécessaires : Pour donner à l'utilisateur les privilèges d'un superutilisateur, exécutez :


`ALTER ROLE your_username CREATEDB;`
Quitter psql : Tapez \q pour quitter l'interface de ligne de commande de PostgreSQL

`Utilisation de PostgreSQL
Pour commencer à utiliser PostgreSQL, connectez-vous à l'aide de votre nouvel utilisateur :

`psql -U your_username -d postgres`

# Installation et Lancement

Installation & lancement : Installer Python en version 3.8.8 Lancez un terminal et placez vous dans le dossier de votre choix puis clonez le repository: git clone https://github.com/PhP-Nexxt/ocr_devapp_pyth_12

Placez vous dans le dossier ocr_devapp_pyth_12, puis créez un environnement virtuel:

`python -m venv venv_epic_event`

Ensuite, activez-le sur MacOs/Linux `source venv_gudlft/bin/activate` - ou sur Windows venv_gudlft\scripts\activate.b Installez ensuite les packages requis: pip install -r requierement.txt

Lancer le programme en utilisant la commande python main.py







