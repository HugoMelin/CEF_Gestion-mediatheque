1. Installer Python :
Téléchargez et installez Python (version 3.8 ou supérieure) depuis python.org.

2. Créer un environnement virtuel :
Ouvrez un terminal ou une invite de commande.
Naviguez vers le dossier où vous voulez créer votre projet.
Exécutez :
	`python -m venv env`
Activez l'environnement virtuel :
Sur Windows : `env\Scripts\activate`
Sur macOS/Linux : `source env/bin/activate`

3. Cloner le projet
`git clone https://github.com/HugoMelin/CEF_Gestion-mediatheque.git`
`cd Gestion-mediatheque`

4. Installer les dépendances :
`pip install django`
`pip install pytest`

5. Configurer la base de données :
Exécutez les migrations :
`python manage.py makemigrations gestion_mediatheque`
`python manage.py migrate`

5. Charger les données de test :
Lancer la commande `python manage.py loaddata initial_data.json`
   
7. Lancer le serveur de développement :
`python manage.py runserver`

8. Accéder à l'application :
Ouvrez un navigateur et allez à `http://127.0.0.1:8000 `
