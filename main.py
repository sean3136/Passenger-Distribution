import numpy as np
import pandas as pd
import cv as cv2
from skimage import io
from PIL import Image
import matplotlib.pylab as plt
import tkinter as Tk
import time
import tkinter.messagebox
import system as sys


class Mainpage(Tk.Frame):
    window = Tk.Tk()
    window.title('Passenger Distribution System')
    window.geometry('800x600')
    window.resizable(width=False, height=False)
    window.configure(background='white')


if __name__ == '__main__':
    app = Mainpage()
    app.pack()
    app.mainloop()






