chuoi_so = input("Nhập các số cách nhau bởi dấu cách: ")

danh_sach_so = chuoi_so.split()

tong = 0
for so in danh_sach_so:
    tong += float(so)

print("Tổng các số đã nhập là:", tong)
