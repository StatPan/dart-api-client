from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class DartResponse(BaseModel):
    status: str
    message: str
    list: List[Dict[str, Any]] = []
