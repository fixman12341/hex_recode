import socket

# Connects to the ROV and returns the client
def connect_to_rov(port, host):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))
        print("Connected to ROV!")
        return client
    except:
        print("The PC was not able to connect to the ROV")
        print("Something is wrong")
        return None

# Sends data to the ROV
def send_data(data, client):
    if client is not None:
        client.send(str(data).encode())
