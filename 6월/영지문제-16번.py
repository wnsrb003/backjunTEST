import sys

k,n = map(int,sys.stdin.readline().split())
lensun = []
for _ in range(k) :
    a = int(sys.stdin.readline())
    lensun.append(a)

start = 1
end = max(lensun)
result = 0
while start <= end : 
    count = 0
    mid = (start+end) // 2
    for i in lensun :
        while i >= mid :
            i = i - mid
            count += 1
            if count > n : break
        if count > n : break
    if count < n :
        end = mid - 1
    else :
        result = mid #최대니까
        start = mid + 1

print(result)