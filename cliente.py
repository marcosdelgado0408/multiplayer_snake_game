import socket
import threading

def enviarMsg(s): # Thread separada para podermos enviar as mensagens e recebermos mensagens ao mesmo tempo
    while True:
        send_message = str(input())
        s.sendall(bytes(send_message, "utf-8"))



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5555))

t = threading.Thread(target=enviarMsg, args=(s,))
t.daemon = True  # vai acabar a thread quando fecharmos o programa
t.start()

while True:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    if not msg:
        break;



