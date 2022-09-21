"""
    Appellation: tokens
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from typing import Optional

from pydantic import BaseModel


class TokenPayload(BaseModel):
    access_token: str
    token_type: str
    username: Optional[str]
