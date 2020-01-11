from tkinter import *
from tkinter import messagebox
from tkinter import Tk
from dkmh.gui.frame.LoginFrame import LoginFrame
# from dkmh.gui.GUI import GUI

class GUILg():
    
    widthLg = 700;
    heightLg = 450;
    
    def __init__(self, main):
        self.main = main
        self.setAttribute()
        self.addComps()
        self.addEvent()
    
    def setAttribute(self):
        self.winlg = Tk()
        self.winlg.title("Đăng ký môn học")
        self.winlg.geometry(str(self.widthLg)+"x"+str(self.heightLg)+"+300+100")
        self.winlg.resizable(0, 0)
        
        self.log = LoginFrame(self, self.widthLg, self.heightLg)
        self.log.grid(row=0, column=0)
    
    def loginsuccess(self, type):
        self.hide()
        self.main.logToDKMH(type)
    def hide(self):
        self.winlg.withdraw()
    
    def addComps(self):
        
        return
    
    def addEvent(self):
        
        return
    
    def show(self):
        self.winlg.update()
        self.winlg.deiconify()
        self.winlg.mainloop()