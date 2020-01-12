import pymysql.cursors

class DB():
    def __init__(self):
        self.columnSV = "sinh_vien"
        self.columnMH = "mon_hoc"
        self.columnSVKH = "sv_kyhoc"
        self.columnSVMH = "sv_monhoc"
        self.columnUser = "user"
#         try:
#             with self.connection.cursor() as cursor:
#                 # SQL 
#                 sql = "SELECT MaMH, TenMH FROM monhoc"
#           
#                 # Thực thi câu lệnh truy vấn (Execute Query).
#                 cursor.execute(sql)
#                   
#                 print ("cursor.description: ", cursor.description)
#           
#                 print()
#           
#                 for row in cursor:
#                     print(row)
#               
#         finally:
#             # Đóng kết nối (Close connection).       
#             self.connection.close()
            
    def getConnection(self):
        # Bạn có thể thay đổi các thông số kết nối.
        connection = pymysql.connect(host='127.0.0.1',
            user='root',
            password='',                             
            db='dkqlmh',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        return connection
    
    def checkUser(self, usn, pw):
        conn = self.getConnection()
        print("Connect successfully!!")
        try:
            with conn.cursor() as cursor:
                # SQL 
                sql = "SELECT * FROM " + self.columnUser + " WHERE tenDangNhap='" + str(usn) + "' AND matKhau='" + str(pw) + "'"
                # Thực thi câu lệnh truy vấn (Execute Query).
                cursor.execute(sql)
                row_count = cursor.rowcount
                
                if row_count==0:
                    q = -1
                for row in cursor:
#                     print(row['phanquyen'])
                    q = row['phanquyen']
              
        finally:
            # Đóng kết nối (Close connection).       
            conn.close()
            
        return q
            
    def getInforUser(self, usn):
        conn = self.getConnection()
        print("Connect successfully!!")
        try:
            with conn.cursor() as cursor:
                # SQL 
                sql = "SELECT maSV, hoTen, lop, khoa, gioiTinh, email, diaChi FROM sinh_vien INNER JOIN user on sinh_vien.tenDangNhap = user.tenDangNhap WHERE user.tenDangNhap='"+usn+"'"      
                # Thực thi câu lệnh truy vấn (Execute Query).
                cursor.execute(sql)
                row_count = cursor.rowcount
                if row_count==0:
                    print("khong tt")
#                     return -1
                
                for row in cursor:
                    infor = row
#                     return row['phanquyen']
              
        finally:
            # Đóng kết nối (Close connection).       
            conn.close()
        
        return infor
        
    def changeToList(self, list, arr):
        for pt in arr:
            list.append(pt)
            
    def getTTHK(self, usn):
        return
        