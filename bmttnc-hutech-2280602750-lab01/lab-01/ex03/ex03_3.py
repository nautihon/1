def tao_tuple_tu_list(list):
    return tuple(list)
input_list = input("nhập ds các số cách nhau bởi đấu phẩy:")
number = list(map(int,input_list.split(',')))

my_tuple = tao_tuple_tu_list(number)
print("list :",number)
print("tuple từ list :",my_tuple)