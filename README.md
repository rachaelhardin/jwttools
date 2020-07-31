# jwttools

Simple, automated JWT cracking and generation. This is mostly for my own regular use but should be useful in CTFs or a bug bounty.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

None currently

### Installing

Install via pip!

```
pip install -r requirements.txt
```

## Usage 

Cracking:
```
python jwtbruteforce.py
Script to brute-force JWT secret key
Enter encoded payload: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.0rETNLc3NM8P2xMYUmSK1MDl_YfUABXHl2LdIYvqmQc
Enter wordlist: ./sample_wordlist
Invalid Token ... [123456]
Invalid Token ... [12345]
Invalid Token ... [123456789]
Invalid Token ... [password]
Invalid Token ... [iloveyou]
Success! Token decoded with ... [princess]
```

Generating:
```
python jwtbruteforce.py
Script to generate a new JWT
Enter a username: rachael
Enter the JWT secret key: secret
Your new JWT is:
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicmFjaGFlbCIsImlhdCI6MTU5NjE1NDMzNiwiZXhwIjoxNTk2MTU0Njk2fQ.t74_P8KnG6VlAg6GtoKdAYaPgMfUsNkNBOCUOIi5Mv4
```

## Contributing

If you have something, go ahead ond set up a PR.
