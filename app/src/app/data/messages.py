"""
    Appellation: messages
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from pydantic import BaseModel


class Status(BaseModel):
    message: str
