from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fraud_detection"]
certificates = db["certificates"]

def insert_cert(data):
    return certificates.insert_one(data).inserted_id

def get_all_certs():
    return list(certificates.find({}, {"_id": 0}))