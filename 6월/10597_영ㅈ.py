# from collections import deque
import sys

# kri = list(sys.stdin.readline().strip())
# kri = deque(kri)

# result = []

# a = kri.popleft()
# while kri :
#     result.append(a)
#     a = kri.popleft()
#     while 1 :
#         if a not in result :
#             break
#         else :
#             if not kri :
#                 result.append(a)
#                 break
#             b = kri.popleft()
#             a = a+b


# print(result)

# 모든 조합

def makeIt(index, c):
    global finish, ans
    if finish: return

    if index==len(num):
        if c==maxN:
            finish = True
            ans = " ".join(map(str, tmp))
        return
    # 한자리 숫자나 두자리 숫자로 탐색
    
    num1 = int(num[index])
    if not used[num1]: 
        used[num1] = True
        tmp[c] = num1
        makeIt(index+1, c+1)
        used[num1] = False
    if index<len(num)-1: 
        num2 = int(num[index:index+2])
        if num2 < maxN+1 and not used[num2]:
            used[num2] = True
            tmp[c] = num2
            makeIt(index+2, c+1)
            used[num2] = False
            
num = sys.stdin.readline().strip()
if len(num)<10:
    maxN = len(num)
else:
    maxN = 9+(len(num)-9)//2 
    
used = [0 for _ in range(maxN+1)]
tmp = [0 for _ in range(maxN)]
finish = False
makeIt(0,0)
print(ans)