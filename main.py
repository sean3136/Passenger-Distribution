import numpy as np
import pandas as pd
import cv as cv2
#from skimage import io
from PIL import Image
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
bus_stops = get_bus_stop()
bus = get_bus()

def add():
    lb.config(text="H")
    lb.place(x=20,y=l)
    
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
                command=add()
              )
              
        btn.place(x=30, y=l)
        l=l+30;
class Mainpage(Tk.Frame):
    global window,lb
    window = Tk.Tk()
    window.title('Passenger Distribution System')
    window.geometry('800x600')
    window.resizable(width=False, height=False)
    window.configure(background='#E0FFFF')
    name = Tk.StringVar("")
    Label(window, text='search bus:',bg='#E0FFFF',font=(16)).place(x=30, y=10)
    lb = Label(window, text='',bg='#E0FFFF',font=(16),fg = '#0080FF')
    enter = Tk.Entry(window, textvariable=name,bd = 2,width=45,relief='sunken',show="bus_stop")
    enter.place(x=30, y=34)
    show_busstop()

if __name__ == '__main__':
    app = Mainpage()
    #app.pack()
    app.mainloop()






