from fastapi import APIRouter
from schemas.academicRecord import serializeDict, serializeList
from models.academicRecord import AcademicRecord
from config.db import acadRec 
from bson import ObjectId

academicRecord = APIRouter()

@academicRecord.get('/')
async def find_all_records():
  return serializeList(acadRec.find())

@academicRecord.post('/')
async def create_record(academicRecord: AcademicRecord):
  acadRec.insert_one(dict(academicRecord))
  return serializeList(acadRec.find())

@academicRecord.put('/{id}')
async def update_record(id, academicRecord: AcademicRecord):
  acadRec.find_one_and_update({"_id":ObjectId(id)},{
    "$set":dict(academicRecord)
  })
  return serializeDict(acadRec.find_one({"_id":ObjectId(id)}))

@academicRecord.delete('/{id}')
async def delete_record(id, academicRecord: AcademicRecord):
  return serializeDict(acadRec.find_one_and_delete({"_id":ObjectId(id)}))
