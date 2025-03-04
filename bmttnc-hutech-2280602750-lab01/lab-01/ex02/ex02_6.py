input_str = input("nhap x,y:")
dimensions = [int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
comNum=dimensions[1]
multilist = [[0 for col in range(comNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(comNum):
        multilist[row][col]= row*col
print(multilist)