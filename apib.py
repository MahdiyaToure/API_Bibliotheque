from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)
motdepasse = quote_plus(os.getenv('db_password'))
hote=os.getenv('hostname')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:{}@{}:5432/bibliotheque'.format(motdepasse,hote)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)
CORS(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,True')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE , OPTION')
    return response

############################################
#        Endpoint: CREATION CLASS LIVRE
############################################

class Livre(db.Model):
    __tablename__='livres'
    Id=db.Column(db.Integer, primary_key =True)
    isbn=db.Column(db.String(50),nullable=False)
    titre=db.Column(db.String(100),nullable= False)
    date_publication=db.Column(db.DateTime,nullable=False)
    auteur=db.Column(db.String(50),nullable=False)
    editeur=db.Column(db.String(50),nullable=False)
    categorie_id=db.Column(db.Integer,db.ForeignKey('categories.Id'),nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
         return{
            'Id': self.Id,
            'isbn': self.isbn,
            'titre': self.titre,
            'date_publication': self.date_publication,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'categorie_id':self.categorie_id
            }

############################################
#     Endpoint: CREATION CATEGORIE
############################################
class Categorie(db.Model):
    __tablename__='categories'
    Id=db.Column(db.Integer, primary_key =True)
    libelle_categorie=db.Column(db.String(50),nullable=False)
    livres=db.relationship('Livre', backref='categorie', lazy=True)

    ############################################
    #    Endpoint: DEFINITION DES FONCTIONS
    ############################################
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return{
            'Id': self.Id,
            'libelle_categorie': self.libelle_categorie
        }
db.create_all()

#####################################################
#      Endpoint: LISTES DES LIVRES
#####################################################

@app.route('/livres',methods=['GET'])
def get_all_livre():

    livres=Livre.query.all()
    livres_formated=[et.format() for et in livres]
    return jsonify({
        'Success':True,
        'total_livres': len(livres),
        'livres':livres_formated
    })

######################################################
#       Endpoint:  RECHERCHE D'UN LIVRE PAR ID 
######################################################
@app.route('/livres/<int:id>',methods=['GET'])
def Select_one_livre(id):
    #selection d'un seul element
    livre=Livre.query.get(id)
    #Verification de l'existe du livre
    if livre is None:
        abort(404)
    else:
        return jsonify({
            'Success':True,
            'selected_id':id,
            'livre':livre.format()
        })


######################################################
#      Endpoint: LISTE DES LIVRES PAR CATEGORIE
######################################################
@app.route('/categories/<int:id>/livres',methods=['GET'])
def Select_livres_categorie(id):
    categorie=Categorie.query.get(id)
    #Verification de l'existe de la categorie
    if categorie is None:
        abort(404)
    else:
        livres=Livre.query.filter(Livre.categorie_id==id).all()
        formated_livres=[ bk.format() for bk in livres]
        return jsonify({
            'Success':True,
            'selected_id':id,
            'categorie':categorie.format(),
            'libelle_categorie':categorie.libelle_categorie,
            'total':len(livres),
            "livres":formated_livres  
            
        })

######################################################
#    Endpoint: RECHERCHE D'UNE CATEGORIE PAR ID
######################################################
@app.route('/categories/<int:id>',methods=['GET'])
def Select_one_cat(id):
    #selection d'un seul element
    categorie=Categorie.query.get(id)
    #Verification de l'existe du livre
    if categorie is None:
        abort(404)
    else:
        return jsonify({
            'Success':True,
            'selected_id':id,
            'Categorie':categorie.format()
        })

######################################################
#      Endpoint:  LISTE DES CATEGORIES
######################################################
@app.route('/categories',methods=['GET'])
def get_all_cat():

    categorie=Categorie.query.all()
    categorie_formated=[et.format() for et in categorie]
    return jsonify({
        'total_etudiants': len(categorie),
        'categorie':categorie_formated
    })

#######################################################
#     Endpoint: SUPPRESSION D'UN LIVRE
#######################################################
@app.route('/livres/<int:id>',methods=['DELETE'])
def Delete_one_livre(id):
    #selection d'un seul element
    livre=Livre.query.get(id)
    #Verification de l'existe du livre
    if livre is None:
        abort(404)
    else:
        livre.delete()
        return jsonify({
            'Success':True,
            'selected_id':id,
            'livre':livre.format(),
            'total_livres':Livre.query.count()

        })


#######################################################
#     Endpoint: SUPPRESSION D'UNE CATEGORIE
#######################################################
@app.route('/categories/<int:id>',methods=['DELETE'])
def Delete_one_cat(id):
    #selection d'un seul element
    categorie=Categorie.query.get(id)
    #Verification de l'existe du livre
    if categorie is None:
        abort(404)
    else:
        categorie.delete()
        return jsonify({
            'Success':True,
            'selected_id':id,
            'Categorie':categorie.format(),
            'total_categories':Categorie.query.count()
        })


#######################################################
#       Endpoint: MODIFICATION D'UN LIVRE
#######################################################
@app.route('/livres/<int:id>',methods=['PATCH'])
def update_one_livre(id):
    #selection d'un seul element
    livre=Livre.query.get(id)
    body=request.get_json()
    livre.isbn=body.get('isbn')
    livre.titre=body.get('titre')
    livre.date_publication=body.get('date_publication')
    livre.auteur=body.get('auteur')
    livre.editeur=body.get('editeur')
    #Verification de l'existe du livre
    if livre is None:
        abort(404)
    else:
       
        livre.update()
        return jsonify({
            'Success':True,
            'selected_id':id,
            'livre':livre.format(),
            'total_livres':Livre.query.count()

        })


#######################################################
#      Endpoint: MODIFICATION D'UNE CATEGORIE
#######################################################
@app.route('/categories/<int:id>',methods=['PATCH'])
def Update_one_cat(id):
    #selection d'un seul element
    body=request.get_json()
    categorie=Categorie.query.get(id)
    categorie.libelle_categorie=body.get('libelle_categorie')
    #Verification de l'existe du livre
    if categorie is None:
        abort(404)
    else:
        categorie.update()
        return jsonify({
            'Success':True,
            'selected_id':id,
            'Categorie':categorie.format(),
            'total_categories':Categorie.query.count()
        })


#######################################################
#      Endpoint:  MESSAGE D'ERREUR
#######################################################
@app.errorhandler(404)
def error_not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'etudiants': "Not Found"
    })


########################################################### FIN ############################################################
