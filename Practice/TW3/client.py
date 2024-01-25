import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('localhost', 12345)
client.connect(address)
while True :
    message = input("Enter message ")
    if message == 'q' :
        break
    client.send(message.encode())