import sys
sys.stdin = open('input.txt')
N = int(input())
arr = list(map(int, list(input())))
print(arr)
print(sum(arr))
