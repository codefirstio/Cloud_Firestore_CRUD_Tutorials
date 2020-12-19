import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

# Read data
# Get a document with known id
result = db.collection('persons').document("p1").get()
if result.exists:
    print(result.to_dict())

# Get all documents
docs = db.collection('persons').get()
for doc in docs:
    print(doc.to_dict())

# Query
# Equal
docs = db.collection('persons').where("age", "==", "52").get()
for doc in docs:
    print(doc.to_dict())

# Greater than
docs = db.collection('persons').where("age", ">", "22").get()
for doc in docs:
    print(doc.to_dict())

# Array contains
docs = db.collection('persons').where("socials", "array_contains", "facebook").get()
for doc in docs:
    print(doc.to_dict())

# In
docs = db.collection('persons').where("address", "in", ["Milan", "London"]).get()
for doc in docs:
    print(doc.to_dict())
