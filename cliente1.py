import socket


while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 5556))
    
    msg = s.recv(1024)
    if not msg:
        continue
    
    send_message = str(input("Digite mensagem para o servidor: "))
    
    s.sendall(bytes(send_message, "utf-8"))

    print(msg.decode("utf-8"))

