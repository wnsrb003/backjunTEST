from collections import defaultdict

def solution(n, computers):
    answer = 0

    visit = [0] * n
    def dfs (m) :
        visit[m] = 1
        for i in range(n) :
            if computers[m][i] == 1 and visit[i] == 0 :
                visit[i] = 1
                dfs(i)

    answer = 0 
    for i in range(n) :
        if visit[i] == 0 :
            dfs(i)
            answer += 1


    return answer