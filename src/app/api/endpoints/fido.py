"""
    Appellation: auth
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from fastapi import APIRouter, Depends, HTTPException, Security, status
from fido2.webauthn import PublicKeyCredentialRpEntity, PublicKeyCredentialUserEntity
from fido2.server import Fido2Server
from tortoise.contrib.fastapi import HTTPNotFoundError

from app import core
from app.data.models import User, UserIn, Users, Token, TokenIn

import fido2.features

fido2.features.webauthn_json_mapping.enabled = True
# Create a new router for the service
router = APIRouter(prefix="/fido", tags=['auth', 'fido'])
# Call the cached session instance
session = core.session()

rp = PublicKeyCredentialRpEntity(name="FIDO Server", id="localhost")
server = Fido2Server(rp)


@router.get("/")
async def index():
    return { "message": "FIDO Router" }


@router.post("/register")
async def registration() -> dict:
    options, state = server.register_begin(
        PublicKeyCredentialUserEntity(
            id=b"user_id",
            name="a_user",
            display_name="A. User",
        ),
        credentials,
        user_verification="discouraged",
        authenticator_attachment="cross-platform",
    )
    # 
    session.state = state

    return dict(options)


@router.post("/register/redirect")
async def register_complete() -> dict:
    response = request.json
    print("RegistrationResponse:", response)
    auth_data = server.register_complete(session["state"], response)

    credentials.append(auth_data.credential_data)
    print("REGISTERED CREDENTIAL:", auth_data.credential_data)
    return {"status": "OK"}


@router.post("/auth", responses={404: dict(model=HTTPNotFoundError)})
async def authenticate_begin():
    if not credentials:
        abort(404)

    options, state = server.authenticate_begin(credentials)
    session.state = state

    return jsonify(dict(options))


@router.post("/auth/redirect", responses={404: dict(model=HTTPNotFoundError)})
async def authenticate_complete():
    if not credentials:
        abort(404)

    response = request.json
    print("AuthenticationResponse:", response)
    server.authenticate_complete(
        session.state,
        credentials,
        response,
    )
    print("ASSERTION OK")
    return {"status": "OK"}
