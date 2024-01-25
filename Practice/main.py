"""
#TW7 : CRC
for i in range(len(data) - len(divisor) + 1) :
    if data_list[i] == '1' :
        for j in range(len(divisor)) :
            data_list[i+j] = str((int(data_list[i + j]) + int(divisor[j]))%2)

return ''.join(data_list[-len(divisor) + 1 :])           

if all(bit == '0' for bit in data_list[-len(divisor) + 1 :]) :
    print("No error")
else :
    print("Error")

"""


"""
#TW6 : Licky Bucket
tokens = 1000
packets = [400, 300, 500, 300, 700, 200, 100]
index = 0
while index < len(packets) :
    
    if tokens >= packets[index] :
        print(f"Packet sent sucessfully : {packets[index]}")
        tokens -= packets[index]
        index += 1
    else :
        print(f"Tokens are less({tokens}<{packets[index]} updating tokens)")
        tokens = 1000
        

print("All packets sent sucessfully ")

"""

"""
#TW4 : TCP

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 12345)
server.bind(address)
server.listen(4)
print("TCP ready to receive message : ")
client_socket, client_address = server.accept()
data = client_socket.recv(1024)
print(f"Data received from {client_address} {data.decode()}")
msg = "Hello Client !"
client_socket.send(msg.encode())
server.close()
client_socket.close()


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 12345)
client_socket.connect(address)
msg = input("Enter message to send : ")
client_socket.send(msg.encode())
data = client_socket.recv(1024)
print(f"Data received from server {data.decode()}")

"""


"""
TW3 : UDP

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('localhost', 12345)
server.bind(address)
print("UDP ready to receive message...")
while True :
    data, client = server.recvfrom(1024)
    if data.decode() == 'q' :
        break
    print(f"Data received from {client} {data.decode()}")

server.close()

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('localhost', 12345)
client.connect(address)
while True :
    message = input("Enter message ")
    if message == 'q' :
        break
    client.send(message.encode())
"""


"""
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

"""
