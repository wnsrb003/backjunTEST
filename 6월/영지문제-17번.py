import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

#이분탐색
#이분탐색으로 어떻게 풀어ㅡㅡ 인덱스 ??? 아님 값 ???? 
# 값으로 하면 내 앞에 얼마만큼에 인덱스가 소요됐는지 어떻게 알지 ??? 
start = 1
end = n*n

# 배열안에 들어갈수있는 수를 이분탐색으로 구해서 해당 수가 몇번째 인덱스인지 확인한다.
# 인덱스의 수가 k와 같은지 확인

# 인덱스를 구하느 규칙 
while start <= end :
    mid = (start+end) // 2
    count = 0
    for i in range(1,n+1) : # i행에 나(mid)보다 작거나 같은 수의 개수 == 인덱스의 수
        count += min(mid//i,n) #n보다 클수도있으니까
    if count < k :
        start = mid + 1
    else :
        end = mid - 1
        
print(start)