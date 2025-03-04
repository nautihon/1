from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhvien =[]
    
    def generateID(self):
        maxId =1
        if (self.soluongsinhvien()>0):
            maxId = self.listSinhvien[0]._id
            for sv in self.listSinhvien:
                if (maxId < sv._id):
                    maxIdd = sv._id
            maxId =maxId+1
        return maxId
    def soluongsinhvien(self):
        return self.listSinhvien.__len__()
    
    def nhapsinhvien(self):
        svId =self.generateID()
        name = input("nhập tên sinh viên:")
        sex = input("nhập giới tính sinh viên:")
        major = input("nhập chuyên ngành của sinh viên:")
        diemTB = float(input("nhập điểm trung bình của sinh viên"))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xeploaihọcluc(sv)
        self.listSinhvien.append(sv)
    def updatesinhvien(self, ID):
        sv:SinhVien= self.findByID(ID)
        if (sv != None):
            name = input("nhập tên sinh viên:")
            sex = input("nhập giới tính sinh viên:")
            major = input("nhập chuyên ngành của sinh viên:")
            diemTB = float(input("nhập điểm trung bình của sinh viên"))
            sv._name =name
            sv._sex =sex
            sv._major =major
            sv._diemTB =diemTB
            self.xeploaihocluc(sv)
        else:
            print("sinh viên có ID ={}không tồn tại.".format(ID))
            
    def sortByID(self):
        self.listSinhvien.sort(key=lambda x: x._id, reverse=False)
    
    def sortByName(self):
        self.listSinhvien.sort(key=lambda x: x._Name, reverse=False)
    
    def sortBydiemTB(self):
        self.listSinhvien.sort(key=lambda x: x._diemTB, reverse=False)
        
    def findByID(self, ID):
        searchResult = None
        if(self.soluongsinhvien()>0):
            for sv in self.listSinhvien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    def findName(self, keyword):
        listSV =[]
        if(self.soluongsinhvien()>0):
            for sv in self.listSinhvien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteById(self,ID):
        isDeleted =False
        sv =self.findByID(ID)
        if (sv != None):
            self.listSinhvien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self,sv:SinhVien):
        if(sv._diemTB>=8):
            sv._hocluc = "Giỏi"
        elif(sv._diemTB>=6.5):
            sv._hocluc = "Khá"
        elif(sv._diemTB>=5):
            sv._hocluc ="Trung Bình"
        else:
            sv._hocluc = "Yếu"
    
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}".format("ID","Name","Sex","Major","Diem TB","Hoc Luc"))
        if(listSV.__len__() >0):
            print ("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}".format(SinhVien._id, SinhVien._name, SinhVien._sex, SinhVien._major, SinhVien._diemTB, SinhVien._hocluc))
        print("\n")
        
    def getlistSinhVien(self):
        return self.listSinhvien
            
    
        