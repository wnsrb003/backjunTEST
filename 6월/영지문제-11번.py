import sys

n,k = map(int,sys.stdin.readline().split())

string = []
for _ in range(n) :
    a = sys.stdin.readline()
    string.append(a[4:len(a)-5])

if k < 5 :
    print(0)
    exit(0)
elif k == 26 :
    print(n)
    exit(0)

learn = [0] * 26

# for i in ('a','c','i','n','t') :
#     learn[ord(i)-ord('a')] = 1

for i in range(len(string)) :
    string[i] = string[i].strip('a''c''i''n''t')

ans = 0
def dfs(idx, cnt) : 
    global ans

    if cnt == k - 5 :
        readcnt = 0
        for s in string :
            check = True
            for j in s :
                if not learn[ord(j)-ord('a')] :
                    check = False
                    break
            if check : readcnt += 1
        ans = max(ans,readcnt)
        return

    for i in range(idx,26) :
        if not learn[i] :
            learn[i] = True
            dfs(i,cnt+1)
            learn[i] = False

dfs(0,0)
print(ans)