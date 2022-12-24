# My first time coding a competitive programming lesson with Python
# Coding by ptd
def dequy(n,m,dong,cot,total):
    if (dong >= n) :
        return total
    total += m[dong][cot]
    return max(dequy(n,m,dong+1,cot,total),dequy(n,m,dong+1,cot+1,total))

def main():
    m = []
    n = int(input())
    for i in range(n):
        m.append([int(x) for x in input().split()])
    print(dequy(n,m,0,0,0))

if __name__ == '__main__':
    main()
    