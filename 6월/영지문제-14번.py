
import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

card.sort()

def check(a):
    start = 0
    end = n-1
    while start <= end :
        mid = (start+end) // 2
        if a == card[mid] : return True
        elif a > card[mid] :
            start = mid+1
        else : 
            end = mid-1
    return False
    
for i in nums :
    if check(i) : print(1,end=' ')
    else :print(0,end= ' ')

