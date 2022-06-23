import sys

string = list(sys.stdin.readline().strip())
d = sys.stdin.readline().strip()
stack = []
result = []

# 뒷글자만 확인하면 계속 재확인할필요옶음
for s in string :
    stack.append(s)
    if s == d[-1] and ''.join(stack[-len(d):]) == d :
        del stack[-len(d):]

if not stack :
    print("FRULA")
else : print(''.join(stack))