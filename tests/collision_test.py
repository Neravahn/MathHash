import random
import string 
from mathhash.core import hash_password


def random_string(length = 16):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def test_no_collision_in_random_inputs():
    hashes = set()
    n = 5000

    for _ in range(n):
        data = random_string(20)
        h = hash_password(data)

        #COLLISION DETECTION
        assert h not in hashes, f"collision found for input: { data }"

        hashes.add(h)


def similar_inputs_do_not_collide():
    base = 'mypassword1234'
    h1 = hash_password(base)
    h2 = hash_password(base + "a")
    h3 = hash_password(base + "b")

    assert h1 != h2
    assert h1 != h3
    assert h2 != h3

