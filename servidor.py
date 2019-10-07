import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",5555))
s.listen()



while True:
    clientsocket, adress = s.accept()
    print("Servidor recebeu concexao de {}".format(adress))
    clientsocket.send(bytes("Servidor está respondendo","utf-8"))


