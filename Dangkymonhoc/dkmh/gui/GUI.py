from tkinter import *
from tkinter import messagebox
from tkinter import Tk
from dkmh.gui.frame.Baseframe import Baseframe
from dkmh.gui.frame.LoginFrame import LoginFrame
from dkmh.user.user import User

class GUI():
    
    widthGUI = 700;
    heightGUI = 450;
    
    def __init__(self):
        self.setAttribute()
        self.addComps()
        self.addEvent()
    
    def setAttribute(self):
        self.win = Tk()
        self.win.title("Đăng ký môn học")
        self.win.geometry(str(self.widthGUI)+"x"+str(self.heightGUI)+"+200+100")
        self.win.resizable(0, 0)

        self.log = LoginFrame(self, self.widthGUI, self.heightGUI)
        self.log.grid(row=0, column=0)
    
    def changeToDKMH(self, type, user):
        self.log.grid(row=0, column=10)
        self.baseFr = Baseframe(self, self.win, self.widthGUI, self.heightGUI, type, user)
        self.baseFr.grid(row=0, column=0)
    
    
    def addComps(self):
        
        return
    
    def addEvent(self):
        
        return
    
    def show(self):
        self.win.update()
        self.win.deiconify()
        self.win.mainloop()
        
    def resize(self, w, h):
        self.widthGUI = w
        self.heightGUI = h
        self.win.geometry(str(self.widthGUI)+"x"+str(self.heightGUI)+"+100+60")
        
    def getWid(self):
        return self.widthGUI
    def getHei(self):
        return self.heightGUI
    
    def changeToLogout(self):
        MsgBox = messagebox.askquestion ('Thông báo','Thoát chương trình??',icon = 'warning')
        if MsgBox == 'yes':
#             self.resize(700, 450) 
            self.baseFr.grid(row=0, column=10)
            self.log.grid(row=0, column=0)
        
        
        