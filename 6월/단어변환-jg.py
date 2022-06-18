def solution(begin, target, words):
    def check(begin, words, arg_cnt):
        nonlocal min_cnt
        if begin == target:
            min_cnt = min(min_cnt, arg_cnt)
            return
        for j, w in enumerate(words):
            cnt = 0
            for i in range(len(w)):
                if cnt > 1:
                    break
                if w[i] != begin[i]:
                    cnt += 1
            if cnt == 1:
                arg_words = words[:]
                del arg_words[j]
                check(w, arg_words, arg_cnt+1)
    min_cnt = 10000000000000
    if not target in words:
        return 0
    check(begin, words, 0)
    if min_cnt == 10000000000000:
        return 0
    return min_cnt