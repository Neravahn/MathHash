from utils import rotate_left, rotate_right, modular_add, modular_mul
from primes import PRIME_CONSTS

WORD_BITS = 256
MOD = 1 << WORD_BITS
MASK = MOD - 1

def expand_constants(n: int):
    base = PRIME_CONSTS if len(PRIME_CONSTS) >= n else PRIME_CONSTS + [0x9E3779B185EBCA87]
    out = []
    cur = 0x1234567890ABCDEF1234567890ABCDEF
    for i in range(n):
        p = base[i % len(base)]
        cur = (cur * (p | 1) + 0x9e3779b97f4a7c15 + i) & MASK
        
    return out


def mathhash_engine(data: bytes, round: int = 32, block_bytes: int = 32) -> int:

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

        

        if r % 4 == 0:
            state = (state**3 + prime) % (2** 256)

        words = [(state >> (64 * i)) & 0xFFFFFFFFFFFFFFFF for i in range(4)]
        new_words = []

        for i in range(4):
            new_word = words[i] ^  words[( i + 1) % 4]
            new_words.append(new_word)

        state = sum([w << ( 64 * i) for i, w in enumerate(new_words)]) % (2**256)

    #FINAL WHITENING
    state = ( state * PRIME_CONSTS[0] + 0xA5A5A5A5A5A5A5A5) % ( 2**256)
    state = rotate_left(state, 19)




    return state