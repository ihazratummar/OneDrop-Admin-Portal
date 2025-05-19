from pydantic import  BaseModel
from typing import  Optional
from models.BloodGroup import  BloodGroup
from models.NotificationScope import NotificationScope


class Donor(BaseModel):
    userId: str
    name: str
    age: str
    gender: str
    bloodGroup: BloodGroup
    city: str
    district: str
    state: str
    available: bool
    contactNumber: str
    isContactNumberPrivate: bool
    notificationEnabled: bool
    notificationScope: NotificationScope
    email: Optional[str]