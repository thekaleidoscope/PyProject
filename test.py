# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 12:20:07 2018

@author: Parv
"""

def printtext():
    
    s = ie.get() 
    print(s)   

from tkinter import *
root = Tk()

root.title('Name')
global ie
ie = Entry(root)
ie.pack()
we = Entry(root)
we.pack()
#e.focus_set()


b = Button(root,text='okay',command=printtext)
b.pack(side='bottom')
root.mainloop()