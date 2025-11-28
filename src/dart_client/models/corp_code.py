from pydantic import BaseModel, Field
from typing import Optional

class CorpCode(BaseModel):
    """
    Model for DART Corporation Code (from corpCode.xml).
    """
    corp_code: str = Field(..., description="DART unique corporation code (8 digits)")
    corp_name: str = Field(..., description="Corporation name")
    stock_code: Optional[str] = Field(None, description="Stock code (6 digits) if listed")
    modify_date: str = Field(..., description="Last modification date (YYYYMMDD)")

    class Config:
        populate_by_name = True
