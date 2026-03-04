n = int(input("Nhập số học sinh trong lớp: "))

ten = []
hodem = []

for i in range(n):
    s = input("Nhập họ tên học sinh thứ " + str(i+1) + ": ")
    sline = s.split()
  m = len(sline)-1
    ten.append(sline[m])                  
  del sline[m]
hodem.append(" ".join(sline))  
print("Danh sách học sinh:")
for i in range(n):
    print(ten[i],hodem[i])
