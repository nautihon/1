def dao_nguoc_chuoi (chuoi):
    chuoi_dao_nguoc = chuoi[::-1]
    return chuoi_dao_nguoc  
input_string =input("nhap chuoi:")
print("chuoi dao nguoc la:",dao_nguoc_chuoi(input_string))
