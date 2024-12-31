from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Students(BaseModel):
    id: int
    user_name: str


class ReadStudents(BaseModel):
    id: int
    user_name: str
    class Config:
        from_attributes = True


