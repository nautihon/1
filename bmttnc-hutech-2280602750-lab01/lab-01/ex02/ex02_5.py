so_gio_lam = float(input("Nhập số giờ làm: "))
luong_giơ = float(input("Nhập lương giờ: "))
gio_tieu_chuan = 44 
gio_vuot_chuan = max(0,so_gio_lam-gio_tieu_chuan)
thuc_linh = so_gio_lam * luong_giơ + gio_vuot_chuan * luong_giơ * 1.5
print(f"Lương thực lĩnh của nhân viên là: ", thuc_linh)