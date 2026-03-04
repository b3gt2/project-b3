ho_ten = input("Nhập họ tên đầy đủ: ").strip()
ds = ho_ten.split()
ten = ds[-1]
ho_dem = " ".join(ds[:-1])
print("Tên:", ten)
print("Họ và tên đệm:", ho_dem)
