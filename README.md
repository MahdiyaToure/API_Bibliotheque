# API GESTION DE BIBLIOTHEQUE

Cette API permet de gérer des categories de livres d'une bibliothèque

### Installing Dependencies

#### Python 3.9.8
#### pip 22.0.3 from C:\Users\Mahdiya\AppData\Local\Programs\Python\Python39\lib\site-packages\pip (python 3.9)

Si vous n'avez pas installé python, merci de suivre cette URL pour l'installer [python docs](https://www.python.org/downloads/windows/#getting-and-installing-the-latest-version-of-python)


#### Environnement virtuel

Vous devez installer le package dotenv en utilisant la commande "pip install python-dotenv"

#### Dépendances de PIP

Exécuter la commande ci dessous pour installer les dépendences
```bash
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

Cette commande installera tous les packages se trouvant dans le fichier `requirements.txt`.

##### clé de Dépendances

- [Flask](http://flask.pocoo.org/)  est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

- [SQLAlchemy](https://www.sqlalchemy.org/) est un toolkit open-source SQL et un ORM écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) est l'extension que nous utiliserons pour gérer les requêtes cross origin de notre serveur frontal.

## Configuration dela base de données

avec postgres en cours d'execcution, vous pouvez restauré la base de données en utilisant le fichier fourni the bibliotheque.sql et insérer des données avec le fichier bibliotheque_insert.sql .
```bash
psql bibliotheque > bibliotheque.sql
```

## Démarrer le serveur

Le demarage du serveur se fait depuis le repertoire contenant les fichers python

Pour démarer le serveur sous Linux ou mac,
On execute

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Pour le démarrer sur Windows, executez:

```bash
set FLASK_APP=apib.py
set FLASK_ENV=development
flask run
```

##  REFERENCE API

Démarrage

URL de base : à l'heure actuelle, cette application ne peut être exécutée que localement et n'est pas hébergée en tant qu'URL de base. L'application principale est hébergée par défaut, http://localhost:5000 ; qui est défini comme proxy dans la configuration frontale.

## Gestion d'erreur

Les erreurs sont renvoyées sou forme d'objet au format Json:
```bash
{
    "success":False
    "error": 400
    "message":"Bad request"
}
```


L'API vous renvoie 4 types d'erreur:
```bash
. 400: Bad request 
. 500: Internal server error
. 422: Unprocessable
. 404: Not found 
```

## Points finaux
. ## GET/livres

    GENERAL:Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 

    SAMPLE: curl -i http://localhost:5000/livres

        {
        "livres": [
            {
                "Id": 2,
                "auteur": "ROXIE ROLL",
                "categorie_id": 1,
                "date_publication": "Wed, 02 Dec 2020 00:00:00 GMT",
                "editeur": "Maxime",
                "isbn": "fhh4",
                "titre": "Leave and Death"
            },
            {
                "Id": 3,
                "auteur": "ROE JOLL",
                "categorie_id": 2,
                "date_publication": "Tue, 02 Dec 2003 00:00:00 GMT",
                "editeur": "Laxime",
                "isbn": "fhh5",
                "titre": "Leavath"
            }
        ],
        'Success':True,
        "total_Livres": 2
    }
```

.##GET/livres/(id)
  GENERAL: Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de son ID et retourne également la valeur du succès et l'id passé en parametre.

    SAMPLE: curl -i http://localhost:5000/livres/2

    {
        {
            "Id": 2,
            "auteur": "ROXIE ROLL",
            "categorie_id": 1,
            "date_publication": "Wed, 02 Dec 2020 00:00:00 GMT",
            "editeur": "Maxime",
            "isbn": "fhh4",
            "titre": "Leave and Death"
        },
        "success": True,
        "selected_id": 2
    }
```

.##GET/categories/(id)/livres
  GENERAL:   Cet endpoint permet de lister les livres appartenant à une categorie donnée. Il renvoie l' objet de la categorie passé en id et les livres l'appartenant ainsi que la valeur du succès et  le total des livres dans la categorie.

    SAMPLE: curl -i http://localhost:5000/categories/1/livres

    {
    "Success": true,
    "categorie": {
        "Id": 3,
        "libelle_categorie": "Fiction"
    },
    "libelle_categorie": "Fiction",
    "livres": [
        {
            "Id": 4,
            "auteur": "PAUL TILL",
            "categorie_id": 3,
            "date_publication": "Wed, 02 Jul 2003 00:00:00 GMT",
            "editeur": "Laxe",
            "isbn": "fhh6",
            "titre": "Avath"
        }
    ],
    "selected_id": 3,
    "total": 1
}

```


.##GET/categories/(id)
  GENERAL: Cet endpoint permet de récupérer les informations d'une categorie particulière s'il existe par le biais de son ID, et retourne également la valeur du succès et l'id passé en parametre
    SAMPLE: curl -i http://localhost:5000/categories/2

   {
    "Categorie": {
        "Id": 2,
        "libelle_categorie": "Horreur"
    },
    "Success": true,
    "selected_id": 2
}
```

 ## GET/categories

    GENERAL:Cet endpoint retourne la liste des objets categories, la valeur du succès et le total des livres. 
    
    SAMPLE: curl -i http://localhost:5000/categories

   {
    "categorie": [
        {
            "Id": 1,
            "libelle_categorie": "Roman d amour"
        },
        {
            "Id": 2,
            "libelle_categorie": "Horreur"
        },
        {
            "Id": 3,
            "libelle_categorie": "Fiction"
        },
        {
            "Id": 4,
            "libelle_categorie": "Anime"
        }
    ],
    "total_etudiants": 4
}
```

. ## DELETE/livres/(id)
    GENERAL: Cet endpoint permet de supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, les informations de ce livre, la valeur du succès et le nouveau total des livres enregistrés.

        SAMPLE: curl -X DELETE http://localhost:5000/livres/3

    { 
        "id": 3,
        "livre": {
                "Id": 3,
                "auteur": "ROE JOLL",
                "categorie_id": 2,
                "date_publication": "Tue, 02 Dec 2003 00:00:00 GMT",
                "editeur": "Laxime",
                "isbn": "fhh5",
                "titre": "Leavath"
            }
        ],
        'Success':True,
        "total_Livres": 2
    }
