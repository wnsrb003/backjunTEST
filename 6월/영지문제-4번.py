import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()
num = ""
sum = 0
for i in word :
    if i in ["0","1","2","3","4","5","6","7","8","9"] :
        num += i
    else :
        if num : 
            sum += int(num)
            num = ""          

if num : 
    sum += int(num)

print(sum)