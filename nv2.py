S = input("Nhập xâu kí tự bất kì: ")
kq = False

for k in range(len(S) - 1):
    if S[k] == "1" and S[k+1] == "0":
        kq = True
        break

if kq:
    print("Xâu có chứa '10'")
else:
    print("Xâu không chứa '10'")
