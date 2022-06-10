import sys

INF = sys.maxsize

# 모든 경우의 수에 대한 거리 구하기. 치킨 집이 올수있는 모든 조합  
#  
n,m = map(int,sys.stdin.readline().split())
graph = [[INF]*n for _ in range(n)]

# 그래프 저장
for i in range(m) :
    a,b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
for i in range (n) :
    graph[i][i] = 0


# 플로이드 위셜 - 모든 경로에서 최단거리 
for k in range(0, n):
    for a in range(0, n):
        for b in range(0,n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)
#모든 경우에 따른 왕복 거리..브루트포스
result = [0]*n
mini = INF
for i in range(n) :
    for j in range(n) :
        for k in range(n) :
            result[k] = min(graph[i][k],graph[j][k])
        # print(result)
        if mini > sum(result) :
            mini = sum(result)
            a,b = i,j

print(a+1,b+1,mini*2)