import json
import jwt

def decode_jwt(jwt):
    jwtDecoded = jwt.decode(jwtEncoded, algorithms=["HS256"], options={"verify_signature": False})
    return jwtDecoded

