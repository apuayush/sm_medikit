# other libraries
# from bs4 import BeautifulSoup as soup
import env

# from motor import MotorClient
# import xmltodict

# from firebase import firebase

# hash libraries
#
JWT_SECRET = env.JWT_SECRET
JWT_ALGORITHM = env.JWT_ALGORITHM
# db = MotorClient(env.db)['sm_medikit']
# fb = firebase.FirebaseApplication(env.fb)
# JWT_SECRET = os.environ['JWT_SECRET']
# JWT_ALGORITHM = os.environ['JWT_ALGORITHM']
# db = MotorClient(os.environ['DB_LINK'])['sm_medikit']

Un = 1 # Unknown uid

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate("api.json")
firebase_admin.initialize_app(cred, {
  'projectId': env.pid,
})

db = firestore.client()

def add_patient(doc):
    doc_ref = db.collection('emergency').document()
    doc_ref.set(doc)

add_patient({'uid': 123412341234,
             'description': 'Mango High',
             'gps': [110.64, 89.01],
             'pname': 'Amrut'
             })