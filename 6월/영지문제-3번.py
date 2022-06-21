import sys

x = sys.stdin.readline().strip()
num = 0
if x[0] == '0' :
    if x[1] == 'x' :
        num = int(x,16)
    else :
        num = int(x,8)
else : num = x 
print(num)
