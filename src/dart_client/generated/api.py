from typing import Optional, Any, Dict, Union, List
from ..models.corp_code import CorpCode
from ..models.disclosure import DisclosureList
from ..models.company import Company

class GeneratedDartAPIMixin:
    """
    Auto-generated API methods from YAML specifications.
    """
    async def get_corp_codes(self) -> List[CorpCode]:
        """
        Helper to get corporation codes as a list of CorpCode objects.
        This is a wrapper around get_corp_code() which handles the XML/ZIP logic internally.
        """
        return await self.get_corp_code()

    # --- Generated Methods Below ---
    async def request(self, endpoint: str, params: Dict[str, Any] | None = None) -> Any:
        raise NotImplementedError("Mixin expects 'request' method to be implemented by host class")

    # --- Group DS001 ---
    async def get_list(self, corp_code: Optional[str] = None, bgn_de: Optional[str] = None, end_de: Optional[str] = None, last_reprt_at: Optional[str] = None, pblntf_ty: Optional[str] = None, pblntf_detail_ty: Optional[str] = None, corp_cls: Optional[str] = None, sort: Optional[str] = None, sort_mth: Optional[str] = None, page_no: Optional[int] = None, page_count: Optional[int] = None) -> DisclosureList:
        """
        공시검색
        
        DART에 등록되어있는 공시보고서의 목록 및 상세정보를 제공합니다.
        
        Endpoint: list.json
        Dataset: list
        Group: DS001
        
        Args:
            corp_code (str): 공시대상회사의 고유번호(8자리)
            bgn_de (str): 검색시작일자(YYYYMMDD)
            end_de (str): 검색종료일자(YYYYMMDD)
            last_reprt_at (str): 최종보고서 검색여부(Y or N)
            pblntf_ty (str): 공시유형
            pblntf_detail_ty (str): 공시상세유형
            corp_cls (str): 법인구분
            sort (str): 정렬(date: 접수일자, crp: 회사명, rpt: 보고서명)
            sort_mth (str): 정렬방법(desc: 내림차순, asc: 오름차순)
            page_no (int): 페이지 번호(1~n)
            page_count (int): 페이지 건수(1~100)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
            "last_reprt_at": last_reprt_at,
            "pblntf_ty": pblntf_ty,
            "pblntf_detail_ty": pblntf_detail_ty,
            "corp_cls": corp_cls,
            "sort": sort,
            "sort_mth": sort_mth,
            "page_no": page_no,
            "page_count": page_count,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        response = await self.request("list.json", params)
        return DisclosureList(**response)

    async def get_company(self, corp_code: str) -> Company:
        """
        기업개황
        
        DART에 등록되어있는 공시대상회사의 기업개황 정보를 제공합니다.
        
        Endpoint: company.json
        Dataset: company
        Group: DS001
        
        Args:
            corp_code (str): 공시대상회사의 고유번호(8자리)
        """
        params = {
            "corp_code": corp_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        response = await self.request("company.json", params)
        return Company(**response)

    async def get_api_2019003(self, rcept_no: str) -> Dict[str, Any]:
        """
        공시서류원본파일
        
        공시보고서 원본파일을 제공합니다. (ZIP 형식 반환)
        
        Endpoint: document.xml
        Dataset: api_2019003
        Group: DS001
        
        Args:
            rcept_no: 접수번호 (14자리)
        """
        params = {
            "rcept_no": rcept_no,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("document.xml", params)

    async def get_api_2019018(self) -> Dict[str, Any]:
        """
        고유번호
        
        DART에 등록되어있는 공시대상회사의 고유번호,회사명,종목코드, 최근변경일자를 파일로 제공합니다. (ZIP 형식 반환)
        
        Endpoint: corpCode.xml
        Dataset: api_2019018
        Group: DS001
        """
        params = {
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("corpCode.xml", params)

    # --- Group DS002 ---
    async def get_irds_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        증자(감자) 현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 증자(감자) 현황을 제공합니다.
        
        Endpoint: irdsSttus.json
        Dataset: irds_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("irdsSttus.json", params)

    async def get_alot_matter(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        배당에 관한 사항
        
        정기보고서(사업, 분기, 반기보고서) 내에 배당에 관한 사항을 제공합니다.
        
        Endpoint: alotMatter.json
        Dataset: alot_matter
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("alotMatter.json", params)

    async def get_tesstk_acqs_dsps_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        자기주식 취득 및 처분 현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 자기주식 취득 및 처분 현황을 제공합니다.
        
        Endpoint: tesstkAcqsDspsSttus.json
        Dataset: tesstk_acqs_dsps_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("tesstkAcqsDspsSttus.json", params)

    async def get_hyslr_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        최대주주 현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 최대주주 현황을 제공합니다.
        
        Endpoint: hyslrSttus.json
        Dataset: hyslr_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("hyslrSttus.json", params)

    async def get_hyslr_chg_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        최대주주 변동현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 최대주주 변동현황을 제공합니다.
        
        Endpoint: hyslrChgSttus.json
        Dataset: hyslr_chg_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("hyslrChgSttus.json", params)

    async def get_mrhl_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        소액주주 현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 소액주주 현황을 제공합니다.
        
        Endpoint: mrhlSttus.json
        Dataset: mrhl_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("mrhlSttus.json", params)

    async def get_exctv_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        임원 현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 임원 현황을 제공합니다.
        
        Endpoint: exctvSttus.json
        Dataset: exctv_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("exctvSttus.json", params)

    async def get_emp_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        직원 현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 직원 현황을 제공합니다.
        
        Endpoint: empSttus.json
        Dataset: emp_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("empSttus.json", params)

    async def get_hmv_audit_indvdl_by_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        이사·감사의 개인별 보수현황(5억원 이상)
        
        정기보고서(사업, 분기, 반기보고서) 내에 이사·감사의 개인별 보수현황(5억원 이상)을 제공합니다.
        
        Endpoint: hmvAuditIndvdlBySttus.json
        Dataset: hmv_audit_indvdl_by_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("hmvAuditIndvdlBySttus.json", params)

    async def get_hmv_audit_all_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        이사·감사 전체의 보수현황(보수지급금액 - 이사·감사 전체)
        
        정기보고서(사업, 분기, 반기보고서) 내에 이사·감사 전체의 보수현황(보수지급금액 - 이사·감사 전체)을 제공합니다.
        
        Endpoint: hmvAuditAllSttus.json
        Dataset: hmv_audit_all_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("hmvAuditAllSttus.json", params)

    async def get_indvdl_by_pay(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        개인별 보수지급 금액(5억이상 상위5인)
        
        정기보고서(사업, 분기, 반기보고서) 내에 개인별 보수지급 금액(5억이상 상위5인)을 제공합니다.
        
        Endpoint: indvdlByPay.json
        Dataset: indvdl_by_pay
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("indvdlByPay.json", params)

    async def get_otr_cpr_invstmnt_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        타법인 출자현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 타법인 출자현황을 제공합니다.
        
        Endpoint: otrCprInvstmntSttus.json
        Dataset: otr_cpr_invstmnt_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("otrCprInvstmntSttus.json", params)

    async def get_stock_totqy_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        주식의 총수 현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 주식의총수현황을 제공합니다.
        
        Endpoint: stockTotqySttus.json
        Dataset: stock_totqy_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("stockTotqySttus.json", params)

    async def get_det_scrits_isu_acmslt(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        채무증권 발행실적
        
        정기보고서(사업, 분기, 반기보고서) 내에 채무증권 발행실적을 제공합니다.
        
        Endpoint: detScritsIsuAcmslt.json
        Dataset: det_scrits_isu_acmslt
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("detScritsIsuAcmslt.json", params)

    async def get_entrprs_bil_scrits_nrdmp_blce(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        기업어음증권 미상환 잔액
        
        정기보고서(사업, 분기, 반기보고서) 내에 기업어음증권 미상환 잔액을 제공합니다.
        
        Endpoint: entrprsBilScritsNrdmpBlce.json
        Dataset: entrprs_bil_scrits_nrdmp_blce
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("entrprsBilScritsNrdmpBlce.json", params)

    async def get_srtpd_psndbt_nrdmp_blce(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        단기사채 미상환 잔액
        
        정기보고서(사업, 분기, 반기보고서) 내에 단기사채 미상환 잔액을 제공합니다.
        
        Endpoint: srtpdPsndbtNrdmpBlce.json
        Dataset: srtpd_psndbt_nrdmp_blce
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("srtpdPsndbtNrdmpBlce.json", params)

    async def get_cprnd_nrdmp_blce(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        회사채 미상환 잔액
        
        정기보고서(사업, 분기, 반기보고서) 내에 회사채 미상환 잔액을 제공합니다.
        
        Endpoint: cprndNrdmpBlce.json
        Dataset: cprnd_nrdmp_blce
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("cprndNrdmpBlce.json", params)

    async def get_new_capl_scrits_nrdmp_blce(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        신종자본증권 미상환 잔액
        
        정기보고서(사업, 분기, 반기보고서) 내에 신종자본증권 미상환 잔액을 제공합니다.
        
        Endpoint: newCaplScritsNrdmpBlce.json
        Dataset: new_capl_scrits_nrdmp_blce
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("newCaplScritsNrdmpBlce.json", params)

    async def get_cndl_capl_scrits_nrdmp_blce(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        조건부 자본증권 미상환 잔액
        
        정기보고서(사업, 분기, 반기보고서) 내에 조건부 자본증권 미상환 잔액을 제공합니다.
        
        Endpoint: cndlCaplScritsNrdmpBlce.json
        Dataset: cndl_capl_scrits_nrdmp_blce
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("cndlCaplScritsNrdmpBlce.json", params)

    async def get_accnut_adtor_nm_nd_adt_opinion(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        회계감사인의 명칭 및 감사의견
        
        정기보고서(사업, 분기, 반기보고서) 내에 회계감사인의 명칭 및 감사의견을 제공합니다.
        
        Endpoint: accnutAdtorNmNdAdtOpinion.json
        Dataset: accnut_adtor_nm_nd_adt_opinion
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("accnutAdtorNmNdAdtOpinion.json", params)

    async def get_adt_servc_cncls_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        감사용역체결현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 감사용역체결현황을 제공합니다.
        
        Endpoint: adtServcCnclsSttus.json
        Dataset: adt_servc_cncls_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("adtServcCnclsSttus.json", params)

    async def get_accnut_adtor_non_adt_servc_cncls_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        회계감사인과의 비감사용역 계약체결 현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 회계감사인과의 비감사용역 계약체결 현황을 제공합니다.
        
        Endpoint: accnutAdtorNonAdtServcCnclsSttus.json
        Dataset: accnut_adtor_non_adt_servc_cncls_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("accnutAdtorNonAdtServcCnclsSttus.json", params)

    async def get_outcmpny_drctr_nd_change_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        사외이사 및 그 변동현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 사외이사 및 그 변동현황을 제공합니다.
        
        Endpoint: outcmpnyDrctrNdChangeSttus.json
        Dataset: outcmpny_drctr_nd_change_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("outcmpnyDrctrNdChangeSttus.json", params)

    async def get_unrst_exctv_mendng_sttus(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        미등기임원 보수현황
        
        정기보고서(사업, 분기, 반기보고서) 내에 미등기임원 보수현황을 제공합니다.
        
        Endpoint: unrstExctvMendngSttus.json
        Dataset: unrst_exctv_mendng_sttus
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("unrstExctvMendngSttus.json", params)

    async def get_drctr_adt_all_mendng_sttus_gmtsck_confm_amount(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        이사·감사 전체의 보수현황(주주총회 승인금액)
        
        정기보고서(사업, 분기, 반기보고서) 내에 이사·감사 전체의 보수현황(주주총회 승인금액)을 제공합니다.
        
        Endpoint: drctrAdtAllMendngSttusGmtsckConfmAmount.json
        Dataset: drctr_adt_all_mendng_sttus_gmtsck_confm_amount
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("drctrAdtAllMendngSttusGmtsckConfmAmount.json", params)

    async def get_drctr_adt_all_mendng_sttus_mendng_pymntamt_ty_cl(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        이사·감사 전체의 보수현황(보수지급금액 - 유형별)
        
        정기보고서(사업, 분기, 반기보고서) 내에 이사·감사 전체의 보수현황(보수지급금액 - 유형별)을 제공합니다.
        
        Endpoint: drctrAdtAllMendngSttusMendngPymntamtTyCl.json
        Dataset: drctr_adt_all_mendng_sttus_mendng_pymntamt_ty_cl
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("drctrAdtAllMendngSttusMendngPymntamtTyCl.json", params)

    async def get_pssrp_cptal_use_dtls(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        공모자금의 사용내역
        
        정기보고서(사업, 분기, 반기보고서) 내에 공모자금의 사용내역을 제공합니다.
        
        Endpoint: pssrpCptalUseDtls.json
        Dataset: pssrp_cptal_use_dtls
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("pssrpCptalUseDtls.json", params)

    async def get_prvsrp_cptal_use_dtls(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        사모자금의 사용내역
        
        정기보고서(사업, 분기, 반기보고서) 내에 사모자금의 사용내역을 제공합니다.
        
        Endpoint: prvsrpCptalUseDtls.json
        Dataset: prvsrp_cptal_use_dtls
        Group: DS002
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("prvsrpCptalUseDtls.json", params)

    # --- Group DS003 ---
    async def get_fnltt_singl_acnt(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        단일회사 주요계정
        
        상장법인(유가증권, 코스닥) 및 주요 비상장법인(사업보고서 제출대상 &amp; IFRS 적용)이 제출한 정기보고서 내에 XBRL재무제표의 주요계정과목(재무상태표, 손익계산서)을 제공합니다.
        
        Endpoint: fnlttSinglAcnt.json
        Dataset: fnltt_singl_acnt
        Group: DS003
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("fnlttSinglAcnt.json", params)

    async def get_fnltt_multi_acnt(self, corp_code: str, bsns_year: str, reprt_code: str) -> Dict[str, Any]:
        """
        다중회사 주요계정
        
        상장법인(유가증권, 코스닥) 및 주요 비상장법인(사업보고서 제출대상 &amp; IFRS 적용)이 제출한 정기보고서 내에 XBRL재무제표의 주요계정과목(재무상태표, 손익계산서)을 제공합니다.
