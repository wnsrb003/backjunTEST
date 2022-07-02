import sys
sys.stdin = open('input.txt')

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
finds = list(map(int, input().split()))
cards.sort()

def find(num):
    left, right = 0, len(cards)-1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == num:
            return 1
        elif cards[mid] < num:
            left = mid + 1
        elif cards[mid] > num:
            right = mid - 1
    return 0

result = []
for f in finds:
    result.append(find(f))
print(*result)