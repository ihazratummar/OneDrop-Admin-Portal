from pydantic import BaseModel
from typing import Optional
from models.BloodGroup import BloodGroup
from enum import Enum


class BloodRequestStatus(Enum):
    PENDING = "Pending"
    ACTIVE = "Active"
    FULFILLED = "Fulfilled"
    EXPIRED = "Expired"
    CANCELED = "Canceled"

class BloodRequestModel(BaseModel):
    id:str
    userId: str
    patientName: str
    contactPersonName: str
    patientAge: str
    patientGender: str
    patientBloodGroup: BloodGroup
    hospitalName: str
    patientCity: str
    patientDistrict: str
    patientState: str
    date: int
    bloodUnit: int
    urgency: str
    requisitionForm: Optional[str]
    dateOfCreation: int
    bloodRequestStatus: BloodRequestStatus
    number: str



