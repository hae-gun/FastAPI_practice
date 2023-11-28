from typing import List, Dict

from pydantic import BaseModel


class CreateToDoRequest(BaseModel):
    contents: str
    is_done: bool


class Params(BaseModel):
    mode: str
    mid: str
    sid1: str


class CrawlingRequest(BaseModel):
    url: str
    params: Params

