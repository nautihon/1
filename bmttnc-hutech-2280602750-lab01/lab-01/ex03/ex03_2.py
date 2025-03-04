def dao_nguoc_list(list):
    return list[::-1]
input_list = input("nhập cd các số cách nhau bằng dấu phẩy:")
numbers = list(map(int,input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print(" list sau khi đảo ngược là :",list_dao_nguoc)