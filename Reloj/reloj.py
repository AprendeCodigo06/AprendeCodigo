from tkinter import *
import time

def tiempo():
    tiempo_actual = time.strftime("%H:%M:%S")
    relog.config(text=tiempo_actual, foreground="white", bg="red")
    relog.after(200, tiempo)

raiz = Tk()
raiz.geometry("350x70")
raiz.title("Reloj")
raiz.wm_attributes("-transparentcolor","red")

relog = Label(raiz, font=("times",70))
relog.place(x=0,y=0,width=350,height=70)
tiempo()

raiz.mainloop()