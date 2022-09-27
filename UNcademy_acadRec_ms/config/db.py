from pymongo import MongoClient
import os

#conn = MongoClient('uncademy_acadrec_db', 27088)
#conn = MongoClient('mongodb://uncademy_acadrec_db/27017/')
#conn = MongoClient('mongodb://uncademy_acadrec_db:27088')
#conn = MongoClient('mongodb://b8cc1cbfbe39_UNcademy_acadRec_db:27088')
#conn = MongoClient('mongodb://db:27017/')
#dbURL = os.environ["DB_URL"]
conn = MongoClient(os.environ['DB_URL'])
#conn = MongoClient()

db = conn["AcademicRecords"]
acadRec = db["AcademicRecord"]

