import serial

port = "/dev/ttyUSB0"
baudrate = 115200

rov = serial.Serial(port, baudrate, timeout=1)

print("Waiting for data...")

while True:
    data = rov.readline().decode().strip()

    if data:
        print("Received:", data)