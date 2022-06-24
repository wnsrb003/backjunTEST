import sys
sys.stdin = open('input.txt')

N = sys.stdin.readline().strip()
bomb = list(sys.stdin.readline().strip())
length = len(bomb)
stack = []
for n in range(len(N)):
    stack.append(N[n])
    if not stack or len(stack) < length:
        continue
    while stack and stack[-1] == bomb[-1]:
        i = len(stack) - length
        if stack[i:i+length] == list(bomb):
            for _ in range(length):
                stack.pop()
        else:
            break

print(''.join(stack) if stack else 'FRULA')
    
