def solution(s):
    answer = 0
    stack = [s[0]]
    
    for i in range(1,len(s)) :
        if stack and s[i] == stack[-1] :
            stack.pop()
        else : stack.append(s[i])
    
    if not stack : answer = 1
    return answer