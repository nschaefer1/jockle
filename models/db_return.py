
from dataclasses import dataclass
from typing import (
    List,
    Tuple,
    Any,
    Optional
)

@dataclass
class DBReturn:
    success: bool
    columns: Optional[Tuple[str, ...]] = None
    rows: Optional[List[Tuple[Any,... ]]] = None
    row: Optional[Tuple[Any, ...]] = None
    row_count: Optional[int] = None
    