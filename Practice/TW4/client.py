import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 12345)
client_socket.connect(address)
msg = input("Enter message to send : ")
client_socket.send(msg.encode())
data = client_socket.recv(1024)
print(f"Data received from server {data.decode()}")