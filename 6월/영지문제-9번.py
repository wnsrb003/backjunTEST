import sys

n = sys.stdin.readline().strip()

c = 9*len(n)

for i in range(c,len(n)-1,-1) :
    a = int(n) - i 
    if a >= 0 :
        sum = 0
        for j in str(a) :
            sum += int(j)
        if sum == i :
            print(a)
            exit(0)
print(0)
