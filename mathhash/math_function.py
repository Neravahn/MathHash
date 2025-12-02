from utils import rotate_left, rotate_right, modular_add, modular_mul
from primes import PRIME_CONSTS

WORD_BITS = 256
MOD = 1 << WORD_BITS
MASK = MOD - 1

# def expand_constants(n: int = 32):
#     base = PRIME_CONSTS if len(PRIME_CONSTS) >= n else PRIME_CONSTS + [0x9E3779B185EBCA87]
#     out = []
#     cur = 0x1234567890ABCDEF1234567890ABCDEF
#     for i in range(n):
#         p = base[i % len(base)]
#         cur = (cur * (p | 1) + 0x9e3779b97f4a7c15 + i) & MASK
        
#     return out



#MAIN MATH HASHING ENGINE
def mathhash_engine(data: bytes, rounds: int = 32, block_bytes: int = 32) -> int:

    """
    MATH ONLY 256 BITS HASHING ENGINE"""

    # RC = expand_constants(max(rounds, 16))
    RC = [
    0x243F6A8885A308D3,
    0x13198A2E03707344,
    0xA4093822299F31D0,
    0x082EFA98EC4E6C89,
    0x452821E638D01377,
    0xBE5466CF34E90C6C,
    0xC0AC29B7C97C50DD,
    0x3F84D5B5B5470917,
    0x9216D5D98979FB1B,
    0xD1310BA698DFB5AC,
]


    #256 BITS SEED
    iv = int.from_bytes(b"aehryq98w495qwu490".ljust(32, b'\xAA'), "big" )& MASK
    state = iv

#++++++++++++++++++++++++++
    #ABSORBINGS
#++++++++++++++++++++++++++
    #PADDING DATA TO BLOCKS(uses simply 00 to pad)
    if len(data) % block_bytes != 0:
        pad_len = block_bytes - (len(data) % block_bytes)
        data = data + b'\x00' * pad_len
    

    #PROCESSING EACH BLOCK
    for bi in range(0, len(data), block_bytes):
        blk = data[bi:bi + block_bytes]
        for i in range(0, block_bytes, 8): #USING 8 BYTE INTS
            chunk = int.from_bytes(blk[i: i + 8], 'big')
            state ^= chunk & MASK
            state = modular_mul(state, (RC[(bi + i) // 8] | 1), MOD)
            state = rotate_left(state, (( i // 8) * 11 + bi) % WORD_BITS)
            state &= MASK

        #SMALL BLOCK FINALIZER
        state = (state + RC[(bi // block_bytes) % len(RC)]) & MASK
        state = rotate_left(state, (state + (bi // block_bytes)) % WORD_BITS)

    #MIXING ROUNDS
    for r in range(rounds):
        p = RC[r % len(RC)]

        #ARITHEMATIC LAYER
        state = modular_add(state, p^ ( r * 0x0101010101010101), MOD)
        state = modular_mul(state, ((p << 1) | 3), MOD)

        #ROTATE/XOR LAYER
        state = rotate_left(state, (13 + r * 7) % WORD_BITS)
        state^= (state >> ((r * 5 + 11) % WORD_BITS))

        #NON LINEARE STEP
        if ( r & 3) == 0:
            base = state | 1
            state = pow(base, 3, MOD)


        #PERMETUATION
        words = [(state >> (64 * i)) & 0xFFFFFFFFFFFFFFFF for i in range(4)]
        new_words = []
        for i in range(4):
            a = words[i]
            b = rotate_left(words[(i + 1) % 4], (r + i) % 64)
            mix = ((a ^ b) + ( p >> ( i * 8 ) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF

            #64 BIT MUL AND ROTATE
            mix = (( mix * (( p >> ( i * 7)) | 1)) & 0xFFFFFFFFFFFFFFFF)
            mix = ((mix << (( i*3 + r) % 64)) | (mix >> ( 64 - (( i *3 + 5 ) % 64)))) & 0xFFFFFFFFFFFFFFFF
            new_words.append(mix)


        new_state = 0
        for i, w in enumerate(new_words):
            new_state |= ( w & 0xFFFFFFFFFFFFFFFF) << ( 64 * i)
        state = ( state ^ new_state) & MASK

        #FINAL FOLD PER ROUD
        state = (state + (0xA5A5A5A5A5A5A5A5 ^ p)) & MASK
        state = rotate_left(state, (r * 3 + 17) % WORD_BITS)

    #FINAL WHITENING
    state = (state ^ iv) & MASK
    state = modular_mul(state, RC[0] | 1, MOD)
    state = rotate_left(state, 19)
    state = ( state + 0xDEADBEEFDEADBEEFDEADBEEFDEADBEEF) & MASK

    return state