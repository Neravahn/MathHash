def hash_password ( password: str) -> str:
    

    #CONVERT PASSWORD INTO BYTES
    password_bytes = password.encode('utf-8')

    import os
    salt = os.urandom(16)   #RANDOM SALT OF 16 BYTES

    combined = password_bytes + salt


    hashed_value = sum(combined) #TEMPORARY PLACE HOLDER

    return hex(hashed_value)



my_hash = hash_password("mypassword1234")
print(my_hash)