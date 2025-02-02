from dataclasses import dataclass
from typing import Dict, Optional
from dataclasses_json import LetterCase, dataclass_json


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class HttpData:
    method: str
    path: str
    protocol: str
    source_ip: str
    user_agent: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class RequestContext:
    http: HttpData


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UrlInvocation:
    headers: Dict[str, str]
    request_context: RequestContext
    is_base_64_encoded: bool
    query_string_parameters: Optional[Dict[str, str]] = None
    body: Optional[str] = None
