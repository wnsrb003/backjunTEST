def solution(str1, str2):
    answer = 0
    s1, s2 = [], []
    for s in range(len(str1)-1):
        if str1[s].isalpha() and str1[s+1].isalpha():
            s1.append((str1[s] + str1[s+1]).upper())
    for s in range(len(str2)-1):
        if str2[s].isalpha() and str2[s+1].isalpha():
            s2.append((str2[s] + str2[s+1]).upper())
    
    union = list(set(s1) | set(s2))
    intersection = list(set(s1) & set(s2))
    u_len = len(union)
    i_len = len(intersection)
    for u in union:
        if s1.count(u) > 1 or s2.count(u) > 1:
            u_len += max(s1.count(u), s2.count(u)) - 1
    for i in intersection:
        if s1.count(i) > 1 or s2.count(i) > 1:
            i_len += min(s1.count(i), s2.count(i)) - 1
    # print(union, intersection)
    if u_len != 0:
        answer = int((i_len / u_len) * 65536)
    else:
        answer = 65536
    print(answer)
            
    # print(union, intersection)
solution('E=M*C^2', 'e=m*c^2');