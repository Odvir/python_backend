import json
import jwt

def decode_jwt(filename):
    file = open(filename, "r")
    jwtEncoded = file.read()
    file.close()
    jwtDecoded = jwt.decode(jwtEncoded, algorithms=["HS256"], options={"verify_signature": False})
    return jwtDecoded

