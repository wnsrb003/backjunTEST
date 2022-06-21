begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def solution(begin, target, words):
    if target not in words :
        return 0
    count = 10000000000 
    def dfs (s,con,word) :
        nonlocal count
        if s == target :
            count = min(count,con)
            return
        for i in word :
            cnt = 0
            for j in range(len(s)) :
                if s[j] != word[i][j] : cnt += 1
                if cnt > 1 : break
            if cnt == 1 :
                l = word[:]
                del l[i]
                dfs(word[i],con+1,l)
    dfs(begin,0,words)
    return count
