import socket


'''
def receiveMessage(s):

    fullMsg = ""
    while True:
        msg = s.recv(1024)
        
        if(len(msg) <= 0):
            break
        
        fullMsg += msg.decode("utf-8")


    return fullMsg
'''


WICH_CLIENT = "c2"


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 5555))

    #send_message = WICH_CLIENT + "-"

    send_message = str(input("Digite mensagem para o servidor: "))

    s.sendall(bytes(send_message, "utf-8"))

    msg = s.recv(1024)

    print(msg.decode("utf-8"))
