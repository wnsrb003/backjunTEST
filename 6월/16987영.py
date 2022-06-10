import sys

n = int(sys.stdin.readline())
eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

maxi = 0
def hit(index) :
    global maxi,n
    if index == n :
        print(eggs)
        count = 0
        for i in eggs :
            if i[0] <= 0 :
                count+=1 
        maxi = max(maxi,count)
        return
    
    if eggs[index][0] <= 0 : 
        hit(index+1)
        return 
    
    

    for i in range(n) :
        if i == index : continue
        if eggs[i][0] <= 0 : continue
        
        eggs[index][0] -= eggs[i][1] 
        eggs[i][0] -= eggs[index][1]
        print(eggs)
        hit(index+1)
        eggs[index][0] += eggs[i][1] 
        eggs[i][0] += eggs[index][1]

hit(0)
print(maxi)
