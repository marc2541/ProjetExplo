# Projet 2

<p>Demo apps, coded in Python, w/ framework : Flask. PostgreSQL as the database.</p>

```bash
.
└── flask_app
    └── PROJETEXPLO
        ├── app.py              # Main controller
        ├── init_db.py          # Create the database and insert lorem ipsum data
        ├── models.py           # N'existe pas, aurait pu être utilisé
        ├── static
            ├── css
                └── style.css        # Contient du css custom
            ├── js
                ├── function.js      # Contient des fonctions custom pour le site
                └── jquery-3.6.1     # Librairie Javascript : jquery-3.6.1
            ├── favicon.ico          # Logo onglet navigateur
            └── menu.png
        └── templates
            ├── base.html            # Contains common layout, nav links, and meta data
            ├── bibliotheque.html    # Index de la bibliothèque
            ├── create.html          # Form pour ajouter un livre à la bibliothèque
            └── index.html           # Page d'accueil
            
```