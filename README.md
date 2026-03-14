# drilling_pipeline_ETL - Pipeline ETL pour données de machines de forage

## Description
**drilling_pipeline_ETL** est un projet Python qui met en place un pipeline ETL pour traiter et uniformiser les données de foreuses.  

Imaginons que vous travailliez pour un géant pétrolier. Chaque foreuse renvoie en temps réel des informations sur ses performances, mais comme elles sont fabriquées par différents industriels, les données ne sont pas homogènes. Certaines foreuses utilisent des unités différentes, d’autres n’ont pas toutes les informations, et les formats de date ou d’identifiant varient.  

Le pipeline **drilling_pipeline_ETL** permet de :
- Uniformiser les données issues de plusieurs sources
- Convertir les unités (miles → mètres)
- Standardiser les dates au format français `DD/MM/YYYY`
- Ajouter des informations manquantes (contact, identifiant)
- Nettoyer les champs inutiles  
- Produire des fichiers prêts à l’usage pour reporting, analyses ou applications de calcul de trajectoire  

Exemple d’application : réaliser un reporting sur toutes les foreuses situées sous 1000 mètres de profondeur pour répondre à un contrôle environnemental, ou identifier les fournisseurs qui vendent le plus de foreuses pour négocier des ristournes.

---

## Fonctionnalités principales
- Nettoyage et standardisation des données hétérogènes
- Conversion des unités et formatage des dates
- Normalisation des identifiants de machine
- Ajout d’informations de contact si manquantes
- Pipeline automatisé pour plusieurs fichiers JSON
- Sortie prête à l’analyse ou à l’intégration dans des applications

---

## Structure du projet

```
drilling_pipeline_ETL/
│
├── data/
│   ├── raw/          # fichiers JSON bruts
│   └── processed/    # fichiers JSON transformés (créés par le pipeline)
│
├── drills_utils.py   # fonctions utilitaires pour traitement des données
├── main.py           # script principal qui applique le pipeline sur tous les fichiers
├── requirements.txt  # dépendances Python
└── README.md
```


---

## Prérequis
- Python 3.x
- Virtualenv recommandé

Installer les dépendances :
pip install -r requirements.txt

---

## Utilisation

Placer les fichiers JSON bruts dans le dossier data/raw.

Lancer le script principal depuis la racine du projet :

python main.py

Les fichiers traités seront générés automatiquement dans data/processed.

Chaque étape du pipeline est appliquée automatiquement grâce aux fonctions définies dans drill_utils.py.

## Exemple de sortie

```json
{
  "machine_id": "DM-001",
  "name": "Land Rover 200",
  "location": {
    "latitude": 37.7749,
    "longitude": -107.9090,
    "region": "San Juan Basin",
    "country": "USA"
  },
  "status": "Under Maintenance",
  "specifications": {
    "type": "Onshore",
    "depth_capacity_meters": 11263,
    "drilling_speed_meters_per_day": 482,
    "crew_size": 25,
    "power_source": "Electric"
  },
  "last_maintenance_date": "15/07/2024",
  "next_maintenance_due": "15/01/2025",
  "contact_information": {
    "operator_company": null,
    "contact_person": null,
    "phone": null,
    "email": null
  }
}

## Contribution

Contributions bienvenues pour :

Ajouter de nouvelles transformations ETL

Améliorer la documentation

Intégrer tests automatisés
