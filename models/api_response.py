from dataclasses import dataclass
from typing import Any, Optional

#################################################################
# API Response Class
#################################################################

@dataclass
class APIResponse:
    success: bool
    message: str = ""
    data: Optional[Any] = None

    # Convert this into a dictionary
    def to_dict(self):
        return {
            'success': self.success,
            'message': self.message,
            'data': self.data
        }