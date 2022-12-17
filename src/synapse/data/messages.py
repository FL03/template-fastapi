"""
    Appellation: messages
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from datetime import datetime
from pydantic import BaseModel


class Message(BaseModel):
    message: str
    timestamp: str

    def message(self) -> str:
        return self.message

    def timestamp(self) -> str:
        return self.timestamp

    def now() -> str:
        self.timestamp = str(datetime.now())
        return self.timestamp


class Status(BaseModel):
    message: str
