import os
import base64
from math_function import simple_math_hash
from utils import rotate_left, rotate_right, modular_add, modular_mul
from primes import PRIME_CONSTS

def hash_password ( password: str) -> str:
    

    #CONVERT PASSWORD INTO BYTES
    password_bytes = password.encode('utf-8')

    salt = os.urandom(16)   #RANDOM SALT OF 16 BYTES

    combined = password_bytes + salt


    hashed_value = simple_math_hash(combined) #TEMPORARY PLACE HOLDER

    hash_bytes = salt + hashed_value.to_bytes(4, 'big')
    return base64.b64encode(hash_bytes).decode('utf-8')

def verify_password ( password: str, stored: str) -> bool:
    data = base64.b64decode(stored)
    salt = data[:16]
    stored_hash = int.from_bytes(data[16:], 'big')
    combined = password.encode('utf-8') + salt


    hashed_value = simple_math_hash(combined)#PLACEHOLDER 
    return hashed_value == stored_hash


my_hash = hash_password("mypassword1234")
print(my_hash)
verify = verify_password("mypassword1234", my_hash)
print("successfull" if verify else "unsuccessfull")