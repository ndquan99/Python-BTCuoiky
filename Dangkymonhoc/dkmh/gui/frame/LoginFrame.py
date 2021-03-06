from tkinter import *
from tkinter import Frame
from dkmh.database.Database import DB
from dkmh.user.user import User


class LoginFrame(Frame):
    
    def __init__(self, window, wid, hei):
        super().__init__()
#         self.pack()
        self.db = DB()
        self.winlg = window
        self["height"] = hei
        self["width"] = wid
        self["relief"] = RAISED
        self["bd"] = 1
        self["bg"] = "#f7f5f0"
        lblIntro = Label(self, text="Hệ Thống Đăng Ký Môn Học", font=("Arial", 20, "bold"), fg="#037bfc", bg="#f7f5f0")
        lblIntro.place(x=150, y=50)
        lblUser = Label(self, text="User :", font=("Arial", 13), bg="#f7f5f0")
        lblUser.place(x=150, y=150)
        self.user = Entry(self, bd=1, font="Arial", width="30")
        self.user.place(x=200, y=150)
        # pass
        lblPassword = Label(self, text="Password :", font=("Arial", 13), bg="#f7f5f0")
        lblPassword.place(x=115, y=220)
        self.pw = Entry(self, bd=1, show="*", width="30", font="Arial")
        self.pw.place(x=200, y=220)
        
        self.lblerror = Label(self, text="", font=("Arial", 10), bg="#f7f5f0", fg="red")
        self.lblerror.place(x=200, y=260)
        # button dang nhap
        btnLogin = Button (self, text = "Login", width=10, fg="green", bg="#e6e1e1", height=2, command=self.logsuccess)
        btnLogin.place(x=464, y=300)
        
    def logsuccess(self):
        usn = str(self.user.get())
        pw = str(self.pw.get())
        pq = self.db.checkUser(usn, pw)
        if len(usn)==0 or len(pw)==0:
            return
        elif pq==1:
            self.winlg.changeToDKMH(0, User(usn, pw, pq))
            self.lblerror['text'] = "" 
        elif pq==2:
            self.winlg.changeToDKMH(1, User(usn, pw, pq))
            self.lblerror['text'] = ""
        else:
            self.lblerror['text'] = "Sai tài khoản hoặc mật khẩu !"
        
        
        
        
        