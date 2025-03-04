from QuanlySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\n CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ")
    print("**********************************************************************************************")
    print("********   1. THÊM SINH VIEN.")
    print("********   2. CẬP NHẬT THÔNG TIN SINH VIÊN BỞI ID.")
    print("********   3. XÓA SINH VIÊN BỞI ID.")
    print("********   4. TÌM KIẾM SINH VIÊN THEO TÊN.")
    print("********   5. SẮP XẾP SINH VIÊN THEO ĐIỂM TRUNG BÌNH.")
    print("********   6. SẮP XẾP SINH VIÊN THEO TÊN CHUYÊN NGÀNH.")
    print("********   7. HIỂN THỊ DANH SÁCH SINH VIÊN.")
    print("********   0. THOÁT.")
    print("**********************************************************************************************")
    
    
    key = int(input("Nhấp tùy chọn"))
    if(key == 1):
        print("\n1. TTHÊM SINH VIÊN.")
        qlsv.nhapsinhvien()
        print("\n THÊM SINH VIÊN THÀNH CÔNG")
    elif (key == 2):
        if(qlsv.soluongsinhvien()>0):
            print("\n2. CẬP NHẬT THÔNG TIN SINH VIÊN BỞI ID.")
            print("\n Nhập ID:")
            id = int(input())
            qlsv.updatesinhvien(id)
        else:
            print("\n DANH SÁCH SINH VIÊN TRONG ")
    elif (key ==  3):
        if(qlsv.soluongsinhvien() > 0):
            print("\n3. XÓA SINH VIÊN")
            print("\nNhap ID:")
            id = int(input())
            if(qlsv.deleteById(id)):
                print("\n sinh vien co id = ",id,"da bi xoa")
            else:
                print("\n sinh vien co id",id,"khong ton tai")
        else:
            print("\nDanh sach sinh vien trong")
    elif(key == 4):
        if(qlsv.soluongsinhvien() > 0):
            print("\n4. TÌM KIẾM SINH VIÊN THEO TÊN ") 
            print("\nNhap ten de tim kiem")
            name = input()
            searchResult = qlsv.findName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong")
    elif(key == 5):
        if(qlsv.soluongsinhvien()>0):
            print("\n5. SẮP XẾP SINH VIÊN THEO ĐIỂM TRUNG BÌNH (GPA)")
            qlsv.sortBydiemTB()
            qlsv.showSinhVien(qlsv.getlistSinhVien())
        else:
            print("\nDanh sach sinh vien trong")
    elif(key == 6):
        if(qlsv.soluongsinhvien() > 0):
            print("\n6. SẮP XẾP SINH VIÊN THEO CHUYÊN NGÀNH")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getlistSinhVien())
        else:
            print("\n Danh sach sinh vien trong")
    elif(key == 7):
        if(qlsv.soluongsinhvien() > 0):
            print("\n7. HIẺN THỊ DANH SÁCH SINH VIÊN")
            qlsv.showSinhVien(qlsv.getlistSinhVien())
        else:
            print("\nDanh sach sinh vien trong")
    elif(key == 0):
        print("\nBẶN ĐÃ CHỌN THOÁT KHỎI CHƯƠNG TRÌNH")
        break
    else:
        print("\n KHÔNG CÓ CHỨC NĂNG NÀY")
        print("\nHÃY CHỌN CHỨC NĂNG TRONG TOP MENU")

