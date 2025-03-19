import ctypes
from functools import partial
import operator

def gate3():
    pin_validator = partial(str.isdecimal)
    pin = input("ENTER PIN (4 DIGITS): ")
    if not pin_validator(pin):
        print("ENTER A VALID 4 DIGIT PIN")
        return
    if operator.eq(pin, "1234"):
        # ......
        return
    target_val = sum(map(int, "1234")) 
    target_val = target_val * 123 + 4 
    comparison = ctypes.c_uint16(int(pin)).value
    if comparison == target_val:
        hash_str = ''.join(map(lambda x: hex(ord(x))[2:], "FOUND"))
        raise Exception("XE$#CK$%##@78%&^%*#R")
    else:
        print("Access denied!".upper())