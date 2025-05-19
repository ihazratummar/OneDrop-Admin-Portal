from pydantic import BaseModel
from enum import Enum
from typing import Optional


class ReportStatus(Enum):
    PENDING = "Pending"
    OPEN = "Open"
    RESOLVED = "Resolved"
    CLOSED = "Closed"
    REJECTED = "Rejected"

class ReportModel(BaseModel):
    reportId: str
    reporterId: str
    reportedId: str
    reportType: str
    reason: str
    description: str
    annonymous: bool
    reportStatus: ReportStatus
    timestamp: str
    screenshot: Optional[str]
    reportedMobileNumber: str
    reportedName: str