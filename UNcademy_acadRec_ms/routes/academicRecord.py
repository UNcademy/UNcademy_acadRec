from fastapi import APIRouter
from schemas.academicRecord import serializeDict, serializeList
from models.academicRecord import AcademicRecord
from config.db import acadRec 
from bson import ObjectId

academicRecord = APIRouter()

def setAdvance(records,semester):
  pass

@academicRecord.get('/academic-record/')
async def find_all_records():
  return serializeList(acadRec.find())

@academicRecord.post('/academic-record/')
async def create_record(academicRecord: AcademicRecord):
  records = await find_all_records()
  ar = dict(academicRecord)
  for idx in range(0,len(ar['materias'])):
    ar['materias'][idx] = dict(ar['materias'][idx])
  print(ar['materias'])
  ar['creditosInscritos'] = 0
  ar['creditosAprobados'] = 0
  ar['creditosPendientes'] = 0
  ar['creditosCursados'] = 0
  ar['creditosCancelados'] = 0
  ar['papa'] = 0
  ar['pa'] = 0
  ar['pappi'] = 0
  ar['avance'] = 0

  acadRec.insert_one(ar)
  return serializeList(acadRec.find())

@academicRecord.put('/academic-record/{id}')
async def update_record(id, academicRecord: AcademicRecord):
  acadRec.find_one_and_update({"_id":ObjectId(id)},{
    "$set":dict(academicRecord)
  })
  return serializeDict(acadRec.find_one({"_id":ObjectId(id)}))

@academicRecord.delete('/academic-record/{id}')
async def delete_record(id, academicRecord: AcademicRecord):
  return serializeDict(acadRec.find_one_and_delete({"_id":ObjectId(id)}))

# Materias pasadas
@academicRecord.get('/academic-record/materias')
async def find_all_approved_courses():
  records = await find_all_records()
  materias = []
  for i in records:
    for j in i['materias']:
      if j['aprobado']:
        materias.append(j)
  return materias

@academicRecord.post('/academic-record/recordFromMQ')
async def create_record_MQ(a):#academicRecord: AcademicRecord):
#  ar = dict(academicRecord)
#  ar =
#  acadRec.insert_one(ar)
#  return serializeList(acadRec.find())
  print('Respuesta MQ '+a)
  return 'respuesta MQ' + a

