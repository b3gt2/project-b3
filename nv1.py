n = int(input("Nhập số học sinh trong lớp: "))

ds_lop = []

for i in range(n):
    hoten = input("Nhập họ tên học sinh thứ " + str(i+1) + ": ")
    ds_lop.append(hoten)

print("Danh sách lớp học:")
for i in range(n):
    print(ds_lop[i])
