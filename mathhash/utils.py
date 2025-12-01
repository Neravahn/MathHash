def rotate_left(x: int, bits: int, width: int = 256):
    return((x << bits) | (x >> (width - bits))) & (( 1 << width) - 1)

def rotate_right(x: int, bits: int, width: int = 256):
    return (( x >> bits) | (x << (width - bits))) & (( 1 << width) - 1)


def modular_add(a: int, b: int, mod: int) -> int:
    return (a + b) % mod


def modular_mul(a: int, b: int, mod: int) -> int:
    return(a * b ) % mod