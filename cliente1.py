import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("localhost",5555))



msg = s.recv(1024) # acho que esta determinando o tamanho do buffer para 1 mg

s.sendall(bytes("IAi boe drx"))

print(msg.decode("utf-8"))