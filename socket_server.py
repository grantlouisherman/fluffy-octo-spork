import socket, os

print(f"Process Id: {os.getpid()}")

s = socket.socket()
print("Socket Started")
port = 1234

s.bind(('', port))
print("Socket is binded")

s.listen(5)
print("Socker is listening")

while True:
    connection, addr = s.accept()
    print(f"Got connection from: {addr}")
    connection.send("You are connected".encode())
    connection.close()
    break
