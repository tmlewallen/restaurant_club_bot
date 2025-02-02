from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Response:
    status: Optional[int] = 200
    payload: Optional[Dict] = None
