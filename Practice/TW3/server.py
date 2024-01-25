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