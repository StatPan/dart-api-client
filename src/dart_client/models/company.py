from typing import Optional
from pydantic import BaseModel, Field

class Company(BaseModel):
    """
    기업개황 정보 (get_company)
    """
    status: str = Field(..., description="에러 및 정보 코드")
    message: str = Field(..., description="에러 및 정보 메시지")
    corp_code: Optional[str] = Field(None, description="고유번호")
    corp_name: Optional[str] = Field(None, description="정식명칭")
    corp_name_eng: Optional[str] = Field(None, description="영문명칭")
    stock_name: Optional[str] = Field(None, description="종목명(상장사)")
    stock_code: Optional[str] = Field(None, description="종목코드(상장사)")
    ceo_nm: Optional[str] = Field(None, description="대표자명")
    corp_cls: Optional[str] = Field(None, description="법인구분 (Y:유가, K:코스닥, N:코넥스, E:기타)")
    jurir_no: Optional[str] = Field(None, description="법인등록번호")
    bizr_no: Optional[str] = Field(None, description="사업자등록번호")
    adres: Optional[str] = Field(None, description="주소")
    hm_url: Optional[str] = Field(None, description="홈페이지")
    ir_url: Optional[str] = Field(None, description="IR홈페이지")
    phn_no: Optional[str] = Field(None, description="전화번호")
    fax_no: Optional[str] = Field(None, description="팩스번호")
    induty_code: Optional[str] = Field(None, description="업종코드")
    est_dt: Optional[str] = Field(None, description="설립일 (YYYYMMDD)")
    acc_mt: Optional[str] = Field(None, description="결산월 (MM)")
