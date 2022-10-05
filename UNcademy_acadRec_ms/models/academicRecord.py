from pydantic import BaseModel

class Materia(BaseModel):
  materiaId: str
  tipologia: str | None = None
  nombre: str
  nota: float
  aprobado: bool 
  creditos: int

class AcademicRecord(BaseModel):
  userId: str
  semestre: str | None = None
  creditosInscritos: int | None = None
  creditosAprobados: int | None = None
  creditosPendientes: int | None = None
  creditosCursados: int | None = None
  creditosCancelados: int | None = None
  papa: float | None = None 
  pa: float | None = None
  pappi: float | None = None
  avance: str | None = None
  materias: list[Materia] | None = None 
  planDeEstudios: str

