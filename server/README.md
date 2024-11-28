
# MyToolbox Server

Serveur Python (Flask) pour l'utilitaire Boîte à outils.

## Lancement en local

Cloner le projet

```bash
  git clone https://github.com/VALENTIN4real/MyToolbox.git
```

Commencer par créer un environnement virtuel
```bash
  cd server/
  py -m venv venv
```

Pour l'utiliser, plusieurs méthodes selon l'OS:
```bash
  # CMD
  C:\> venv\Scripts\activate.bat

  # PowerShell
  PS C:\> venv\Scripts\Activate.ps1

  # Bash / Zsh
  source venv/bin/activate
```

Installer les dépendances
```bash
  py -m pip install -r requirements.txt
```

Initialiser la base de données
```bash
  flask -app app init-db
```

Lancer l'app
```bash
  flask run
  flask run --debug
  py app.py # (debug actif)
```

On peut aussi utiliser PyCharm, il faut alors setup l'environnement virtuel qu'on a créé :

Cliquer en bas à droite de l'IDE sur l'interpréteur et sélectionner "Add New Interpreter" puis "Add local Interpreter" et enfin sélectionner "Select existing" en pointant l'exécutable python dans le venv.