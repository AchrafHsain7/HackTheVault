import numpy as np
from functools import reduce

def gate2():
    pin = input("ENTER PIN (4 DIGITS): ")
    while not pin.isdecimal():
        print("ENTER A VALID DECIMAL PIN")
        pin = input("Enter PIN (4 digits): ")
    magicKey = input("ENTER THE QUANTUM KEY: ")
    magicNumber = reduce(lambda x, y: x + y, [ord(c) - ord('0') for c in magicKey])
    if np.int32(int(pin)) == magicNumber:
        #........
        print("Access granted!".upper())
    else:
        print("Access denied!".upper())