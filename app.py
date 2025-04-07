import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv('associations_etudiantes.csv')
evenements_df = pd.read_csv('evenements_associations.csv')

## Vous devez ajouter les routes ici : 

app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

## Vous devez ajouter les routes ici :

# Vérifie si le serveur est en fonctionnement
@app.route('/api/alive', methods=['GET'])
def alive():
   return jsonify({"message": "Alive"}), 200

# Liste de toutes les associations (IDs uniquement)
@app.route('/api/associations', methods=['GET'])
def get_associations():
   ids = associations_df['id'].tolist()
   return jsonify(ids), 200

# Détails d'une association
@app.route('/api/association/<int:id>', methods=['GET'])
def get_association(id):
   row = associations_df[associations_df['id'] == id]
   if row.empty:
       return jsonify({"error": "Association not found"}), 404
   return jsonify(row.iloc[0].to_dict()), 200

# Liste de tous les événements (IDs uniquement)
@app.route('/api/evenements', methods=['GET'])
def get_evenements():
   ids = evenements_df['id'].tolist()
   return jsonify(ids), 200

# Détails d'un événement
@app.route('/api/evenement/<int:id>', methods=['GET'])
def get_evenement(id):
   row = evenements_df[evenements_df['id'] == id]
   if row.empty:
       return jsonify({"error": "Event not found"}), 404
   return jsonify(row.iloc[0].to_dict()), 200

# Événements d'une association
@app.route('/api/association/<int:id>/evenements', methods=['GET'])
def get_evenements_association(id):
   events = evenements_df[evenements_df['association_id'] == id]
   return jsonify(events.to_dict(orient='records')), 200

# Associations par type
@app.route('/api/associations/type/<type>', methods=['GET'])
def get_associations_by_type(type):
   filtered = associations_df[associations_df['type'].str.lower() == type.lower()]
   return jsonify(filtered.to_dict(orient='records')), 200

if __name__ == '__main__':
   app.run(debug=False)

if __name__ == '__main__':
    app.run(debug=False)