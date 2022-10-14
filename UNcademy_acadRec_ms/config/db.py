from pymongo import MongoClient
import os

conn = MongoClient(os.environ['DB_URL'])
#conn = MongoClient()

db = conn["AcademicRecords"]
acadRec = db["AcademicRecord"]

