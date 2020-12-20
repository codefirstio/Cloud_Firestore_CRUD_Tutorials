import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

# Delete a document - known ID
db.collection('persons').document("p1").delete()

# Delete a field - known ID
db.collection('persons').document("p2").update("age", firestore.DELETE_FIELD)

# Delete a document with a known ID
docs = db.collection('persons').where("age", ">=", 50).get() # Get all documents with age >=50
for doc in docs:
    key = doc.id
    db.collection('persons').document(key).delete()

# Delete a field - unknown ID
docs = db.collection('persons').where("age", ">=", 40).get() # Get all documents with age >=40
for doc in docs:
    key = doc.id
    db.collection('persons').document(key).update("age", firestore.DELETE_FIELD)

# Delete all documents in a collection
docs = db.collection('persons').get() # Get all data
for doc in docs:
    db.collection('persons').document(key).delete()
