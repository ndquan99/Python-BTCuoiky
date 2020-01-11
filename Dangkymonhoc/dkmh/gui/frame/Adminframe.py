from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from _operator import gt

class Adminframe(Frame):
    
    def __init__(self, gui, wid, hei):
        super().__init__()
#         self.pack()
        self.gui = gui
        self["height"] = hei
        self["width"] = wid
        self["relief"] = RAISED
        self["bd"] = 1
        self["bg"] = "#f7f5f0"
        
        lblSchool = Label(self, text="Trường Đại Học Khoa Học Tự Nhiên", font=("Arial", 18, "bold"), fg="#037bfc", bg="#f7f5f0")
        lblSchool.place(x=20, y=10)
        
        lblUsername = Label(self, text="xin chào : " + "Admin", font=("Arial", 12), fg="black", bg="#f7f5f0")
        lblUsername.place(x=940, y=16)

        btnLogout = Button (self, text="Log out", command=self.logout, width=7, fg="blue", bg="#f7f5f0", height=1)
        btnLogout.place(x=1080, y=15)
        fr_ql = Frame(self, width=110, height=640, bg="#a4c0ed")
        fr_ql.place(x=0, y=60)
        
        btnqlsv = Button (fr_ql, text="Quản lí Sinh viên", command=self.updateMainToQLSV, width=14, fg="black", bg="white", height=2)
        btnqlsv.place(x=0, y=30)
        
        btnqlmh = Button (fr_ql, text="Quản lí Môn học", command=self.updateMainToQLMH, width=14, fg="black", bg="white", height=2)
        btnqlmh.place(x=0, y=90)
        
        self.fr_main = Frame(self, width=wid - 110, height=640, bg="white")
        self.fr_main.place(x=110, y=60)
        
        self.fr_qlsv = Frame(self.fr_main, width=wid - 110, height=640, bg="white")
        self.fr_qlsv.grid(row=0, column=1)
        
        self.fr_dsmh = Frame(self.fr_main, width=wid - 110, height=640, bg="white")
        self.fr_dsmh.grid(row=0, column=2)
    
        self.getAllSV()
        self.getAllMH()
        
    def logout(self):
        return    
    
    def updateMainToQLSV(self):
        self.fr_qlsv.grid(row=0, column=0)
        self.fr_dsmh.grid(row=0, column=2)
        return 
    
    def updateMainToQLMH(self):
        self.fr_dsmh.grid(row=0, column=0)
        self.fr_qlsv.grid(row=0, column=1)
        return
    
    def getAllSV(self):
        fr_listSV = Frame(self.fr_qlsv, width=790, height=315, bg="white")
        fr_listSV.place(x=30, y=30)
        self.entry_tkSV = Entry(self.fr_qlsv, bd=2, font=("Arial",12), width="20")
        self.entry_tkSV.place(x=820, y=33)
        btnTimkiemSV = Button (self.fr_qlsv, text="Tìm kiếm", width=8, fg="blue", bg="#e6e1e1", height=1, command=self.timkiemSV)
        btnTimkiemSV.place(x=1010, y=30)
        lb_qlsv = Label(self.fr_qlsv, text="Quản lí sinh viên ", font=("Arial", 12, "bold"), fg="black", bg="white")
        lb_qlsv.place(x=820, y=80)
        lb_msv = Label(self.fr_qlsv, text="MSV :", font=("Arial", 10), fg="black", bg="white")
        lb_msv.place(x=820, y=120)
        self.entry_msv = Label(self.fr_qlsv, text="", font=("Arial",11), fg="black", bg="white")
        self.entry_msv.place(x=870, y=120)
