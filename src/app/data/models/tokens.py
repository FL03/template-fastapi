"""
    Appellation: tokens
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Tokens(Model):
    id = fields.CharField(max_length=256, pk=True)
    access_token = fields.CharField(max_length=256, null=False)
    token_type = fields.CharField(max_length=128, null=True)
    username = fields.CharField(max_length=128, null=True)

    class Meta:
        computed = []
        exclude = []


Token = pydantic_model_creator(Tokens, name="Token")
TokenIn = pydantic_model_creator(Tokens, exclude_readonly=True, name="TokenIn")
