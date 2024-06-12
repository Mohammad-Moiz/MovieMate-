import firebase_admin
from firebase_admin import credentials, firestore

def get_db():
    if not firebase_admin._apps:
        cred = credentials.Certificate("pondering-5ff7c-c033cfade319.json")
        firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db
