from pydantic import BaseModel
from typing import List, Optional

class BiologicalFilters(BaseModel):
    ageRange: Optional[str]
    gender: Optional[str]
    medicalConditions: List[str]
    medications: List[str]
    familyHistory: List[str]
    lifestyle: List[str]
    pastHospitalizations: List[str]

class DiseaseResponse(BaseModel):
    explanation: Optional[str]
    suggestedSpecialist: Optional[str]
    careTips: List[str]

class Disease(BaseModel):
    name: str
    description: str
    tags: List[str]
    symptoms: List[str]
    triggers: List[str]
    severity: Optional[str]
    duration: Optional[str]
    biologicalFilters: BiologicalFilters
    response: DiseaseResponse