#         self.entry_msv.Ea
        lb_nameSV = Label(self.fr_qlsv, text="Họ tên :", font=("Arial", 10), fg="black", bg="white")
        lb_nameSV.place(x=820, y=165)
        self.entry_nameSV = Entry(self.fr_qlsv, bd=2, font=("Arial",11), width="22")
        self.entry_nameSV.place(x=870, y=165)
        lb_class = Label(self.fr_qlsv, text="Lớp :", font=("Arial", 10), fg="black", bg="white")
        lb_class.place(x=820, y=210)
        self.entry_class = Entry(self.fr_qlsv, bd=2, font=("Arial",11), width="22")
        self.entry_class.place(x=870, y=210)
        lb_gt = Label(self.fr_qlsv, text="GT :", font=("Arial", 10), fg="black", bg="white")
        lb_gt.place(x=820, y=255)
        self.entry_gt = Entry(self.fr_qlsv, bd=2, font=("Arial",11), width="22")
        self.entry_gt.place(x=870, y=255)
        lb_email = Label(self.fr_qlsv, text="Email :", font=("Arial", 10), fg="black", bg="white")
        lb_email.place(x=820, y=300)
        self.entry_email = Entry(self.fr_qlsv, bd=2, font=("Arial",11), width="22")
        self.entry_email.place(x=870, y=300)
        btnChonSV = Button (self.fr_qlsv, text="Chọn", width=15, fg="blue", bg="#e6e1e1", height=2, command=self.chonSV)
        btnChonSV.place(x=820, y=360)
        btnThemSV = Button (self.fr_qlsv, text="Thêm", width=15, fg="blue", bg="#e6e1e1", height=2, command=self.themSV)
        btnThemSV.place(x=960, y=360)
        btnSuaSV = Button (self.fr_qlsv, text="Sửa", width=15, fg="blue", bg="#e6e1e1", height=2, command=self.suaSV)
        btnSuaSV.place(x=820, y=420)
        btnXoaSV = Button (self.fr_qlsv, text="Xóa", width=15, fg="blue", bg="#e6e1e1", height=2, command=self.xoaSV)
        btnXoaSV.place(x=960, y=420)
        btnResetSV = Button (self.fr_qlsv, text="Cập nhật", width=15, fg="blue", bg="#e6e1e1", height=2, command=self.resetDataSV)
        btnResetSV.place(x=960, y=480)
        self.dataColsSV = ("      Mã Sinh Viên      ", "      Họ và Tên      ", "      Lớp      ", "      Giới tính      ", "      Email      ")        
        self.treeSV = ttk.Treeview(height=27, columns=self.dataColsSV, 
                                 show = 'headings')
          
        ysb = ttk.Scrollbar(orient=VERTICAL, command= self.treeSV.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command= self.treeSV.xview)
        self.treeSV['yscroll'] = ysb.set
        self.treeSV['xscroll'] = xsb.set
        # add tree and scrollbars to frame
        self.treeSV.grid(in_=fr_listSV, row=0, column=0, sticky=NSEW)
