from pydantic import BaseModel, HttpUrl

from typing import Sequence

class Record(BaseModel):
    ''' model for Record'''

    id: int
    label: str
    source: str
    url: HttpUrl

class RecordSearchResults(BaseModel):
    results: Sequence[Record]

class RecordCreate(BaseModel):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int