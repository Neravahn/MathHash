# MathHash - A Pure Math-Based 256-bit Hashing Engine

MathHash is a fully custom 256-bit hashing algorith written entirely in Python, using only mathematics, bitwise operations, and modular arithematic - no cryptographic libraries

It also inclues a simple password hashing API with random salts, making it easy for devlopers to use MathHash as a learning toop or experimental hashing engine.

⚠️ Disclaimer: MathHash is an educational hashing project. It is not a replacement for industry-standard cryptographic algorithms like Argon2, bcrypt, or SHA-256.


## FEATURES

#### Pure Python
- No dependencies. All math + bitwise logic written from scratch.

#### 256 bit hash output
- Produces a deterministic 32-bytes hash.

#### Salting built-in
- Automatic random 16-bytes salts for password hashing.

#### Easy to integrate
-Simple API:
```python
from mathhash import hash_password, verify_password
```


## INSTALLATION
```bash
pip install MathHash
```


## USAGE
Hash a password
```python
from mathhash import hash_password

hashed = hash_password('mypassword1234')
print(hashed)
```

Verify a password
```python
from mathhash import hash_password

is_valid = verify_password('mypassword1234', hashed)
print(is_valid)
```


## HOW IT WORKS (in short)
MathHash's engine mixes:
- modular addition
- modular multiplication
- left & right rotations
- nonlinear exponentation
- 64-bit word permutation
- round constants inpired by Feistel & sponge desgin


## PROJECT STRUCTURE 
**MathHash/**  
│  
├── **mathhash/**  
│   ├── `__init__.py`  
│   ├── `core.py`       # Password hashing & verification  
│   ├── `engine.py`     # Main 256-bit math hashing engine  
│   ├── `utils.py`      # Bit rotations & modular arithmetic  
│   └── `primes.py`     # Prime constants (optional)  
│  
├── **tests/**  
│   ├── `test_collision.py`  
│   ├── `test_avalanche.py`  
│   └── `test_basic.py`  
│  
├── `README.md`  
├── `LICENSE`  
└── `pyproject.toml`


## RUNNING TESTS
Install pytest:
```bash
pip install pytest
```
Run test
```bash
pytest
```
Includes tests:
- Random collision tests
- Similar-input seperation
- Avalanche effect check

## ⚠ SECURITY WARNING
MathHash is not cryptographically audited.
Do not use it in production or to secure real user passwords.

This is for:
- Learning
- Research
- Portfolio projects
- Hackathons
- Understanding hashing internals


## CONTIBUTING
PRs and issues are welcome!
Open an issue on GitHub to suggest improvements


## LICENSE
This project is licensed under the MIT License.
See the LICENSE file for more details.


