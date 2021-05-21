from tkinter import *
from random import randrange
 
def move():
    global x
    global y,pX,pY
    global Serpent
    can.delete('all')
    i=len(Serpent)-1
    j=0
    while i > 0:
        Serpent[i][0]=Serpent[i-1][0]
        Serpent[i][1]=Serpent[i-1][1]
        can.create_oval(Serpent[i][0], Serpent[i][1], Serpent[i][0]+10, Serpent[i][1]+10,outline='purple', fill='black')
        i=i-1


    can.create_rectangle(pX, pY, pX+5, pY+5, outline='green', fill='black')
   
    if direction  == 'gauche':
        Serpent[0][0]  = Serpent[0][0] - dx
        if Serpent[0][0] < 0:
            Serpent[0][0] = 493
    elif direction  == 'droite':
        Serpent[0][0]  = Serpent[0][0] + dx
        if Serpent[0][0] > 493:
            Serpent[0][0] = 0
    elif direction  == 'haut':
        Serpent[0][1]  = Serpent[0][1] - dy
        if Serpent[0][1] < 0:
            Serpent[0][1] = 493
    elif direction  == 'bas':
        Serpent[0][1]  = Serpent[0][1] + dy
        if Serpent[0][1] > 493:
            Serpent[0][1] = 0
    can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10,outline='black', fill='purple')
    
   
    if flag != 0:
        fen.after(60, move)

    collision()
    eat()
 
def newGame():
    global pX,pY
    global flag
    if flag == 0:
        flag = 1
    move()
 
def left(event):
    global direction
    direction = 'gauche'
 
def right(event):
    global direction
    direction = 'droite'
 
def up(event):
    global direction
    direction = 'haut'
 
def down(event):
    global direction
    direction = 'bas'

def collision():
    if Serpent[0][0] + 10 == 500:
        can.delete("all")
    if Serpent[0][0] <= 0 : 
        can.delete("all")
    if Serpent[0][0] <= 0 :
        can.delete("all")
    if Serpent[0][0] == 500 :
        can.delete("all")
   
def eat():
    global pomme
    global x,y,pX,pY
    global Serpent
    if Serpent[1][0]>pX-7 and  Serpent[1][0]<pX+7:        
        if Serpent[1][1]>pY-7 and Serpent[1][1]<pY+7:
            pX = randrange(5, 495)
            pY = randrange(5, 495)
            can.coords('pomme',pX, pY, pX+5, pY+5)
            Serpent.append([0,0])
       
x = 245
y = 24        
dx, dy = 10, 10
flag = 0
direction = 'droite'
Serpent=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]

pX = randrange(5, 495)
pY = randrange(5, 495)

fen = Tk()
can = Canvas(fen, width=500, height=500, bg='white')
can.pack(side=TOP, padx=5, pady=5)


b1 = Button(fen, text='Lancer', command=newGame, bg='black' , fg='green')
b1.pack(side=LEFT, padx=5, pady=5)

b2 = Button(fen, text='Quitter', command=fen.destroy, bg='black' , fg='green')
b2.pack(side=RIGHT, padx=5, pady =5)

fen.bind('<d>', right)
fen.bind('<q>', left)
fen.bind('<z>' , up)
fen.bind('<s>', down)

fen.mainloop()