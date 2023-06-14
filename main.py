import os
import numpy as np
import pandas as pd
# import cv as cv2
#from skimage import io
import matplotlib.pylab as plt
from tkinter import *
import tkinter as Tk
import time
import tkinter.messagebox
import system as sys
from passenger_distribute import passenger_distribute
from bus_stop import get_bus_stop
from bus import get_bus
from detect import detect
from PIL import Image, ImageTk
bus_stops = get_bus_stop()
bus = get_bus()
stop_btn = []

def search(stop_id):
    if stop_id.isdigit() == False:
        tkinter.messagebox.showerror('Error','Please enter the correct bus stop number')
        return
    if int(stop_id) >= len(bus_stops):
        tkinter.messagebox.showerror('Error','Please enter the correct bus stop number')
        return
    print("查詢站牌: " + bus_stops[int(stop_id)].get_stop_name() + "\n")
    # passenger_distribute(stop_id)
    return

def add(stop):
    lb.config(text="H")
    lb.place(x=20,y=l)
    if(os.path.exists('./image/busStop' + str(stop) + '.jpg')):
        image=Image.open('./image/busStop' + str(stop) + '.jpg')
    else:
        image=Image.open('./image/busStop.jpg')
    img=image.resize((350, 200))
    my_img=ImageTk.PhotoImage(img)
    pic.configure(image=my_img)
    pic.image = my_img
    
def show_busstop():
    global l
    l=56
    for i in bus_stops:
        btn = Tk.Button(window,
                text=i.get_stop_name(),
                font=(20),
                relief='flat',
                activeforeground='#0072E3',
                justify='left',
                width=25,
                bg='#E0FFFF',
              )
        stop_btn.append(btn)
              
        btn.place(x=30, y=l)
        l=l+30;
    for i in range(len(bus_stops)):
        stop_btn[i].config(command=lambda b=i: add(b))

class Mainpage(Tk.Frame):
    global window, lb, pic
    window = Tk.Tk()
    window.title('Passenger Distribution System')
    window.geometry('800x600')
    window.resizable(width=False, height=False)
    window.configure(background='#E0FFFF')

    image = Image.open('image/busStop.jpg')
    img=image.resize((350, 200))
    my_img=ImageTk.PhotoImage(img)
    pic = Label(window,image = my_img)
    pic.place(x=400,y = 100)
    Label(window, text='search bus:',bg='#E0FFFF',font=(16)).place(x=30, y=10)
    lb = Label(window, text='',bg='#E0FFFF',font=(16),fg = '#0080FF')
    name = Tk.StringVar()
    enter = Tk.Entry(window, textvariable=name,bd = 2,width=45,relief='sunken')
    enter.place(x=30, y=34)
    show_busstop()

if __name__ == '__main__':
    app = Mainpage()
    #app.pack()
    app.mainloop()






