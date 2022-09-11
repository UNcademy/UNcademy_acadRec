from fastapi import FastAPI
from routes.academicRecord import academicRecord

app = FastAPI()

app.include_router(academicRecord)
