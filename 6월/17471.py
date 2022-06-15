from collections import defaultdict
import sys

n = int(sys.stdin.readline())
person = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for i in range(n) :
    a = list(map(int, sys.stdin.readline().split()))
    graph[i+1] = a[1:]

print(graph)

mini = 10000000000

def dfs1(index) :
    global mini
    visit[index] = 1
    temp = visit[:]
    if check(temp) :
        a ,b = 0,0
        for i in range(1,n+1) :
            if visit[i] == 0 : a += person[i-1]
            else : b += person[i-1]
        mini = min(mini,abs(a-b))
    # 검증 - 나머지 선거구가 전부 이어지는지 검증
    # 이어진다면 인구 차이 구하기

    for i in graph[index] :
        if visit[i] == 0 :
            dfs1(i)
            visit[i] = 0


def check(temp) :
    for i in range(1,n+1) :
        if temp[i] == 0 :
            dfs(i,temp)
            if 0 in temp : return False
            return True  
    return False

def dfs(v,seen):
    seen[v] = 1
    for i in graph[v] :
        if seen[i] == 0:
            dfs(i,seen)

for i in range(1,n+1) :
    # print(i)
    visit = [0] * (n+1)
    visit[0] = 1
    dfs1(i)

if mini == 10000000000 :
    print(-1)
else : print(mini)