import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
import socket
import threading
import queue
import struct

# essa strng vai servir para adicionar os caracteres da direção(e, d, c, b)


screen = pygame.display.set_mode((500,500))
screen_rect = screen.get_rect()



def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def recvMsg(socket1):
    global screen, screen_rect

    try:
        while True:

            len_str = socket1.recv(4)
            size = struct.unpack('!i', len_str)[0]

            img_str = bytes()

            while size > 0:
                if size >= 4096:
                    data = socket1.recv(4096)
                else:
                    data = socket1.recv(size)

                if not data:
                    break

                size -= len(data)
                img_str += data


            image = pygame.image.fromstring(img_str, (500, 500), 'RGB')
            image_rect = image.get_rect(center=screen_rect.center)

            screen.blit(image, image_rect) # jogo a nova imagem nesse image_rect

    finally:
        print("Closing socket and exit")
        socket1.close()
        pygame.quit()


        #msg = socket1.recv(10000)
        #msg2 = socket1.recv(10000)

        
        #size = msg.decode("utf-8")

        #receber_direcoes = msg2.decode("utf-8")
        


        #if not msg:
         #   break


def main():
    global width, rows, s, s2, snack
    global tela, size
    global win
    global screen, screen_rect



    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect(("localhost", 5556))
 
    ID = "2"  # id do snake para o outro snake saber e não mostrar os proprios comandos
    width = 500
    rows = 20
    clock = pygame.time.Clock()

    enviar_move = ""
    
    pygame.init()

    T = threading.Thread(target=recvMsg, args=(socket1, )).start()


    while True:
        pygame.time.delay(50)
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    enviar_move = "e"  
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    enviar_move = "e" 

                elif keys[pygame.K_RIGHT]:
                    enviar_move = "d"

                elif keys[pygame.K_UP]:
                    enviar_move = "c"

                elif keys[pygame.K_DOWN]:
                    enviar_move = "b"

                elif keys[pygame.K_RIGHT]:
                    enviar_move = "d"

                elif keys[pygame.K_UP]:
                    enviar_move = "c"

                elif keys[pygame.K_DOWN]:
                    enviar_move = "b"

        enviar = ID + enviar_move
        socket1.sendall(bytes(enviar, "utf-8")) # enviando direção da cobra de saída

        print(enviar)

        pygame.display.update()
    pass


main()
