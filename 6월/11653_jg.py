import sys
# sys.stdin = open('input.txt')

N = int(input())
# N = 9991
result = []
while(N>1):
    for i in range(2, N+1):
        if N % i == 0:
            result.append(i)
            N = N // i
            break
print('\n'.join(list(map(str,result))))