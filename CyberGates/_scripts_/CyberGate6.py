import string

KEY = 789
ASCII = string.ascii_letters + string.digits
def gate6(SECRET):
    encrypted = ""
    for c in SECRET:
        tmp = ord(c) ^ KEY
        tmp = tmp << 2
        encrypted +=  chr(tmp)
    return encrypted