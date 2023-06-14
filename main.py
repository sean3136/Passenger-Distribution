import os
import numpy as np
import pandas as pd
# import cv as cv2
# from skimage import io
import matplotlib.pylab as plt
from tkinter import *
import tkinter as Tk
import tkinter.font as font
import time
import tkinter.messagebox
import system as sys
from bus_stop import get_bus_stop
from bus import get_bus
from detect import detect
from PIL import Image, ImageTk
from system import algorithm
bus_stops = get_bus_stop()
bus = get_bus()
sum_num = detect()
stop_btn = []
busstop_info_label = None  # New label to display bus stop information


def search(stop_id):
    if stop_id.isdigit() == False:
        tkinter.messagebox.showerror(
            'Error', 'Please enter the correct bus stop number')
        return
    if int(stop_id) >= len(bus_stops):
        tkinter.messagebox.showerror(
            'Error', 'Please enter the correct bus stop number')
        return
    print("查詢站牌: " + bus_stops[int(stop_id)].get_stop_name() + "\n")
    return


def add(stop):
    if (os.path.exists('./image/busStop' + str(stop) + '.jpg')):
        image = Image.open('./image/busStop' + str(stop) + '.jpg')
    else:
        image = Image.open('./image/busStop.jpg')
    img = image.resize((500, 300))
    my_img = ImageTk.PhotoImage(img)
    pic.configure(image=my_img)
    pic.image = my_img
    show_busstop_info(stop)  # Show bus stop info


def show_busstop_info(stop):
    global busstop_info_label

    if busstop_info_label is not None:
        busstop_info_label.destroy()  # Clear previous bus stop info label

    bus_stop = bus_stops[stop]
    info = f"  \t本站排隊人數: {bus_stop.waiting_people}\n  \t本站可上車人數: {bus_stop.stop_available}"
    busstop_info_label = Label(
        window, text=info, bg='#E0FFFF', font=(80), fg='#000000')
    busstop_info_label.place(x=530, y=420)


def show_busstop():
    global l
    l = 76
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
        btn.place(x=40, y=l)
        l = l+30
    print(stop_btn[17].place_info())
    for i in range(len(bus_stops)):
        stop_btn[i].config(command=lambda b=i: add(b))

def bus_move():
    lb.place(x=20, y=76)
    for i in range(1, 512):
        lb.place(x=20, y=76+i)
        window.update()
        time.sleep(0.03)

class Mainpage(Tk.Frame):
    global window, lb, pic
    window = Tk.Tk()
    window.title('Passenger Distribution System')
    window.geometry('1000x700')
    window.resizable(width=False, height=False)
    window.configure(background='#E0FFFF')

    image = Image.open('image/busStop.jpg')
    img = image.resize((500, 300))
    my_img = ImageTk.PhotoImage(img)
    pic = Label(window, image=my_img)
    pic.place(x=420, y=100)

    lb = Label(window, text='-->', bg='#E0FFFF', font=(16), fg='red')
    lb.place(x=20, y=76)

    border_color = Frame(window, background="navy")
    bus_1579 = Label(border_color, text='1579 Bus', bd=0,  font=font.Font(size=25),
          relief='solid')
    bus_1579.pack(padx=1, pady=1)
    border_color.pack(padx=40, pady=40)

    bus_btn = Tk.Button(window, text='Bus Start', font=font.Font(size=15),
                        relief='sunken',
                        activeforeground='#0072E3',
                        justify='left',
                        # width=25,
                        bg='#E0FFFF',
                        command=bus_move)
    bus_btn.place(x=620, y=500)
    show_busstop()


if __name__ == '__main__':
    app = Mainpage()
    algorithm()
    app.mainloop()