(대상법인 복수조회 복수조회 가능)
        
        Endpoint: fnlttMultiAcnt.json
        Dataset: fnltt_multi_acnt
        Group: DS003
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("fnlttMultiAcnt.json", params)

    async def get_api_2019019(self, rcept_no: str, reprt_code: str) -> Dict[str, Any]:
        """
        재무제표 원본파일(XBRL)
        
        상장법인(유가증권, 코스닥) 및 주요 비상장법인(사업보고서 제출대상 &amp; IFRS 적용)이 제출한 정기보고서 내에 XBRL재무제표의 원본파일(XBRL)을 제공합니다.
        
        Endpoint: api_2019019.json
        Dataset: api_2019019
        Group: DS003
        
        Args:
            rcept_no: 접수번호 (14자리)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
        """
        params = {
            "rcept_no": rcept_no,
            "reprt_code": reprt_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("api_2019019.json", params)

    async def get_fnltt_singl_acnt_all(self, corp_code: str, bsns_year: str, reprt_code: str, fs_div: str) -> Dict[str, Any]:
        """
        단일회사 전체 재무제표
        
        상장법인(유가증권, 코스닥) 및 주요 비상장법인(사업보고서 제출대상 &amp; IFRS 적용)이 제출한 정기보고서 내에 XBRL재무제표의 모든계정과목을 제공합니다.
        
        Endpoint: fnlttSinglAcntAll.json
        Dataset: fnltt_singl_acnt_all
        Group: DS003
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
            fs_div: 개별/연결구분 (CFS=연결, OFS=개별)
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
            "fs_div": fs_div,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("fnlttSinglAcntAll.json", params)

    async def get_xbrl_taxonomy(self, sj_div: str) -> Dict[str, Any]:
        """
        XBRL택사노미재무제표양식
        
        금융감독원 회계포탈에서 제공하는 IFRS 기반 XBRL 재무제표 공시용 표준계정과목체계(계정과목) 을 제공합니다.
        
        Endpoint: xbrlTaxonomy.json
        Dataset: xbrl_taxonomy
        Group: DS003
        
        Args:
            sj_div: 재무제표구분 (BS=재무상태표, IS=손익계산서, etc)
        """
        params = {
            "sj_div": sj_div,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("xbrlTaxonomy.json", params)

    async def get_fnltt_singl_indx(self, corp_code: str, bsns_year: str, reprt_code: str, idx_cl_code: str) -> Dict[str, Any]:
        """
        단일회사 주요 재무지표
        
        상장법인(유가증권, 코스닥) 및 주요 비상장법인(사업보고서 제출대상 &amp; IFRS 적용)이 제출한 정기보고서 내에 XBRL재무제표의 주요 재무지표를 제공합니다.
        
        Endpoint: fnlttSinglIndx.json
        Dataset: fnltt_singl_indx
        Group: DS003
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
            idx_cl_code: 지표구분코드
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
            "idx_cl_code": idx_cl_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("fnlttSinglIndx.json", params)

    async def get_fnltt_cmpny_indx(self, corp_code: str, bsns_year: str, reprt_code: str, idx_cl_code: str) -> Dict[str, Any]:
        """
        다중회사 주요 재무지표
        
        상장법인(유가증권, 코스닥) 및 주요 비상장법인(사업보고서 제출대상 &amp; IFRS 적용)이 제출한 정기보고서 내에 XBRL재무제표의 주요 재무지표를 제공합니다.(대상법인 복수조회 가능)
        
        Endpoint: fnlttCmpnyIndx.json
        Dataset: fnltt_cmpny_indx
        Group: DS003
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)
            idx_cl_code: 지표구분코드
        """
        params = {
            "corp_code": corp_code,
            "bsns_year": bsns_year,
            "reprt_code": reprt_code,
            "idx_cl_code": idx_cl_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("fnlttCmpnyIndx.json", params)

    # --- Group DS004 ---
    async def get_majorstock(self, corp_code: str) -> Dict[str, Any]:
        """
        대량보유 상황보고
        
        주식등의 대량보유상황보고서 내에 대량보유 상황보고 정보를 제공합니다.
        
        Endpoint: majorstock.json
        Dataset: majorstock
        Group: DS004
        
        Args:
            corp_code: 기업 고유번호 (8자리)
        """
        params = {
            "corp_code": corp_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("majorstock.json", params)

    async def get_elestock(self, corp_code: str) -> Dict[str, Any]:
        """
        임원ㆍ주요주주 소유보고
        
        임원ㆍ주요주주특정증권등 소유상황보고서 내에 임원ㆍ주요주주 소유보고
정보를 제공합니다.
        
        Endpoint: elestock.json
        Dataset: elestock
        Group: DS004
        
        Args:
            corp_code: 기업 고유번호 (8자리)
        """
        params = {
            "corp_code": corp_code,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("elestock.json", params)

    # --- Group DS005 ---
    async def get_ast_inhtrf_etc_ptbk_opt(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        자산양수도(기타), 풋백옵션
        
        주요사항보고서(자산양수도(기타), 풋백옵션) 내에 주요 정보를 제공합니다.
        
        Endpoint: astInhtrfEtcPtbkOpt.json
        Dataset: ast_inhtrf_etc_ptbk_opt
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("astInhtrfEtcPtbkOpt.json", params)

    async def get_df_ocr(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        부도발생
        
        주요사항보고서(부도발생) 내에 주요 정보를 제공합니다.
        
        Endpoint: dfOcr.json
        Dataset: df_ocr
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("dfOcr.json", params)

    async def get_bsn_sp(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        영업정지
        
        주요사항보고서(영업정지) 내에 주요 정보를 제공합니다.
        
        Endpoint: bsnSp.json
        Dataset: bsn_sp
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("bsnSp.json", params)

    async def get_ctrcvs_bgrq(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        회생절차 개시신청
        
        주요사항보고서(회생절차 개시신청) 내에 주요 정보를 제공합니다.
        
        Endpoint: ctrcvsBgrq.json
        Dataset: ctrcvs_bgrq
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("ctrcvsBgrq.json", params)

    async def get_ds_rs_ocr(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        해산사유 발생
        
        주요사항보고서(해산사유 발생) 내에 주요 정보를 제공합니다.
        
        Endpoint: dsRsOcr.json
        Dataset: ds_rs_ocr
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("dsRsOcr.json", params)

    async def get_piic_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        유상증자 결정
        
        주요사항보고서(유상증자 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: piicDecsn.json
        Dataset: piic_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("piicDecsn.json", params)

    async def get_fric_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        무상증자 결정
        
        주요사항보고서(무상증자 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: fricDecsn.json
        Dataset: fric_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("fricDecsn.json", params)

    async def get_pifric_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        유무상증자 결정
        
        주요사항보고서(유무상증자 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: pifricDecsn.json
        Dataset: pifric_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("pifricDecsn.json", params)

    async def get_cr_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        감자 결정
        
        주요사항보고서(감자 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: crDecsn.json
        Dataset: cr_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("crDecsn.json", params)

    async def get_bnk_mngt_pcbg(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        채권은행 등의 관리절차 개시
        
        주요사항보고서(채권은행 등의 관리절차 개시) 내에 주요 정보를 제공합니다.
        
        Endpoint: bnkMngtPcbg.json
        Dataset: bnk_mngt_pcbg
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("bnkMngtPcbg.json", params)

    async def get_lwst_lg(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        소송 등의 제기
        
        주요사항보고서(소송 등의 제기) 내에 주요 정보를 제공합니다.
        
        Endpoint: lwstLg.json
        Dataset: lwst_lg
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("lwstLg.json", params)

    async def get_ov_lst_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        해외 증권시장 주권등 상장 결정
        
        주요사항보고서(해외 증권시장 주권등 상장 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: ovLstDecsn.json
        Dataset: ov_lst_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("ovLstDecsn.json", params)

    async def get_ov_dlst_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        해외 증권시장 주권등 상장폐지 결정
        
        주요사항보고서(해외 증권시장 주권등 상장폐지 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: ovDlstDecsn.json
        Dataset: ov_dlst_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("ovDlstDecsn.json", params)

    async def get_ov_lst(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        해외 증권시장 주권등 상장
        
        주요사항보고서(해외 증권시장 주권등 상장) 내에 주요 정보를 제공합니다.
        
        Endpoint: ovLst.json
        Dataset: ov_lst
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("ovLst.json", params)

    async def get_ov_dlst(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        해외 증권시장 주권등 상장폐지
        
        주요사항보고서(해외 증권시장 주권등 상장폐지) 내에 주요 정보를 제공합니다.
        
        Endpoint: ovDlst.json
        Dataset: ov_dlst
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("ovDlst.json", params)

    async def get_cvbd_is_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        전환사채권 발행결정
        
        주요사항보고서(전환사채권 발행결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: cvbdIsDecsn.json
        Dataset: cvbd_is_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("cvbdIsDecsn.json", params)

    async def get_bdwt_is_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        신주인수권부사채권 발행결정
        
        주요사항보고서(신주인수권부사채권 발행결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: bdwtIsDecsn.json
        Dataset: bdwt_is_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("bdwtIsDecsn.json", params)

    async def get_exbd_is_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        교환사채권 발행결정
        
        주요사항보고서(교환사채권 발행결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: exbdIsDecsn.json
        Dataset: exbd_is_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("exbdIsDecsn.json", params)

    async def get_bnk_mngt_pcsp(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        채권은행 등의 관리절차 중단
        
        주요사항보고서(채권은행 등의 관리절차 중단) 내에 주요 정보를 제공합니다.
        
        Endpoint: bnkMngtPcsp.json
        Dataset: bnk_mngt_pcsp
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("bnkMngtPcsp.json", params)

    async def get_wd_cocobd_is_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        상각형 조건부자본증권 발행결정
        
        주요사항보고서(상각형 조건부자본증권 발행결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: wdCocobdIsDecsn.json
        Dataset: wd_cocobd_is_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("wdCocobdIsDecsn.json", params)

    async def get_tsstk_aq_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        자기주식 취득 결정
        
        주요사항보고서(자기주식 취득 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: tsstkAqDecsn.json
        Dataset: tsstk_aq_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("tsstkAqDecsn.json", params)

    async def get_tsstk_dp_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        자기주식 처분 결정
        
        주요사항보고서(자기주식 처분 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: tsstkDpDecsn.json
        Dataset: tsstk_dp_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("tsstkDpDecsn.json", params)

    async def get_tsstk_aq_trctr_cns_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        자기주식취득 신탁계약 체결 결정
        
        주요사항보고서(자기주식취득 신탁계약 체결 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: tsstkAqTrctrCnsDecsn.json
        Dataset: tsstk_aq_trctr_cns_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("tsstkAqTrctrCnsDecsn.json", params)

    async def get_tsstk_aq_trctr_cc_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        자기주식취득 신탁계약 해지 결정
        
        주요사항보고서(자기주식취득 신탁계약 해지 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: tsstkAqTrctrCcDecsn.json
        Dataset: tsstk_aq_trctr_cc_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("tsstkAqTrctrCcDecsn.json", params)

    async def get_bsn_inh_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        영업양수 결정
        
        주요사항보고서(영업양수 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: bsnInhDecsn.json
        Dataset: bsn_inh_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("bsnInhDecsn.json", params)

    async def get_bsn_trf_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        영업양도 결정
        
        주요사항보고서(영업양도 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: bsnTrfDecsn.json
        Dataset: bsn_trf_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("bsnTrfDecsn.json", params)

    async def get_tgast_inh_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        유형자산 양수 결정
        
        주요사항보고서(유형자산 양수 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: tgastInhDecsn.json
        Dataset: tgast_inh_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("tgastInhDecsn.json", params)

    async def get_tgast_trf_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        유형자산 양도 결정
        
        주요사항보고서(유형자산 양도 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: tgastTrfDecsn.json
        Dataset: tgast_trf_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("tgastTrfDecsn.json", params)

    async def get_otcpr_stk_invscr_inh_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        타법인 주식 및 출자증권 양수결정
        
        주요사항보고서(타법인 주식 및 출자증권 양수결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: otcprStkInvscrInhDecsn.json
        Dataset: otcpr_stk_invscr_inh_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("otcprStkInvscrInhDecsn.json", params)

    async def get_otcpr_stk_invscr_trf_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        타법인 주식 및 출자증권 양도결정
        
        주요사항보고서(타법인 주식 및 출자증권 양도결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: otcprStkInvscrTrfDecsn.json
        Dataset: otcpr_stk_invscr_trf_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("otcprStkInvscrTrfDecsn.json", params)

    async def get_stkrtbd_inh_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        주권 관련 사채권 양수 결정
        
        주요사항보고서(주권 관련 사채권 양수 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: stkrtbdInhDecsn.json
        Dataset: stkrtbd_inh_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("stkrtbdInhDecsn.json", params)

    async def get_stkrtbd_trf_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        주권 관련 사채권 양도 결정
        
        주요사항보고서(주권 관련 사채권 양도 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: stkrtbdTrfDecsn.json
        Dataset: stkrtbd_trf_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("stkrtbdTrfDecsn.json", params)

    async def get_cmp_mg_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        회사합병 결정
        
        주요사항보고서(회사합병 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: cmpMgDecsn.json
        Dataset: cmp_mg_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("cmpMgDecsn.json", params)

    async def get_cmp_dv_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        회사분할 결정
        
        주요사항보고서(회사분할 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: cmpDvDecsn.json
        Dataset: cmp_dv_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("cmpDvDecsn.json", params)

    async def get_cmp_dvmg_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        회사분할합병 결정
        
        주요사항보고서(회사분할합병 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: cmpDvmgDecsn.json
        Dataset: cmp_dvmg_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("cmpDvmgDecsn.json", params)

    async def get_stk_extr_decsn(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        주식교환·이전 결정
        
        주요사항보고서(주식교환·이전 결정) 내에 주요 정보를 제공합니다.
        
        Endpoint: stkExtrDecsn.json
        Dataset: stk_extr_decsn
        Group: DS005
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("stkExtrDecsn.json", params)

    # --- Group DS006 ---
    async def get_estk_rs(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        지분증권
        
        증권신고서(지분증권) 내에 요약 정보를 제공합니다.
        
        Endpoint: estkRs.json
        Dataset: estk_rs
        Group: DS006
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("estkRs.json", params)

    async def get_bd_rs(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        채무증권
        
        증권신고서(채무증권) 내에 요약 정보를 제공합니다.
        
        Endpoint: bdRs.json
        Dataset: bd_rs
        Group: DS006
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("bdRs.json", params)

    async def get_stkdp_rs(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        증권예탁증권
        
        증권신고서(증권예탁증권) 내에 요약 정보를 제공합니다.
        
        Endpoint: stkdpRs.json
        Dataset: stkdp_rs
        Group: DS006
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("stkdpRs.json", params)

    async def get_mg_rs(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        합병
        
        증권신고서(합병) 내에 요약 정보를 제공합니다.
        
        Endpoint: mgRs.json
        Dataset: mg_rs
        Group: DS006
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("mgRs.json", params)

    async def get_extr_rs(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        주식의포괄적교환·이전
        
        증권신고서(주식의포괄적교환·이전) 내에 요약 정보를 제공합니다.
        
        Endpoint: extrRs.json
        Dataset: extr_rs
        Group: DS006
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("extrRs.json", params)

    async def get_dv_rs(self, corp_code: str, bgn_de: str, end_de: str) -> Dict[str, Any]:
        """
        분할
        
        증권신고서(분할) 내에 요약 정보를 제공합니다.
        
        Endpoint: dvRs.json
        Dataset: dv_rs
        Group: DS006
        
        Args:
            corp_code: 기업 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
        """
        params = {
            "corp_code": corp_code,
            "bgn_de": bgn_de,
            "end_de": end_de,
        }
        # Filter None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self.request("dvRs.json", params)
