from utils import rotate_left, rotate_right, modular_add, modular_mul
from primes import PRIME_CONSTS


def mathhash_engine(data: bytes, round: int = 4) -> int:

    """
    MATH ONLY 256 BITS HASHING ENGINE"""

    state = 0

    #CONVERTING BYTE INTO A 256 BIT INTEGET STATE
    for b in data:
        state = (state * 131524535 + b) % (2 ** 256)


    #MIXING ROUND
    for r in range(round):
        prime = PRIME_CONSTS[r % len(PRIME_CONSTS)]

        #ADDING ORIME
        state = modular_add(state, prime, 2**256)

        #MULTIPLYING PRIME
        state = modular_mul(state, prime, 2**256)

        #ROTATIONS BITS
        state = rotate_left(state, (r + 1)* 5 % 64)
        state = rotate_right(state, (r + 1) * 3 % 64)



        #XOR
        state ^= (state >> (( r + 1) * 7))

        state &= (2 ** 256 -1)

    return state