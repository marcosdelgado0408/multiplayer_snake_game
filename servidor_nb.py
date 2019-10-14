import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5555 if len(sys.argv) == 1 else int(sys.argv[1])
sock.bind(('localhost', port))
sock.listen(5)

try:
    while True:
        conn, info = sock.accept()

        data = conn.recv(1024)
        while data:
            print(data.decode("utf-8"))
            data = conn.recv(1024)
            conn.send(bytes(data))
except KeyboardInterrupt:
    sock.close
