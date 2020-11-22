from tkinter import *

def ical(source,side):
    store_obj=frame(source,borederwidth=4,bd=4,bg="powder blue")
    store_obj.pack(side=side,expand=YES,fill=BOTH)
    return store_obj
def button(source,side,text,command=None):
    store_obj=button(source,text=text,command=command)
    store_obj.pack(side=side,expand=YES,fill=BOTH)
    return store_obj
class app(Frame):
    def __init__(self):
        frame__init__(self)
        self.option_add("*Font","arial 20 bold")
        self.pack(expand=YES,fill=BOth)
        self.master.title('calculator')



        display=stringvar()
        entry(self,relief=RIDGE,
            textvariable=display,justify='right',bd=30,bd=30,bg="powder blue").pack(side=TOP,expand=yes
