from pydantic import BaseModel

class AcademicRecord(BaseModel):
    userId: str
    semestre: str
    creditosInscritos: str
    creditosAprobados: str
    creditosPendientes: str
    creditosCursados: str
    creditosCancelados: str
    tipologia: str
    papa: str
    pa: str
    pappi: str
    avance: str
    materias: str
    planDeEstudios: str
