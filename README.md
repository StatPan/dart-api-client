# dart-api-client

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

DART(Data Analysis, Retrieval and Transfer System) API를 위한 비동기 Python 클라이언트 라이브러리입니다.

## 특징

- ✨ **비동기 우선**: `asyncio`와 `httpx` 기반 고성능 비동기 요청
- 🔒 **타입 안전성**: Pydantic 모델과 타입 힌트로 IDE 자동완성 지원
- 🚀 **83개 API 자동 생성**: YAML 스펙에서 모든 DART API 메서드 자동 생성
- ⚡ **Rate Limiting**: 클라이언트 측 요청 제한으로 API 한도 관리
- 📝 **상세한 문서화**: 각 메서드마다 파라미터 설명 포함
- 🧪 **검증 완료**: 실제 DART API로 테스트 완료

## 설치

```bash
pip install dart-api-client
```

또는 개발 버전:

```bash
git clone https://github.com/statpan/dart-api-client.git
cd dart-api-client
pip install -e .
```

## 빠른 시작

### 1. API 키 설정

환경변수에 DART API 키를 설정하거나:

```bash
export DART_API_KEY="your_api_key_here"
```

코드에서 직접 전달:

```python
from dart_client import DartAPIClient

client = DartAPIClient(api_key="your_api_key_here")
```

### 2. 기본 사용법

```python
import asyncio
from dart_client import DartAPIClient

async def main():
    async with DartAPIClient() as client:
        # 고유번호(기업 코드) 조회
        corp_codes = await client.get_corp_code()
        print(f"✅ {len(corp_codes):,}개 기업 코드 다운로드")
        print(f"예시: {corp_codes[0].corp_name} ({corp_codes[0].corp_code})")
        
        # 기업정보 조회
        company = await client.get_company(corp_code="00126380")
        print(f"✅ 기업명: {company['corp_name']}")
        
        # 공시검색
        disclosures = await client.get_list(
            corp_code="00126380",
            bgn_de="20240101",
            end_de="20240131",
            page_count=10
        )
        print(f"✅ 공시 {disclosures['total_count']}건 검색")

if __name__ == "__main__":
    asyncio.run(main())
```

## 주요 기능

### 1. 기업 정보 조회

```python
# 고유번호 전체 다운로드 (ZIP/XML 자동 처리)
corp_codes = await client.get_corp_code()

# 특정 기업 정보
company_info = await client.get_company(corp_code="00126380")
```

### 2. 공시 검색

```python
# 기간별 공시 검색
disclosures = await client.get_list(
    corp_code="00126380",      # 삼성전자
    bgn_de="20240101",         # 시작일
    end_de="20241231",         # 종료일
    pblntf_ty="A",             # 정기공시
    page_no=1,
    page_count=100
)

for item in disclosures['list']:
    print(f"[{item['rcept_dt']}] {item['report_nm']}")
```

### 3. 재무제표 조회

```python
# 단일회사 재무제표
financials = await client.get_fnltt_singl_acnt(
    corp_code="00126380",
    bsns_year="2023",
    reprt_code="11011"  # 사업보고서
)

# 다중회사 비교
multi_financials = await client.get_fnltt_multi_acnt(
    corp_code="00126380,00164779",  # 여러 기업 동시 조회
    bsns_year="2023",
    reprt_code="11011"
)
```

### 4. 주주 정보

```python
# 최대주주 현황
shareholders = await client.get_hyslr_sttus(
    corp_code="00126380",
    bsns_year="2023",
    reprt_code="11011"
)

# 소액주주 현황
minor_shareholders = await client.get_mrhl_sttus(
    corp_code="00126380",
    bsns_year="2023",
    reprt_code="11011"
)
```

### 5. 임원 정보

```python
# 임원 현황
executives = await client.get_exctv_sttus(
    corp_code="00126380",
    bsns_year="2023",
    reprt_code="11011"
)

# 임원 보수 현황
exec_pay = await client.get_hmv_audit_all_sttus(
    corp_code="00126380",
    bsns_year="2023",
    reprt_code="11011"
)
```

## API 그룹

라이브러리는 83개의 DART API를 6개 그룹으로 제공합니다:

### DS001 - 기본 조회 (4개 API)
- `get_list`: 공시검색
- `get_company`: 기업개황
- `get_api_2019003`: 공시서류 원본파일
- `get_api_2019018`: 고유번호 (또는 `get_corp_code`)

### DS002 - 정기보고서 (28개 API)
자본금, 배당, 주주, 임원, 직원, 보수, 감사 등

### DS003 - 재무제표 (7개 API)
단일/다중 재무제표, XBRL, 재무지표 등

### DS004 - 지분공시 (2개 API)
대량보유, 임원/주요주주 소유보고

### DS005 - 주요사항 (36개 API)
유무상증자, 합병/분할, 자기주식, 소송 등

### DS006 - 증권신고서 (6개 API)
지분증권, 채무증권, 합병, 분할 등

## 고급 사용법

### Rate Limiting 조정

```python
# 분당 요청 수 제한 (기본값: 100)
client = DartAPIClient(requests_per_minute=300)
```

### 에러 처리

```python
from dart_client.errors import DartAPIError, DartLimitError, DartAuthError

try:
    result = await client.get_company(corp_code="00126380")
except DartAuthError as e:
    print(f"인증 오류: {e.message}")
except DartLimitError as e:
    print(f"API 한도 초과: {e.message}")
except DartAPIError as e:
    print(f"API 오류 [{e.code}]: {e.message}")
```

### 동기 코드에서 사용

```python
import asyncio

def get_company_sync(corp_code):
    async def _fetch():
        async with DartAPIClient() as client:
            return await client.get_company(corp_code=corp_code)
    
    return asyncio.run(_fetch())

company = get_company_sync("00126380")
```

## 파라미터 참고

### 보고서 코드 (reprt_code)
- `11011`: 사업보고서
- `11012`: 반기보고서
- `11013`: 1분기보고서
- `11014`: 3분기보고서

### 법인구분 (corp_cls)
- `Y`: 유가증권시장
- `K`: 코스닥
- `N`: 코넥스
- `E`: 기타

### 날짜 형식
- `YYYYMMDD`: 예) `20240101`

## 개발

### 테스트

```bash
# 전체 테스트
uv run pytest

# Fixture 기반 테스트
uv run pytest tests/test_with_fixtures.py -v

# 실제 API 테스트 (DART_API_KEY 필요)
uv run tests/test_integration_real.py
```

### 코드 생성

YAML 스펙이 업데이트되면:

```bash
uv run scripts/generate_client.py
```

## 라이선스

MIT License

## 기여

이슈와 PR을 환영합니다!

## 관련 링크

- [DART 오픈API 가이드](https://opendart.fss.or.kr/guide/main.do)
- [DART API 명세서](https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019001)
