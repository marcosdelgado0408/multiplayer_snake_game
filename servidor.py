import socket
import threading
import socketserver


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",5555))
s.listen()



def tratarCliente(clientsocket):
       
    msg = "Mensagem recebida do servidor: "

    msg_cliente  = clientsocket.recv(1024)

    msg += msg_cliente.decode("utf-8") # para transformar em string -> usar o decode


    clientsocket.sendall(bytes(msg,"utf-8"))

    clientsocket.close();
    

    
    

while True:

    clientsocket, adress = s.accept()
    
    print("Servidor recebeu concexao de {}".format(adress))

    msg = "Mensagem recebida do servidor: "

    msg_cliente = clientsocket.recv(1024)

    # para transformar em string -> usar o decode
    msg += msg_cliente.decode("utf-8")

    clientsocket.sendall(bytes(msg, "utf-8"))

    clientsocket.detach()

    
'''    t = threading.Thread(target=tratarCliente,args=(clientsocket,))
    t.start()
'''