#             self.tree.place(x=0, y=0)
        ysb.grid(in_=fr_listSV, row=0, column=1, sticky=NS)
        xsb.grid(in_=fr_listSV, row=1, column=0, sticky=EW)
        # set frame resize priorities
        fr_listSV.rowconfigure(0, weight=1)
        fr_listSV.columnconfigure(0, weight=1)
        self.addDataSV()
        return 
    
    def addDataSV(self):
        self.dataSV = [
                ["17000300", "Nguyễn Văn A", "K62-A4-Mt&khtt", "Nam", "nguyenvana_t62@hus.edu.vn"],
                ["17000301", "Nguyễn Văn B", "K62-A4-Mt&khtt", "Nữ", "nguyenvanb_t62@hus.edu.vn"],
                ["17000302", "Nguyễn Văn C", "K62-A4-Mt&khtt", "Nam", "nguyenvanc_t62@hus.edu.vn"]]
        # configure column headings
        for c in self.dataColsSV:
            self.treeSV.heading(c, text=c.title(),
            command=lambda c=c: self._column_sort(c))            
            self.treeSV.column(c, width='150')
        # add data to the tree 
        for item in self.dataSV: 
            vls = (str(item[0]), str(item[1]), str(item[2]), str(item[3]), str(item[4]))
            self.treeSV.insert('', 'end', values=vls)
        return
    
    def getAllMH(self):
        fr_listMH = Frame(self.fr_dsmh, width=790, height=315, bg="white")
        fr_listMH.place(x=30, y=30)
        self.entry_tkMH = Entry(self.fr_dsmh, bd=2, font=("Arial",12), width="20")
        self.entry_tkMH.place(x=820, y=33)
        btnTimkiemMH = Button (self.fr_dsmh, text="Tìm kiếm", width=8, fg="blue", bg="#e6e1e1", height=1, command=self.timkiemMH)
        btnTimkiemMH.place(x=1010, y=30)
        lb_qlMH = Label(self.fr_dsmh, text="Quản lí môn học ", font=("Arial", 12, "bold"), fg="black", bg="white")
        lb_qlMH.place(x=820, y=80)
        lb_mmh = Label(self.fr_dsmh, text="Mã MH :", font=("Arial", 10), fg="black", bg="white")
        lb_mmh.place(x=820, y=120)
        self.entry_mmh = Label(self.fr_dsmh, text="", font=("Arial",11), fg="black", bg="white")
        self.entry_mmh.place(x=885, y=120)
        lb_nameMH = Label(self.fr_dsmh, text="Môn học :", font=("Arial", 10), fg="black", bg="white")
        lb_nameMH.place(x=820, y=165)
        self.entry_nameMH = Entry(self.fr_dsmh, bd=2, font=("Arial",11), width="22")
        self.entry_nameMH.place(x=885, y=165)
        lb_soTC = Label(self.fr_dsmh, text="Số TC :", font=("Arial", 10), fg="black", bg="white")
        lb_soTC.place(x=820, y=210)
        self.entry_soTC = Entry(self.fr_dsmh, bd=2, font=("Arial",11), width="22")
        self.entry_soTC.place(x=885, y=210)
        lb_class = Label(self.fr_dsmh, text="Lớp :", font=("Arial", 10), fg="black", bg="white")
        lb_class.place(x=820, y=255)
        self.entry_classMH = Entry(self.fr_dsmh, bd=2, font=("Arial",11), width="22")
        self.entry_classMH.place(x=885, y=255)
        lb_time = Label(self.fr_dsmh, text="Thời gian:", font=("Arial", 10), fg="black", bg="white")
        lb_time.place(x=820, y=300)
        self.entry_time = Entry(self.fr_dsmh, bd=2, font=("Arial",11), width="22")
        self.entry_time.place(x=885, y=300)
        btnChonSV = Button (self.fr_dsmh, text="Chọn", width=15, fg="blue", bg="#e6e1e1", height=2, command=self.chonMH)
        btnChonSV.place(x=820, y=360)
        btnThemSV = Button (self.fr_dsmh, text="Thêm", width=15, fg="blue", bg="#e6e1e1", height=2, command=self.themMH)
        btnThemSV.place(x=960, y=360)
        btnSuaSV = Button (self.fr_dsmh, text="Sửa", width=15, fg="blue", bg="#e6e1e1", height=2, command=self.suaMH)
        btnSuaSV.place(x=820, y=420)
        btnXoaSV = Button (self.fr_dsmh, text="Xóa", width=15, fg="blue", bg="#e6e1e1", height=2, command=self.xoaMH)
        btnXoaSV.place(x=960, y=420)
        btnResetSV = Button (self.fr_dsmh, text="Cập nhật", width=15, fg="blue", bg="#e6e1e1", height=2, command=self.resetDataMH)
        btnResetSV.place(x=960, y=480)
        self.dataColsMH = ("      Mã Môn học      ", "      Tên Môn học      ", "      Số Tín      ", "      Lớp      ", "      Thời gian      ")        
        self.treeMH = ttk.Treeview(height=27, columns=self.dataColsMH, 
                                 show = 'headings')
          
        ysb = ttk.Scrollbar(orient=VERTICAL, command= self.treeMH.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command= self.treeMH.xview)
        self.treeMH['yscroll'] = ysb.set
        self.treeMH['xscroll'] = xsb.set
        # add tree and scrollbars to frame
        self.treeMH.grid(in_=fr_listMH, row=0, column=0, sticky=NSEW)
