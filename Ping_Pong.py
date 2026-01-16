from tkinter import *
from tkinter import messagebox
import random
xgeschw = 5
ygeschw = 6
def move_sl_up(event):
    schläger_links.place(x=schläger_links.winfo_x(),y=schläger_links.winfo_y()-10)
def move_sl_down(event):
    schläger_links.place(x=schläger_links.winfo_x(),y=schläger_links.winfo_y()+10)
def move_sr_up(event):                                                                               #bewegungen der Schläger
    schläger_rechts.place(x=schläger_rechts.winfo_x(),y=schläger_rechts.winfo_y()-10)
def move_sr_down(event):
    schläger_rechts.place(x=schläger_rechts.winfo_x(),y=schläger_rechts.winfo_y()+10)
def kollidiert(ball_coords, paddle): 
    px = paddle.winfo_x()
    py = paddle.winfo_y()
    pw = paddle.winfo_width()
    ph = paddle.winfo_height()

    bx1, by1, bx2, by2 = ball_coords

    return (
        bx2 >= px and
        bx1 <= px + pw and   #es werden rechnungen returnt
        by2 >= py and
        by1 <= py + ph
    )
def move_ball():
    global xgeschw , ygeschw #muss global angegeben werden,weil es auserhaulb deffiniert wird
    coords = canvas.coords(ball)
    print(coords)
    if coords[1] <= 0 or coords[3] >= 750:
        ygeschw *= -1
    if kollidiert(coords,schläger_links) or kollidiert(coords,schläger_rechts):  #es wird eine deffinition aufgerufen
        xgeschw += random.randint(1,15)
        xgeschw -= random.randint(1,10)
        xgeschw *= -1
    if coords[0]<-20:
        messagebox.showwarning(title="Loser",message="Rot hat verloren")
    if coords[0]>1600:
        messagebox.showwarning(title="Loser",message="Blau hat verloren")
    canvas.move(ball, xgeschw, ygeschw)
    window.after(20, move_ball)  # ruft sich selbst alle 20 ms auf
window = Tk()
window.title("Ping_Pong")
canvas = Canvas(window,height=750,width=1500,bg="#D3D991")
canvas.pack()
schläger_links = Label(canvas,height=20,width=10,bg="red")
schläger_links.place(x=15,y=((750/2)-50))                           #optisches Zeug
schläger_rechts = Label(canvas,height=20,width=10,bg="blue")
schläger_rechts.place(x=1500-80,y=((750/2)-50))
canvas.create_line(1500/2,751,1500/2,-1,width=7)
window.bind("<w>",move_sl_up)
window.bind("<s>",move_sl_down)
window.bind("<Up>",move_sr_up)        #Steuerung
window.bind("<Down>",move_sr_down)
ball = canvas.create_rectangle(200,200,240,240,fill="black")
move_ball()
window.mainloop()