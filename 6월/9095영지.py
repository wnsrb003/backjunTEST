import sys

t = int(sys.stdin.readline())
case = []
for _ in range(t) :
    n = int(sys.stdin.readline())
    case.append(n)
    # 1. DP로 풀기
    # 2. 디피 테이블 : n일때 경우의수 저장

m = max(case)
dp = [0]*(m+1)
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,m+1) :
    dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
    
for i in case :
    print(dp[i])