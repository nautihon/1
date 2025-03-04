def dem_so_lan_xuat_hien(list):
    count_dict = {}
    for item in list :
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("nhập ds các từ , cách nhau bằng dấu cách:")
word_list = input_string.split()

so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("số lần xuất hiện của các phần tử :",so_lan_xuat_hien)