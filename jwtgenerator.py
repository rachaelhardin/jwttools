#!/usr/bin/python
# Short script to generate a new JWT with a new user and a signing key

import jwt
from datetime import datetime, timedelta

print("Script to generate a new JWT")
username = input("Enter a username: ")
secret = input("Enter the JWT secret key: ")

raw_payload = {
    "user" : username,
    "iat" : datetime.utcnow(),
    "exp" : datetime.utcnow() + timedelta(seconds=360)
}

payload = jwt.encode(raw_payload, secret, algorithm='HS256')
print("Your new JWT is:")
print(str(payload, "utf-8"))
