
import sys

kri = sys.stdin.readline().strip()

if len(kri) < 10 :
    n = len(kri)
else :
    n = (len(kri) - 9)//2 + 9

print(n)

visited = [0 for _ in range(n+1)]
result = [0 for _ in range(n)]

def dfs(index,c) :
    global ans
    if index==len(kri):
        if c==n:
            ans = " ".join(map(str, result))
            print(ans)
            exit(0)
        return

    
    num1 = int(kri[index])
    if not visited[num1]: 
        visited[num1] = True
        result[c] = num1
        dfs(index+1, c+1)
        visited[num1] = False
    if index<len(kri)-1: 
        num2 = int(kri[index:index+2])
        if num2 < n+1 and not visited[num2]:
            visited[num2] = True
            result[c] = num2
            dfs(index+2, c+1)
            visited[num2] = False
dfs(0,0)




    # if visited[int(kri[i])] == 0 :
    #     result.append(kri[i])
    #     visited[int(kri[i])] = 1
    #     dfs(i+1)
    #     result.pop()
    #     visited[int(kri[i])] = 0
    
    # if visited[int(kri[i]+kri[i+1])] == 0 :
    #     result.append(kri[i])
    #     visited[int(kri[i]+kri[i+1])] = 1
    #     dfs(i+2)
    #     result.pop()
    #     visited[int(kri[i]+kri[i+1])] = 0

## 하나로 쪼개는 경우 두개로 쪼개는 경우?