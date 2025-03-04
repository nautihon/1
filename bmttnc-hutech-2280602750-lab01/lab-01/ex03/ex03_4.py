def truy_cap_phan_tu(tuple_data):
    firt_element = tuple_data[0]
    last_element = tuple_data[-1]
    return firt_element, last_element

input_tuple = eval(input("nhập tuple ví dụ như (1,2,3): "))
firt,last = truy_cap_phan_tu(input_tuple)

print("phan tử đầu tiên là: ",firt)
print("phần tử cuối cùng là :",last)
    