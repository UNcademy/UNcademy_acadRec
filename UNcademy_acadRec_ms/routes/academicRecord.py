from fastapi import APIRouter
from schemas.academicRecord import serializeDict, serializeList
from models.academicRecord import AcademicRecord
from config.db import acadRec 
from bson import ObjectId

academicRecord = APIRouter()

def setAdvance(records,semester):
  pass

# New
@academicRecord.get('/academic-record/{userId}')
async def student_records(userId: str):
  return serializeList(acadRec.find({"userId": userId}).sort("semestre", 1).limit(1))

@academicRecord.get('/academic-record/student-program/{userId}')
async def student_program(userId: str):
  return serializeList(acadRec.find({"userId": userId}, {"programa": 1, "_id": 0}).limit(1))

@academicRecord.get('/academic-record/')
async def find_all_records():
  return serializeList(acadRec.find())

@academicRecord.post('/academic-record/')
async def create_record(academicRecord: AcademicRecord):
  ar = dict(academicRecord)
  records = await student_records(ar["userId"])
  for idx in range(len(ar['materias'])):
    ar['materias'][idx] = dict(ar['materias'][idx])

  ar['programa'] = dict(ar['programa'])
  cd = ar['programa']['creditosDisciplinarOpt'] + ar['programa']['creditosDisciplinarOb']
  cf = ar['programa']['creditosFundamentacionOpt'] + ar['programa']['creditosFundamentacionOb']
  cl = ar['programa']['creditosLibreEleccion']
  cg = ar['programa']['creditosTrabajoDeGrado']
  ct = cd + cf + cl + cg
  
  ca = ar['creditosAprobados']
#  ar['creditosInscritos'] = 0
#  ar['creditosAprobados'] = 0
  ar['creditosPendientes'] = ct - ca
  ar['creditosCursados'] = 3
#  ar['creditosCancelados'] = 0
  ar['papa'] = 3.7
  ar['pa'] = 4.3
  ar['pappi'] = 3.1
  if ct > 0:
    ar['avance'] = "{:.1%}".format(ca/ct)
  else:
    ar['avance'] = "{:.1%}".format(0)

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

# Devuelve todas las materias aprovadas del estudiante
@academicRecord.get('/academic-record/materias/{userId}')
async def student_approved_courses(userId: str):
  records = await student_records(userId)
  materias = []
  for i in records:
    for j in i['materias']:
      if j['aprobado']:
        materias.append(j)
  return materias

@academicRecord.post('/academic-record/recordFromMQ')
async def create_record_MQ(message: dict):
  ar = {}
  plan = {}
  ar['userId'] = message['Username']
  plan['programaId'] = message['Program']
  ar['programa'] = plan
  acadRec.insert_one(ar)
  print(ar)
  return serializeList(acadRec.find())

