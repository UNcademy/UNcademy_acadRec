from fastapi import APIRouter
from schemas.academicRecord import serializeDict, serializeList
from models.academicRecord import AcademicRecord
from config.db import db
from bson import ObjectId

academicRecord = APIRouter()

@academicRecord.get('/')
async def find_all_records():
  return serializeList(db.academicRecord.find())

@academicRecord.post('/')
async def create_record(academicRecord: AcademicRecord):
  db.academicRecord.insert_one(dict(academicRecord))
  return serializeList(db.academicRecord.find())

@academicRecord.put('/{id}')
async def update_record(id, academicRecord: AcademicRecord):
  db.academicRecord.find_one_and_update({"_id":ObjectId(id)},{
    "$set":dict(academicRecord)
  })
  return serializeDict(db.academicRecord.find_one({"_id":ObjectId(id)}))

@academicRecord.delete('/{id}')
async def delete_record(id, academicRecord: AcademicRecord):
  return serializeDict(db.academicRecord.find_one_and_delete({"_id":ObjectId(id)}))
