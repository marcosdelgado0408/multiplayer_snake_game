import socket
import threading
import socketserver

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
import queue

# essa strng vai servir para adicionar os caracteres da direção(e, d, c, b)
receber_direcoes = ""


class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 255, 255)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius, j*dis+8)
            circleMiddle2 = (i*dis + dis - radius*2, j*dis+8)
            pygame.draw.circle(surface, (255, 255, 255), circleMiddle, radius)
            pygame.draw.circle(surface, (255, 255, 255), circleMiddle2, radius)


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos, color=color)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        self.enviar_move = ""

    def move(self):

        # c -> cima 
        # b -> baixo 
        # d -> direita
        # e -> esquerda
        #enviar_move = ""


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.enviar_move = "e" 

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.enviar_move = "d"

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.enviar_move = "c"

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.enviar_move = "b"
    
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                else:
                    c.move(c.dirnx, c.dirny)
        
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):

        cor = self.color

        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1, tail.pos[1]), color=cor))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1, tail.pos[1]), color=cor))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1]-1), color=cor))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1]+1), color=cor))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


class snake2(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos,color=color)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        global receber_direcoes
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        '''

        keys = receber_direcoes

        if keys == "2e":
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif keys == "2d":
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif keys == "2c":
            self.dirnx = 0
            self.dirny = -1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif keys == "2b":
            self.dirnx = 0
            self.dirny = 1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):

        cor = self.color

        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1, tail.pos[1]), color=cor))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1, tail.pos[1]),color=cor))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1]-1),color=cor))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1]+1),color=cor))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


'''
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))
'''

def redrawWindow():
    global rows, width, s , s2, snack, win
    win.fill((0, 0, 0))
    s.draw(win)
    s2.draw(win)
    snack.draw(win)
    #drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, item):

    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


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
    global receber_direcoes
    while True:
        msg = socket1.recv(1024)

        print(msg.decode("utf-8"))

        receber_direcoes = msg.decode("utf-8") # colocando as direções da outra cobra na Fila

        if not msg:
            break












































def tratarCliente(clientsocket, adress):
    global win
    global receber_direcoes
    while True:
        msg_cliente = clientsocket.recv(1024).decode("utf-8")  # para transformar em string -> usar o decode
        receber_direcoes = msg_cliente


        for i in range(0,len(lista_sockets)):
            #if(adress != lista_adresses[i]): # não enviar a mensagem do próprio cliente
            lista_sockets[i].send(win.get_view())        

        if not msg_cliente: # isso vai servir para não dar erro de ficar tentando receber recv caso matarmos o cliente no terminal
            clientsocket.close()  
            lista_sockets.remove(clientsocket)
            break





def main():
    global width, rows, s, s2, snack
    global receber_direcoes
    global win

    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 250), (10, 10))
    s2 = snake2((0, 255, 0), (10, 5))
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.bind(("localhost",5557))
    print("Escutando...")
    sock.listen(2)

    clientsocket, adress = sock.accept()
    print("Servidor recebeu concexao de {}".format(adress))
    lista_sockets.append(clientsocket)
    lista_adresses.append(adress) 
   
    while flag:
        pygame.time.delay(50)
        clock.tick(10)   

        t = threading.Thread(target=tratarCliente,args=(clientsocket, adress))
        t.start()

        s.move()
        s2.move()
        
        if s.body[0].pos == snack.pos: # cobra 1 comer snack
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))

        if s2.body[0].pos == snack.pos: # cobra 3 comer snack
            s2.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))

        
        for x in range(len(s.body)): # cobra 1 morrer 
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                print('Score: ', len(s.body))
                message_box('You Lost!', 'Play again...')
                s.reset((10, 10))
                break

        for x in range(len(s2.body)): # cobra 2 morrer
            if s2.body[x].pos in list(map(lambda z: z.pos, s2.body[x+1:])):
                print('Score: ', len(s.body))
                message_box('You Lost!', 'Play again...')
                s2.reset((10, 5))
                break
            

        redrawWindow()
    pass


lista_sockets = []
lista_adresses = []
main()