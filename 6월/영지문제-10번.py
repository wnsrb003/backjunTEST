import sys

n,m = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))

card.sort()

maxi = 0
for i in range(n) :
    for j in range(i+1,n) :
        #if card[i] + card[j] >= m : break
        for z in range(j+1,n) :
            if card[i] + card[j] + card[z] > m : break
            maxi = max(maxi,card[i] + card[j] + card[z])

print(maxi)