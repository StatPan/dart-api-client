import yaml
import re
from pathlib import Path
from typing import Any, Dict, List

# Configuration
SCRIPT_DIR = Path(__file__).parent
CONFIG_DIR = SCRIPT_DIR.parent.parent / "configs" / "dart"
OUTPUT_DIR = SCRIPT_DIR.parent / "src" / "dart_client" / "generated"
MODELS_FILE = OUTPUT_DIR / "models.py"
API_FILE = OUTPUT_DIR / "api.py"

def to_camel_case(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def to_pascal_case(snake_str: str) -> str:
    return snake_str.replace("_", " ").title().replace(" ", "")

def load_specs() -> Dict[str, List[Dict[str, Any]]]:
    specs = {}
    for yaml_file in sorted(CONFIG_DIR.glob("ds*.yaml")):
        group_code = yaml_file.stem
        with open(yaml_file, "r") as f:
            data = yaml.safe_load(f)
            if "apis" in data:
                specs[group_code] = data["apis"]
    return specs

def generate_models(specs: Dict[str, List[Dict[str, Any]]]):
    lines = [
        "from pydantic import BaseModel, Field",
        "from typing import Optional, List, Any, Dict",
        "",
        "class DartResponse(BaseModel):",
        "    status: str",
        "    message: str",
        "    list: List[Dict[str, Any]] = []",
        "",
    ]
    
    # We could generate specific input models here if we wanted strict validation objects
    # For now, we'll rely on method arguments in the API class
    
    with open(MODELS_FILE, "w") as f:
        f.write("\n".join(lines))
    print(f"Generated {MODELS_FILE}")

def generate_api(specs: Dict[str, List[Dict[str, Any]]]):
    # Common parameter descriptions
    PARAM_DESCRIPTIONS = {
        "corp_code": "기업 고유번호 (8자리)",
        "bsns_year": "사업연도 (YYYY)",
        "reprt_code": "보고서 코드 (11011=사업보고서, 11012=반기, 11013=1분기, 11014=3분기)",
        "rcept_no": "접수번호 (14자리)",
        "bgn_de": "시작일 (YYYYMMDD)",
        "end_de": "종료일 (YYYYMMDD)",
        "last_reprt_at": "최종보고서 검색여부 (Y/N)",
        "pblntf_ty": "공시유형",
        "pblntf_detail_ty": "공시상세유형",
        "corp_cls": "법인구분 (Y=유가, K=코스닥, N=코넥스, E=기타)",
        "sort": "정렬 (date=접수일, crp=회사명, rpt=보고서명)",
        "sort_mth": "정렬방법 (asc=오름차순, desc=내림차순)",
        "page_no": "페이지 번호",
        "page_count": "페이지당 건수 (최대 100)",
        "fs_div": "개별/연결구분 (CFS=연결, OFS=개별)",
        "sj_div": "재무제표구분 (BS=재무상태표, IS=손익계산서, etc)",
        "idx_cl_code": "지표구분코드",
    }
    
    lines = [
        "from typing import Optional, Any, Dict, Union",
        "from ..models.corp_code import CorpCode",
        "from ..models.disclosure import DisclosureList",
        "",
        "class GeneratedDartAPIMixin:",
        "    \"\"\"",
        "    Auto-generated API methods from YAML specifications.",
        "    \"\"\"",
        "    async def request(self, endpoint: str, params: Dict[str, Any] | None = None) -> Any:",
        "        raise NotImplementedError(\"Mixin expects 'request' method to be implemented by host class\")",
        ""
    ]

    for group, apis in specs.items():
        lines.append(f"    # --- Group {group.upper()} ---")
        
        for api in apis:
            api_id = api["id"]
            name = api["name"]
            # Remove /api/ prefix if present, then strip leading slash
            endpoint = api["endpoint"].lstrip("/")
            if endpoint.startswith("api/"):
                endpoint = endpoint[4:]  # Remove 'api/' prefix
            dataset = api.get("dataset", api_id)
            method_name = f"get_{api_id}" if not api_id.startswith("get_") else api_id
            
            # Special case naming for some known IDs to be friendlier?
            # For now, use ID as is (snake_case from YAML)
            
            params = api.get("params", {})
            required = params.get("required", {}) or {}
            optional = params.get("optional", {}) or {}
            
            # Build enhanced docstring
            docstring_parts = [
                f'"""',
                f"{name}",
                "",
            ]
            
            if "notes" in api and api["notes"]:
                docstring_parts.append(api["notes"].strip())
                docstring_parts.append("")
            
            docstring_parts.append(f"Endpoint: {endpoint}")
            docstring_parts.append(f"Dataset: {dataset}")
            docstring_parts.append(f"Group: {group.upper()}")
            
            # Add Args section if there are parameters
            all_params_list = list(required.keys()) + list(optional.keys())
            if all_params_list:
                docstring_parts.append("")
                docstring_parts.append("Args:")
                for param in all_params_list:
                    desc = PARAM_DESCRIPTIONS.get(param, param)
                    docstring_parts.append(f"    {param}: {desc}")
            
            docstring_parts.append('"""')
            
            # Indent docstring properly
            docstring = "\n        ".join(docstring_parts)

            # Build arguments
            args = ["self"]
            
            # Required args
            for param in required.keys():
                # Type inference could be better, but most DART params are strings
                # except page_no, page_count which are ints
                py_type = "str"
                if param in ["page_no", "page_count"]:
                    py_type = "int"
                args.append(f"{param}: {py_type}")
            
            # Optional args
            for param in optional.keys():
                py_type = "Optional[str]"
                default = "None"
                if param in ["page_no", "page_count"]:
                    py_type = "int"
                    default = "1" if param == "page_no" else "100"
                args.append(f"{param}: {py_type} = {default}")

            args_str = ", ".join(args)
            
            # Method body
            lines.append(f"    async def {method_name}({args_str}) -> Dict[str, Any]:")
            lines.append(f"        {docstring}")
            lines.append(f"        params = {{")
            
            for param in all_params_list:
                lines.append(f'            "{param}": {param},')
            lines.append(f"        }}")
            lines.append(f"        # Filter None values")
            lines.append(f"        params = {{k: v for k, v in params.items() if v is not None}}")
            lines.append(f'        return await self.request("{endpoint}", params)')
            lines.append("")

    with open(API_FILE, "w") as f:
        f.write("\n".join(lines))
    print(f"Generated {API_FILE}")

def main():
    specs = load_specs()
    generate_models(specs)
    generate_api(specs)

if __name__ == "__main__":
    main()
