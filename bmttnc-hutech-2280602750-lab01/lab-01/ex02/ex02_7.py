print("nhập các dòng văn vản (nhap 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line == "done":
        break
    lines.append(line)
print("\n các dòng đã nhập sau khi chuyển thành chữ in hoa :")
for line in lines:
    print(line.upper())