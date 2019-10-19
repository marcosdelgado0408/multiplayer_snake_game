import socket
import threading
import socketserver




def tratarCliente(clientsocket):
   
    while True:
       
        msg_cliente = clientsocket.recv(1024).decode("utf-8")  # para transformar em string -> usar o decode

        for i in range(0,len(lista_sockets)):
            lista_sockets[i].send(bytes(msg_cliente,"utf-8"))        

        print(msg_cliente)

        if not msg_cliente: # isso vai servir para não dar erro de ficar tentando receber recv caso matarmos o cliente
            clientsocket.close()  
            lista_sockets.remove(clientsocket)
            break




lista_sockets = []

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("localhost",5556))
print("Escutando...")
s.listen(2)


while True:
    clientsocket, adress = s.accept()
    print("Servidor recebeu concexao de {}".format(adress))
    lista_sockets.append(clientsocket)
    
    t = threading.Thread(target=tratarCliente,args=(clientsocket,))
    t.daemon = True # vai acabar a thread quando fecharmos o programa
    t.start()
    




    
    
