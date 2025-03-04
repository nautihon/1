def ting_tong_so_chan(list):
 tong =0 
 for num in list:
    if num % 2 == 0:
        tong += num
 return tong
input_list =input("nhap danh sach cac so, cach nhau bang dau phay:")
numbers = list(map(int ,input_list.split(',')))

tong_chan = ting_tong_so_chan(numbers)
print("tong cac so chan trong list la:",tong_chan)