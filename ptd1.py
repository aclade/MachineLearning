a = [int(x) for x in input().split()]

a.sort()
if a[0] == 0 or a[1] == 0 or a[2] == 0:
    print("a,b,c khong la day cap so nhan")
else:
    if (a[2]/a[1] == a[1] / a[0]) :
        print("a,b,c la day cap so nhan")
    else :
        print("a,b,c khong la day cap so nhan")