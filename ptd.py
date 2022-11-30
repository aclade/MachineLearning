a = int(input())
b = int(input())
c = int(input())

a1 = min(a,b,c);
c1 = max(a,b,c);
if a == 0 or b == 0 or c == 0:
    print("a,b,c khong la day cap so nhan")
else:
    if a != a1 and a != c1:
        b1 = a
    elif b != a1 and b != c1:
        b1 = b
    else:
        b1 = c 

    if (c1/b1 == b1/a1):
        print("a,b,c la day cap so nhan")
    else :
        print("a,b,c khong la day cap so nhan")