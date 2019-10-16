import socket
import threading
import socketserver
 


def tratarCliente(clientsocket):

        print("Servidor recebeu concexao de {}".format(adress))

        msg_cliente = clientsocket.recv(1024).decode("utf-8")  # para transformar em string -> usar o decode

        for i in range(0,len(lista_sockets)):
            lista_sockets[i].send(bytes(msg_cliente,"utf-8"))        

        print(msg_cliente)

        #clientsocket.sendall(bytes(msg_cliente,"utf-8"))

        clientsocket.close()  
        lista_sockets.remove(clientsocket)






s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("localhost",5556))
print("Escutando...")
s.listen(2)

lista_sockets = []



while True:
    clientsocket, adress = s.accept()
    lista_sockets.append(clientsocket)
    t = threading.Thread(target=tratarCliente,args=(clientsocket,)).start()
    




    
    
