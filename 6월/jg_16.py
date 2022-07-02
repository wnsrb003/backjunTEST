import heapq
from collections import deque
q = []
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
for x, y in people:
    heapq.heappush(q, [y, x])
result = deque([])
for _ in range(len(people)):
    y, x = heapq.heappop(q)
    if not result:
        result.append([x,y])
        continue
    if not y:
        for i in range(len(result)):
            if result[i][0] > x:
                result.insert(i, [x,y])
                break
            if i == len(result) - 1:
                result.append([x,y])
    else:
        cnt = 0
        for i in range(len(result)):
            if cnt > y:
                result.insert(i, [x,y])
                break
            if i == len(result) - 1:
                result.append([x,y])
            cnt+=1
print(result)