from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from dkmh.database.Database import DB
from dkmh.user.user import User

class Userframe(Frame):
    
    def __init__(self, gui, wid, hei, user):
        super().__init__()
#         self.pack()
        self.db = DB()
        self.user = user
        self.gui = gui
        self["height"] = hei
        self["width"] = wid
        self["relief"] = RAISED
        self["bd"] = 1
        self["bg"] = "#f7f5f0"
        self.inforSV = self.db.getInforUser(self.user.getUsn())
#         print(self.inforSV)
        
        lblSchool = Label(self, text="Trường Đại Học Khoa Học Tự Nhiên", font=("Arial", 18, "bold"), fg="#037bfc", bg="#f7f5f0")
        lblSchool.place(x=20, y=10)
        
        lblUsername = Label(self, text="Mã SV: " + str(self.inforSV['maSV']), font=("Arial", 12), fg="#037bfc", bg="#f7f5f0")
        lblUsername.place(x=765, y=16)

        btnLogout = Button (self, text="Log out", command=self.logout, width=7, fg="blue", bg="#f7f5f0", height=1)
        btnLogout.place(x=920, y=15)
        fr_ql = Frame(self, width=150, height=540, bg="#a4c0ed")
        fr_ql.place(x=0, y=60)
        
        self.fr_main = Frame(self, width=wid - 150, height=540, bg="white")
        self.fr_main.place(x=150, y=60)
        
#         main frame
        
        btnTTCN = Button (fr_ql, text="Thông tin cá nhân", command=self.updateMainToTTCN, width=14, fg="blue", bg="#e6e1e1", height=2)
        btnTTCN.place(x=20, y=30)
        
        btnDKMH = Button (fr_ql, text="Đăng Kí Môn Học", command=self.updateMainToDKMH, width=14, fg="blue", bg="#e6e1e1", height=2)
        btnDKMH.place(x=20, y=90)
        
        btnDSMH = Button (fr_ql, text="Danh sách môn học", command=self.updateMainToDSMH, width=14, fg="blue", bg="#e6e1e1", height=2)
        btnDSMH.place(x=20, y=150)
        
        self.fr_title =  Frame(self.fr_main, width=wid - 150, height=540, bg="white")
        self.fr_title.grid(row=0, column=0)
        
        lblIntro = Label(self.fr_title, text="Hệ Thống Đăng Kí Môn Học", font=("Arial", 20, "bold"), fg="black", bg="white")
        lblIntro.place(x=30, y=30)   
        
#             frame thong tin ca nhan
        self.fr_ttcn = Frame(self.fr_main, width=wid - 150, height=540, bg="white")
        lblTtcn = Label(self.fr_ttcn, text="Thông tin cá nhân", font=("Arial", 18, "bold"), fg="black", bg="white")
        lblTtcn.place(x=280, y=25)
        self.fr_ttcn.grid(row=0, column=1)
        
