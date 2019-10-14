import socket
import threading
import socketserver


global c1_msg, c2_msg

c1_msg = ""
c2_msg = ""

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",5555))
s.listen()


'''
def tratarCliente(clientsocket):
       
    msg = "Mensagem recebida do servidor: "

    msg_cliente  = clientsocket.recv(1024)

    msg += msg_cliente.decode("utf-8") # para transformar em string -> usar o decode


    clientsocket.sendall(bytes(msg,"utf-8"))

    clientsocket.close();'''
    

    
    

while True:

    clientsocket, adress = s.accept()
    
    print("Servidor recebeu concexao de {}".format(adress))

    msg_cliente = clientsocket.recv(1024)

    # para transformar em string -> usar o decode
    msg = msg_cliente.decode("utf-8")
     

    if(msg.find("c1") != -1): # caso encontre "c1" na mensagem do cliente
        splited_msg = msg.split("-")
        c1_msg = splited_msg[1]

        clientsocket.sendall(bytes(c2_msg, "utf-8"))
        clientsocket.close()


    elif(msg.find("c2") != -1): # caso encontre "c2-" na mensagem do cliente
        splited_msg = msg.split("-")
        c2_msg = splited_msg[1]

        clientsocket.sendall(bytes(c1_msg, "utf-8"))
        clientsocket.close()
    

    else:    
        clientsocket.sendall(bytes(msg, "utf-8"))

        clientsocket.close()

    
'''    t = threading.Thread(target=tratarCliente,args=(clientsocket,))
    t.start()
'''
