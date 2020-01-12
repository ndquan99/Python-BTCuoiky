from tkinter import *
from dkmh.gui.frame.Userframe import Userframe
from dkmh.gui.frame.Adminframe import Adminframe
from dkmh.user.user import User

class Baseframe(Frame):
    
    def __init__(self, gui, window, wid, hei, type, user):
        super().__init__()
#         self.pack()
        self.gui = gui
        self["height"] = hei
        self["width"] = wid
        self["relief"] = RAISED
        self["bd"] = 1
        self["bg"] = "#f7f5f0"
        if type==1:
            self.gui.resize(1250, 600)
            self.userfr = Userframe(self.gui, self.gui.getWid(), self.gui.getHei(), user)
            self.userfr.grid(row=0, column=0)
        else:
            self.gui.resize(1350, 700)
            self.adminfr = Adminframe(self.gui, self.gui.getWid(), self.gui.getHei())
            self.adminfr.grid(row=0, column=0)
        
