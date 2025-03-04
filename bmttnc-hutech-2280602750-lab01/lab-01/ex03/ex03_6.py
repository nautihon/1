def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return
    else:
        return False

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
Key_to_delete = 'b'
result = xoa_phan_tu(my_dict,Key_to_delete)
if result:
    print("phần tử được xóa từ dictionary:",my_dict)
else:
    print("không tìm thấy phần tủ cần xóa trong Dictionary .")