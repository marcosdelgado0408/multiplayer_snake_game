import socket

while True:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 5555))

    data = str(input("Digite oq quer pro servidor: "))  # 70 MB of data
    sock.send(bytes(data,"utf-8"))  # True

    print(sock.recv(1024).decode("utf-8"))
