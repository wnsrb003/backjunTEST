from collections import deque
def solution(s):
    def is_(brakets):
        stack = list()
        for braket in brakets:
            if braket == '[' or braket == '(' or braket == '{':
                stack.append(braket)

            else:
                if not stack:
                    return False

                if braket == ']' and stack[-1] == '[':
                    stack.pop()

                elif braket == ')' and stack[-1] == '(':
                    stack.pop()

                elif braket == '}' and stack[-1] == '{':
                    stack.pop()

        if not stack:
            return True
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        s.append(s.popleft())
        if is_(s):
            answer += 1
    return (answer)
