from pymongo import MongoClient

#conn = MongoClient('uncademy_acadrec_db',27018)
conn = MongoClient('mongodb://uncademy_acadrec_db:27018/')
#conn = MongoClient()

db = conn["AcademicRecords"]
acadRec = db["AcademicRecord"]

