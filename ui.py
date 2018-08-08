from Tkinter import *
from tkintertable import TableCanvas, TableModel
from PIL import Image, ImageTk
#import MySQLdb
import time
import tkMessageBox
import psycopg2

R = Tk()

def login():
    conn_string = "host='localhost' dbname='LogIn' user='postgres' password='JonasRobert29'"
    conn = psycopg2.connect(conn_string)
    print "Connected! CHAMMMMMMMMMMMP!"
    gg = "white"


    R.geometry('720x673')
    R.title('Login')
    R.resizable(width=FALSE, height=FALSE)
    Image_open = Image.open("Login.png")
    R.winfo_x()
    R.winfo_y()
    image = ImageTk.PhotoImage(Image_open)
    logo = Label(R, image=image, bg=gg)
    logo.place(x=0, y=0, bordermode="outside")
    e1 = Entry(R, width=20, font=("bold", 15), highlightthickness=1, bg=gg, relief=SUNKEN)
    e1.place(x=280, y=400)
    e2 = Entry(R, width=20, show="*", font=("bold", 15), highlightthickness=1, bg=gg, relief=SUNKEN)
    e2.place(x=280, y=512)
    R.mainloop()
