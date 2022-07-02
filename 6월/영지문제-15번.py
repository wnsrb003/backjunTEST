import sys

n,m = map(int,sys.stdin.readline().split())
time = list(map(int,sys.stdin.readline().split()))

start = max(time)
end = sum(time) # 최대 크기
result = 0
while start <= end :
    mid = (start+end)//2
    count = 1
    sum = time[0]
    for i in range(1,n):
        if mid < sum + time[i] :
            sum = time[i]
            count += 1
        else : sum += time[i]
    if count > m :
        start = mid +1
    else : 
        result = mid
        end = mid - 1
        
print(result)