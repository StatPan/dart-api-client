from pydantic import BaseModel, Field
from typing import Optional, List

class Disclosure(BaseModel):
    """
    Model for a single disclosure entry.
    """
    corp_code: str = Field(..., description="DART corporation code")
    corp_name: str = Field(..., description="Corporation name")
    stock_code: Optional[str] = Field(None, description="Stock code")
    corp_cls: str = Field(..., description="Corporation class (Y/K/N/E)")
    report_nm: str = Field(..., description="Report title")
    rcept_no: str = Field(..., description="Receipt number")
    flr_nm: str = Field(..., description="Filer name")
    rcept_dt: str = Field(..., description="Receipt date (YYYYMMDD)")
    rm: str = Field(..., description="Remarks")

class DisclosureList(BaseModel):
    """
    Model for disclosure search response.
    """
    status: str
    message: str
    page_no: int
    page_count: int
    total_count: int
    total_page: int
    list: List[Disclosure] = []
