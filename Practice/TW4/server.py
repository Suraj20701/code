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