```

. ## DELETE/categories/(id)
    GENERAL: Cet endpoint permet de supprimer un element si l'ID existe.Retourne l'ID de la categorie supprimée, les informations de cette categorie, la valeur du succès et le nouveau total des categories enregistrés.

        SAMPLE: curl -X DELETE http://localhost:5000/categories/1

    {
        "categorie": {
            "id": 1,
            "libelle_categorie": "Roman d'amour"
        },
        "id": 1,
        "success": true,
        "total_categories": 5
    }   
```
. ##PATCH/livres/(id)
    GENERAL: Cet endpoint permet de mettre à jour les informations du livre dont  l' id en passé en parametre et affiche le livre mis à jour, la valeur du succès et l'id passé en parametre..

    SAMPLE: curl -X PATCH http://localhost:5000/livres/3 -H "Content-Type:application/json" -d '{"auteur": "Robert GREENE","date_publication": "31-12-1998","editeur":    "Les editions Leduc.s","id": 3,"isbn": "979-10-92928-07-5","titre": "Power - Les 48 lois du pouvoir"}'

    {
    "livre": {
            "Id": 3,
            "auteur": "ROE JOLL",
            "categorie_id": 2,
            "date_publication": "Tue, 02 Dec 2003 00:00:00 GMT",
            "editeur": "Laxime",
            "isbn": "fhh5",
            "titre": "Leavath"
        }
        "success": true,
        "updated_id": 3
    }

```

. ##PATCH/categories(id)
    GENERAL:Cet endpoint permet de mettre à jour le libelle la categorie dont l' ID est passé en paramètre. Il retourne une nouvelle categorie avec la nouvelle valeur,  la valeur du succès et l'id passé en parametre.

    SAMPLE: curl -X PATCH 'http://localhost:5000/categories/8' -H "Content-Type:application/json" -d '{"libelle_categorie":"BD"}'

    {
        "categorie": {
            "id": 8,
            "libelle_categorie": "BD"
        },
        "success": true,
        "updated_id": 8
    }
'''

. ##PATCH/livres/(id)
    GENERAL: Cet endpoint permet de mettre à jour les informations du livre dont  l' id en passé en parametre et affiche le livre mis à jour, la valeur du succès et l'id passé en parametre..

    SAMPLE: curl -X PATCH http://localhost:5000/livres/3 -H "Content-Type:application/json" -d '{"auteur": "Robert GREENE","date_publication": "31-12-1998","editeur":    "Les editions Leduc.s","id": 3,"isbn": "979-10-92928-07-5","titre": "Power - Les 48 lois du pouvoir"}'

    {
    "livre": {
            "Id": 3,
            "auteur": "ROE JOLL",
            "categorie_id": 2,
            "date_publication": "Tue, 02 Dec 2003 00:00:00 GMT",
            "editeur": "Laxime",
            "isbn": "fhh5",
            "titre": "Leavath"
        },
        "success": true,
        "total_categories": 3
    }

```

FIN#   A P I _ B i b l i o t h e q u e  
 