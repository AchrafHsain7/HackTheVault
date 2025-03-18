import string
from sympy import prime

def gate5(KEY):
    chars = string.ascii_letters + "0123456789"
    primes = [prime(i) for i in range(1, len(chars)+1)]
    s = list(KEY)
    encrypted = ""
    for c in s:
        encrypted += hex(primes[chars.index(c)])
    return encrypted

