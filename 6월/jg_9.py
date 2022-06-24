import sys
sys.stdin = open('input.txt')

num = int(input())
result = 0
for i in range(num):
    n = i + sum(map(int, list(str(i))))
    if n == num:
        result = i
        break

print(result)