#             self.tree.place(x=0, y=0)
        ysb.grid(in_=fr_listMH, row=0, column=1, sticky=NS)
        xsb.grid(in_=fr_listMH, row=1, column=0, sticky=EW)
        # set frame resize priorities
        fr_listMH.rowconfigure(0, weight=1)
        fr_listMH.columnconfigure(0, weight=1)
        self.addDataMH()
        return
    
    def addDataMH(self):
        self.dataMH = [
                ["12345", "Bóng chuyền hơi", "1", "KTX", "T3-(6-8)-KTX Mễ Trì"],
                ["12346", "Bóng chuyền", "1", "KTX", "T4-(6-8)-KTX Mễ Trì"]]
        # configure column headings
        for c in self.dataColsMH:
            self.treeMH.heading(c, text=c.title(),
            command=lambda c=c: self._column_sort(c))            
            self.treeMH.column(c, width='150')
        # add data to the tree 
        for item in self.dataMH: 
            vls = (str(item[0]), str(item[1]), str(item[2]), str(item[3]), str(item[4]))
            self.treeMH.insert('', 'end', values=vls)
        return
    
    def timkiemSV(self):
        infor = str(self.entry_tkSV.get())
        if len(infor)==0:
            return
        else:
            arrSV = []
            for sv in self.dataSV:
                if str(sv[0])==infor or infor.lower() in str(sv[1]).lower():
                    vls = (sv[0], sv[1], str(sv[2]), str(sv[3]), str(sv[4]))
                    arrSV.append(vls)
            if len(arrSV)>0:
                self.changeDataSV(arrSV)
    
    def chonSV(self):
        item = self.treeSV.item(self.treeSV.focus())
        itemValues = item['values']
        if len(itemValues)==0:
            return
        else:
            self.entry_msv['text'] = itemValues[0]
            self.entry_nameSV.delete(0, END)
            self.entry_nameSV.insert(0, itemValues[1])
            self.entry_class.delete(0, END)
            self.entry_class.insert(0, itemValues[2])
            self.entry_gt.delete(0, END)
            self.entry_gt.insert(0, itemValues[3])
            self.entry_email.delete(0, END)
            self.entry_email.insert(0, itemValues[4])
    
    def suaSV(self):
        msv = str(self.entry_msv['text'])
        if len(msv)==0:
            return
        else:
            name = self.entry_nameSV.get()
            lop = self.entry_class.get()
            gt = self.entry_gt.get()
            email = self.entry_email.get()
            if len(name)==0 or len(lop)==0 or len(gt)==0 or len(email)==0:
                return
            else:
                MsgBox = messagebox.askquestion ('Thông báo','Chấp nhận thay đổi??',icon = 'warning')
                if MsgBox == 'yes':
                    for sv in self.dataSV:
                        if str(sv[0])==msv:
                            sv[1] = name
                            sv[2] = lop
                            sv[3] = gt
                            sv[4] = email
                            self.changeDataSV(self.dataSV)
                            return
                    MsgBox2 = messagebox.askquestion ('Thông báo','Không tìm thấy mã sv '+msv,icon = 'warning')
    
    def xoaSV(self):
        item = self.treeSV.item(self.treeSV.focus())
        itemValues = item['values']
        if len(itemValues)==0:
            return
        else:
            msv = itemValues[0]
            count = 0
            for sv in self.dataSV:
                if str(sv[0])==str(msv):
                    MsgBox = messagebox.askquestion ('Thông báo','Chấp nhận thay đổi??',icon = 'warning')
                    if MsgBox == 'yes':
                        del self.dataSV[count]
                        self.changeDataSV(self.dataSV)
                    break
                count = count + 1
            
    def themSV(self):
        svMax = self.dataSV[len(self.dataSV)-1]
        msvMax = int(svMax[0])
        msv = str(msvMax+1)
        name = self.entry_nameSV.get()
        lop = self.entry_class.get()
        gt = self.entry_gt.get()
        email = self.entry_email.get()
        if len(msv)==0 or len(name)==0 or len(lop)==0 or len(gt)==0 or len(email)==0:
            return
        else:
            for sv in self.dataSV:
                if str(sv[4])==str(email):
                    MsgBox2 = messagebox.askquestion ('Thông báo','Email đã tồn tại',icon = 'warning')
                    return
            MsgBox = messagebox.askquestion ('Thông báo','Chấp nhận thay đổi??',icon = 'warning')
            if MsgBox == 'yes':
                vls = [msv, name, lop, gt, email]
                self.dataSV.append(vls)
                self.changeDataSV(self.dataSV)
    
    def changeDataSV(self, arr):
        self.removeDataSV()
        for item in arr: 
            vls = (item[0], item[1], str(item[2]), str(item[3]), str(item[4]))
            self.treeSV.insert('', 'end', values=vls)
        return
    
    def removeDataSV(self):
        x = self.treeSV.get_children()
        if(x != '()') :
            for child in x:
                self.treeSV.delete(child)
    
    def removeDataMH(self):
        x = self.treeMH.get_children()
        if(x != '()') :
            for child in x:
                self.treeMH.delete(child)
                
    def resetDataSV(self):
        self.removeDataSV()
        self.changeDataSV(self.dataSV)
        
    def chonMH(self):
        item = self.treeMH.item(self.treeMH.focus())
        itemValues = item['values']
        if len(itemValues)==0:
            return
        else:
            self.entry_mmh['text'] = itemValues[0]
            self.entry_nameMH.delete(0, END)
            self.entry_nameMH.insert(0, itemValues[1])
            self.entry_soTC.delete(0, END)
            self.entry_soTC.insert(0, itemValues[2])
            self.entry_classMH.delete(0, END)
            self.entry_classMH.insert(0, itemValues[3])
            self.entry_time.delete(0, END)
            self.entry_time.insert(0, itemValues[4])
    
    def themMH(self):
        return
    
    def xoaMH(self):
        item = self.treeMH.item(self.treeMH.focus())
        itemValues = item['values']
        if len(itemValues)==0:
            return
        else:
            mmh = itemValues[0]
            count = 0
            for mh in self.dataMH:
                if str(mh[0])==str(mmh):
                    MsgBox = messagebox.askquestion ('Thông báo','Chấp nhận thay đổi??',icon = 'warning')
                    if MsgBox == 'yes':
                        del self.dataMH[count]
                        self.changeDataMH(self.dataMH)
                    break
                count = count + 1
    
    def resetDataMH(self):
        self.removeDataMH()
        self.changeDataMH(self.dataMH)
    
    def timkiemMH(self):
        infor = str(self.entry_tkMH.get())
        if len(infor)==0:
            return
        else:
            arrMH = []
            for mh in self.dataMH:
                if str(mh[0])==infor or infor.lower() in str(mh[1]).lower():
                    vls = (mh[0], mh[1], str(mh[2]), str(mh[3]), str(mh[4]))
                    arrMH.append(vls)
            if len(arrMH)>0:
                self.changeDataMH(arrMH)
    
    def suaMH(self):
        return
    
    def changeDataMH(self, arr):
        self.removeDataMH()
        for item in arr: 
            vls = (item[0], item[1], str(item[2]), str(item[3]), str(item[4]))
            self.treeMH.insert('', 'end', values=vls)
        
    