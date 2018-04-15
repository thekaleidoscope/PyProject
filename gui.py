# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 01:26:40 2018

@author: Parv
"""
from tkinter import *
#import tkinter as Tk 


def admin_window():
    window = Toplevel(root)
    #l=Label(window,text="test")
    #l.pack()
    global id_entry,name_entry,tseats_entry,price_entry,id_rem
    def addinput():
        mid = id_entry.get() 
        mname = name_entry.get()
        mseats=tseats_entry.get()
        mprice=price_entry.get()
        print(mid,mname,mseats,mprice)
        
    def remmovie():
        rem_id=id_rem.get()
        print(rem_id)
    
    label1=Label(window,text="New Movie")
    label2=Label(window,text="ID")
    label3=Label(window,text="Name")
    label4=Label(window,text="Total Seats")
    label5=Label(window,text="Price")
    
    id_entry=Entry(window)
    name_entry=Entry(window)
    tseats_entry=Entry(window)
    price_entry=Entry(window)
    
    label1.grid(row=0)
    label2.grid(row=1)
    label3.grid(row=2)
    label4.grid(row=3)
    label5.grid(row=4)
    
    id_entry.grid(row=1,column=1)
    name_entry.grid(row=2,column=1)
    tseats_entry.grid(row=3,column=1)
    price_entry.grid(row=4,column=1)

    
    b1=Button(window, text="submit", fg="red",command=addinput)
    b1.grid(row=5, column=1)
    
    label5=Label(window,text="Remove Movie")
    id_rem=Entry(window)
    b2=Button(window, text="submit", fg="blue",command=remmovie)
    label5.grid(row=0,column=3)
    id_rem.grid(row=1,column=3)
    b2.grid(row=2, column=3)
    

def user_window():
    window = Toplevel(root)
    
    
    
    def showall():
        print("working")
    
    def showmovie():
        sid = id_show.get()
        print(sid)
        
    def bookmovie():
        mid=book_mov_id.get()
        seat=book_mov_seat.get()
        print(mid,seat)
        
    def refundmovie():
        mid=ref_mov_id.get()
        seat=ref_mov_seat.get()
        print(mid,seat)
        
    global id_show,book_mov_id,book_mov_seat,ref_mov_id,ref_mov_seat 
    b1=Button(window, text="Show All Movies", fg="red",command=showall)
    b1.grid(row=0, column=0)
    showmov=Label(window,text="Show Movie")
    showmov.grid(row=1)
    id_show=Entry(window)
    id_show.grid(row=1,column=1)
    showbutton=Button(window,text="submit",command=showmovie).grid(row=1,column=2)
    
    bookl=Label(window,text="Book Movie").grid(row=2)
    book_mov_id=Entry(window)
    book_mov_id.grid(row=2,column=1)
    book_mov_seat=Entry(window)
    book_mov_seat.grid(row=2,column=2)
    bookbutton=Button(window,text="book",command=bookmovie).grid(row=2,column=3)
    
    refl=Label(window,text="Refund Movie").grid(row=3)
    ref_mov_id=Entry(window)
    ref_mov_id.grid(row=3,column=1)
    ref_mov_seat=Entry(window)
    ref_mov_seat.grid(row=3,column=2)
    refbutton=Button(window,text="refund",command=refundmovie).grid(row=3,column=3)
    
    
root=Tk() 
topFrame = Frame(root)
topFrame.pack()

bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=Button(topFrame, text="ADMIN", fg="red",command=admin_window)
button2=Button(topFrame, text="USER", fg="blue",command=user_window)
button1.pack(side=LEFT)
button2.pack()


root.mainloop()