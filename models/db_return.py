
from dataclasses import dataclass
from typing import (
    List,
    Tuple,
    Any,
    Optional
)

@dataclass
class DBReturn:
    columns: Tuple[str, ...]
    rows: Optional[List[Tuple[Any,... ]]]
    row: Optional[Tuple[Any, ...]]
    row_count: int
    