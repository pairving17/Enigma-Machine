# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:55:08 2019

@author: Owner
"""
from tkinter import *
from BackendFunctionsEM import *

master = Tk()

labelStr = StringVar()

def enter():
    global labelStr
    a = EngimaMachine(CodeBar.get())
    print(a)
    labelStr.set(a)
    print(labelStr)
#Lables
Label(master, text="Code").grid(row=0,column=1, sticky = W)
Label(master, text="Keys").grid(row=4,column=0, sticky = W)

# Buttons 
Button(master, text="Enter",command= enter).grid(row=1,column=3)

#Entry Bars
CodeBar = Entry(master)
Key1Bar = Entry(master)
Key2Bar = Entry(master)
Key3Bar = Entry(master)
Key4Bar = Entry(master)

# Geometery
CodeBar.grid(row=0, column=2)

Key1Bar.grid(row=4,column=1)
Key2Bar.grid(row=4,column=2)
Key3Bar.grid(row=4,column=3)
Key4Bar.grid(row=4,column=4)

labelStr = StringVar()
labelBar = Label(master,textvariable= labelStr).grid(row=5,column=0)
master.geometry("500x500")


mainloop( )





