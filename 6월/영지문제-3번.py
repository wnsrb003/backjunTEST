import sys

x = sys.stdin.readline().strip()
num = 0
if x[0] == '0' :
    if x[1] == 'x' :
        x = x[2:]
        x = x[-1::]
        num = int(x,16)
    else :
        num = int(x,8)
else : num = x 
print(num)
