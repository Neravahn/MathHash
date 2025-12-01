def simple_math_hash(data: bytes ) -> int:
    #FOR TESTING RN

    result = 0
    prime = 31

    for b in data:
        result = (result * prime + b) % ( 2 ** 256)
        result = (( result << 3) | (result >> ( 256 - 3))) & 0xFFFFFFFF
        
    return result