#             frame dkmh
        self.fr_dkmh = Frame(self.fr_main, width=wid - 150, height=540, bg="white")
        lblDkmh = Label(self.fr_dkmh, text="Đăng Kí Môn Học", font=("Arial", 18, "bold"), fg="black", bg="white")
        lblDkmh.place(x=30, y=25)
        self.fr_dkmh.grid(row=0, column=2)
        
        self.fr_dsmh = Frame(self.fr_main, width=wid - 150, height=540, bg="white")
        lblDsmh = Label(self.fr_dsmh, text="Danh sách môn học đã đăng ký :", font=("Arial", 18, "bold"), fg="black", bg="white")
        lblDsmh.place(x=30, y=25)
        self.fr_dkmh.grid(row=0, column=3)
        
        
        
        self.addInforToTTCN()
        self.addDataToDKFR()
        self.addToDSMH()
        
    def logout(self):
        self.gui.changeToLogout()
        return
    
    def updateMainToTTCN(self):
        self.fr_title.grid(row=0, column=1)
        self.fr_dkmh.grid(row=0, column=2)
        self.fr_dsmh.grid(row=0, column=3)
        self.fr_ttcn.grid(row=0, column=0)
        return
    def updateMainToDKMH(self):
        self.fr_title.grid(row=0, column=1)
        self.fr_dkmh.grid(row=0, column=0)
        self.fr_ttcn.grid(row=0, column=2)
        self.fr_dsmh.grid(row=0, column=3)
        return
    
    def updateMainToDSMH(self):
        self.fr_title.grid(row=0, column=1)
        self.fr_dkmh.grid(row=0, column=3)
        self.fr_ttcn.grid(row=0, column=2)
        self.fr_dsmh.grid(row=0, column=0)
        return
    
    def addInforToTTCN(self):
        msv = Label(self.fr_ttcn, text="Mã Sinh viên: "+str(self.inforSV['maSV']), font=("Arial", 11), fg="black", bg="white")
        msv.place(x=30, y=80)
        name = Label(self.fr_ttcn, text="Họ và tên: "+str(self.inforSV['hoTen']), font=("Arial", 11), fg="black", bg="white")
        name.place(x=30, y=115)
        age = Label(self.fr_ttcn, text="Ngày sinh: ", font=("Arial", 11), fg="black", bg="white")
        age.place(x=30, y=145)
        cmt = Label(self.fr_ttcn, text="Lớp: "+str(self.inforSV['lop']), font=("Arial", 11), fg="black", bg="white")
        cmt.place(x=30, y=175)
        dt = Label(self.fr_ttcn, text="Khoa: "+str(self.inforSV['khoa']), font=("Arial", 11), fg="black", bg="white")
        dt.place(x=30, y=205)
        nguyenquan = Label(self.fr_ttcn, text="Nguyên quán:", font=("Arial", 11), fg="black", bg="white")
        nguyenquan.place(x=30, y=235)
        noht = Label(self.fr_ttcn, text="Nơi ở hiện nay: "+str(self.inforSV['diaChi']), font=("Arial", 11), fg="black", bg="white")
        noht.place(x=30, y=265)
        dtdd = Label(self.fr_ttcn, text="Điện thoại di động: ", font=("Arial", 11), fg="black", bg="white")
        dtdd.place(x=30, y=295)
        gt = Label(self.fr_ttcn, text="Giới tính: "+str(self.inforSV['gioiTinh']), font=("Arial", 11), fg="black", bg="white")
        gt.place(x=450, y=115)
        ns = Label(self.fr_ttcn, text="Nơi sinh: ", font=("Arial", 11), fg="black", bg="white")
        ns.place(x=450, y=145)
        qt = Label(self.fr_ttcn, text="Quốc tịch: ", font=("Arial", 11), fg="black", bg="white")
        qt.place(x=450, y=175)
        email = Label(self.fr_ttcn, text="Email: "+str(self.inforSV['email']), font=("Arial", 11), fg="black", bg="white")
        email.place(x=450, y=205)
        
        ttht = Label(self.fr_ttcn, text="Thông tin học tập:", font=("Arial", 15, "bold"), fg="black", bg="white")
        ttht.place(x=30, y=345)
        
        return
    
    def addDataToDKFR(self):
        self.count = 0
        fr_listSV = Frame(self.fr_dkmh, width=790, height=315, bg="white")
        fr_listSV.place(x=30, y=70)
        slmh = Label(self.fr_dkmh, text="Số lượng đã thêm :", font=("Arial", 10, "bold"), fg="black", bg="white")
        slmh.place(x=30, y=460)
        self.countMH = Label(self.fr_dkmh, text=str(self.count), font=("Arial", 10, "bold"), fg="black", bg="white")
        self.countMH.place(x=170, y=460)
        btnAddMH = Button (self.fr_dkmh, text="Đăng ký", width=10, fg="blue", bg="#e6e1e1", height=2, command=self.addMH)
        btnAddMH.place(x=200, y=450)
        self.mess = Label(self.fr_dkmh, text="", font=("Arial", 10, "bold"), fg="green", bg="white")
        self.mess.place(x=300, y=460)
        self.dataCols = ("      Mã Môn học      ", "      Tên Môn học      ", "      Số Tín      ", "      Số lượng      ", "      Lớp      ", "      Thời gian      ", "      Điểm      ")        
        self.tree = ttk.Treeview(height=16, columns=self.dataCols, 
                                 show = 'headings')
          
        ysb = ttk.Scrollbar(orient=VERTICAL, command= self.tree.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command= self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set
        # add tree and scrollbars to frame
        self.tree.grid(in_=fr_listSV, row=0, column=0, sticky=NSEW)
#             self.tree.place(x=0, y=0)
        ysb.grid(in_=fr_listSV, row=0, column=1, sticky=NS)
        xsb.grid(in_=fr_listSV, row=1, column=0, sticky=EW)
        # set frame resize priorities
        fr_listSV.rowconfigure(0, weight=1)
        fr_listSV.columnconfigure(0, weight=1)
        self.addDataMH()
        
    def addDataMH(self):
#         0:chua qua 1:qua r va ko dc hoc cai thien 2: qua r va dc hoc cai thien
        self.data = [
                ["12345", "Bóng chuyền hơi", "1", "50", "50",  "KTX", "T3-(6-8)",   "F"],
                ["12346", "Bóng chuyền hơi", "1", "49", "50",  "KTX", "T4-(6-8)",   "F"],
                ["12347", "Toán rời rạc",    "3", "44", "100", "102T5", "T5-(6-8)", "C"],
                ["12348", "Toán rời rạc",    "3", "30", "100", "102T5", "T2-(3-5)", "C"],
                ["12349", "Toán rời rạc",    "3", "22", "100", "102T5", "T3-(1-3)", "C"],
                ["12350", "Python",          "2", "30", "70",  "502T5", "T4-(1-2)", ""],
                ["12351", "Python",          "2", "2",  "70",  "503T5", "T3-(1-3)", ""],
                ["12352", "C/C++",           "2", "10", "70",  "501T5", "T6-(6-8)", ""],
                ["12353", "C/C++",           "2", "41", "70",  "501T5", "T3-(1-3)", ""]]
        # configure column headings
        for c in self.dataCols:
            self.tree.heading(c, text=c.title(),
            command=lambda c=c: self._column_sort(c))            
            self.tree.column(c, width='150')
        # add data to the tree 
        for item in self.data:
            sl = str(item[3]) + "/" + str(item[4])
            vls = (item[0], item[1], str(item[2]), sl, str(item[5]), str(item[6]), str(item[7]))
            self.tree.insert('', 'end', values=vls)
    
    def _column_sort(self, c):
        return 0
    
    def addMH(self):
        item = self.tree.item(self.tree.focus())
        itemValues = item['values']
        if len(itemValues)==0:
            return
        else:
            mmh = str(itemValues[0])
            for mh in self.dataDK:
                if str(mh[0])==mmh:
                    MsgBox = messagebox.askquestion ('Thông báo','Môn học này đã đăng kí',icon = 'warning')
                    self.mess['text'] = ""
                    return
                elif str(mh[1])==str(itemValues[1]) or str(mh[5])==str(itemValues[5]):
                    MsgBox = messagebox.askquestion ('Thông báo','Môn học bị trùng lịch',icon = 'warning')
                    self.mess['text'] = ""
                    return
            for mh in self.data:
                if str(mh[0])==mmh:
                    if int(str(mh[3]))>=int(str(mh[4])):
                        MsgBox2 = messagebox.askquestion ('Thông báo','Môn học đã đủ số lượng',icon = 'warning')
                        self.mess['text'] = ""
                        return
                    diem = str(mh[7])
                    type = ""
                    if diem == "F":
                        type = "Đăng kí học lại"
                    elif diem == "D" or diem == "D+":
                        type = "Đăng kí học cải thiện"
                    elif diem == "":
                        type = "Đăng kí lần đầu"
                    else:
                        MsgBox1 = messagebox.askquestion ('Thông báo','Môn học không đủ điều kiền để học lại hoặc cải thiện !!',icon = 'warning')
                        self.mess['text'] = ""
                        return
                    MsgBox = messagebox.askquestion ('Thông báo','Thêm môn học vào danh sách??',icon = 'warning')
                    if MsgBox == 'yes':
                        vls = (str(mh[0]), str(mh[1]), str(mh[2]), type, str(mh[5]), str(mh[6]))
                        self.dataDK.append(vls)
        #                         print(self.dataDK)
                        slht = int(str(mh[3])) + 1
                        mh[3] = str(slht)
                        self.mess['text'] = "Thêm môn học thành công"
                        self.resetAllMH()
                        self.resetMHDK()
                        self.updateCountMHDK(1)
                    break
    
    def addToDSMH(self):
        fr_dsdk = Frame(self.fr_dsmh, width=790, height=315, bg="white")
        fr_dsdk.place(x=30, y=70)
        btnXoa = Button (self.fr_dsmh, text="Xóa", width=10, fg="white", bg="red", height=2, command=self.xoaMHDK)
        btnXoa.place(x=600, y=450)
        btnDK = Button (self.fr_dsmh, text="Đăng kí Thêm", width=10, fg="white", bg="green", height=2, command=self.updateMainToDKMH)
        btnDK.place(x=700, y=450)
        self.slmh = 0
        self.sldk = Label(self.fr_dsmh, text="Số lượng môn học : "+str(self.slmh), font=("Arial", 10, "bold"), fg="black", bg="white")
        self.sldk.place(x=30, y=460)
        self.soTC = 0
        self.sltc = Label(self.fr_dsmh, text="Số Tín : "+str(self.soTC), font=("Arial", 10, "bold"), fg="black", bg="white")
        self.sltc.place(x=190, y=460)
        self.dataColsDSDK = ("      Mã Môn học      ", "      Tên Môn học      ", "      Số Tín      ", "      Lần ĐK      ", "      Lớp      ", "      Thời gian      ")        
        self.treeDSDK = ttk.Treeview(height=16, columns=self.dataColsDSDK, 
                                 show = 'headings')
          
        ysb = ttk.Scrollbar(orient=VERTICAL, command= self.treeDSDK.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command= self.treeDSDK.xview)
        self.treeDSDK['yscroll'] = ysb.set
        self.treeDSDK['xscroll'] = xsb.set
        # add tree and scrollbars to frame
        self.treeDSDK.grid(in_=fr_dsdk, row=0, column=0, sticky=NSEW)
#             self.tree.place(x=0, y=0)
        ysb.grid(in_=fr_dsdk, row=0, column=1, sticky=NS)
        xsb.grid(in_=fr_dsdk, row=1, column=0, sticky=EW)
        # set frame resize priorities
        fr_dsdk.rowconfigure(0, weight=1)
        fr_dsdk.columnconfigure(0, weight=1)
        for c in self.dataColsDSDK:
            self.treeDSDK.heading(c, text=c.title(),
            command=lambda c=c: self._column_sort(c))            
            self.treeDSDK.column(c, width='150')
        self.updateDSDK()
    
    def updateDSDK(self):
        self.clearMH()
#         self.dataDK = [
#                 ("12346", "Bóng chuyền hơi", "1", "Đăng kí học lại", "KTX",   "T4-(6-8)-KTX Mễ Trì"),
#                 ("12350", "Python",          "2", "Đăng kí lần đầu", "502T5", "T4-(1-2)-402T5")]
        self.dataDK = []
        for item in self.dataDK: 
            vls = (item[0], item[1], str(item[2]), str(item[3]), str(item[4]), str(item[5]))
            self.treeDSDK.insert('', 'end', values=vls)
        self.slmh = len(self.dataDK)
        for mh in self.dataDK:
            self.soTC = self.soTC + int(mh[2])
        self.sldk['text'] = "Số lượng môn học : "+str(self.slmh)
        self.sltc['text'] = "Số Tín : "+str(self.soTC)
        
    def clearMH(self):
        x = self.treeDSDK.get_children()
        if(x != '()') :
            for child in x:
                self.treeDSDK.delete(child)
    
    def clearAllMH(self):
        x = self.tree.get_children()
        if(x != '()') :
            for child in x:
                self.tree.delete(child)
    
            
    def xoaMHDK(self):
        item = self.treeDSDK.item(self.treeDSDK.focus())
        itemValues = item['values']
        if len(itemValues)==0:
            return
        else:
            mmh = itemValues[0]
            count = 0
            for mh in self.dataDK:
                if str(mh[0])==str(mmh):
                    MsgBox = messagebox.askquestion ('Thông báo','Xóa môn học đăng kí??',icon = 'warning')
                    if MsgBox == 'yes':
                        del self.dataDK[count]
                        for mh1 in self.data:
                            if str(mh1[0])==str(mmh):
                                slht = int(str(mh1[3])) - 1
                                mh1[3] = str(slht)
                        self.resetAllMH()
                        self.resetMHDK()
                        self.updateCountMHDK(-1)
                    break
                count = count + 1
    
    def updateCountMHDK(self, sl):
        self.count = self.count + sl
        self.countMH['text'] = str(self.count)
        self.soTC = 0
        for mh in self.dataDK:
            self.soTC = self.soTC + int(mh[2])
        self.slmh = len(self.dataDK)
        self.sldk['text'] = "Số lượng môn học : "+str(self.slmh)
        self.sltc['text'] = "Số Tín : "+str(self.soTC)
        
    def resetAllMH(self):
        self.clearAllMH()
        for item in self.data:
            sl = str(item[3]) + "/" + str(item[4])
            vls = (item[0], item[1], str(item[2]), sl, str(item[5]), str(item[6]), str(item[7]))
            self.tree.insert('', 'end', values=vls)
    def resetMHDK(self):
        self.clearMH()
        for item in self.dataDK: 
            vls = (item[0], item[1], str(item[2]), str(item[3]), str(item[4]), str(item[5]))
            self.treeDSDK.insert('', 'end', values=vls)
