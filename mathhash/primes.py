
PRIME_CONSTS = [
    65537,       
    6700417,    
    2147483647,  
    32416190071, 
]



def is_prime(n: int) -> bool:
    if  n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



#GENERATING A PRIME NUMBER
def gen_prime(limit: int) -> list[int]:
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)

    return primes