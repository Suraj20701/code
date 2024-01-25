import random
import math
from math import gcd

def is_prime(num) :
    if num <= 1 :
        False
    for i in range(2, int(math.sqrt(num))) :
        if num % i == 0 :
            return False
        
    return True

def generate_prime(bits) :
    while True :
        num = random.getrandbits(bits)
        if is_prime(num) :
            return num
        
def generate_key_pair(bits) :
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p-1) * (q-1)
    while True : 
        e = random.randint(2, phi)
        if gcd(e, phi) == 1 :
            break
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def encrypt(public_key, msg) :
    e, n = public_key
    cipher = [pow(ord(m), e, n) for m in msg]
    return cipher

def decrypt(private_key, cipher) :
    d,  n = private_key
    msg = "".join([chr(pow(c, d, n)) for c in cipher])
    return msg


if __name__ == "__main__" :
    bits = 8
    public_key, private_key = generate_key_pair(bits)
    msg = input("Enter msg : ")
    cipher = encrypt(public_key, msg)
    print(cipher)
    msg = decrypt(private_key, cipher)
    print(msg)