import socket

HOST = "127.0.0.1"
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for connection...")

connection, address = server.accept()
print("Connected!")

while True:
    data = connection.recv(1024).decode()

    if not data:
        break

    print("Received:", data)
connection.close()
server.close()