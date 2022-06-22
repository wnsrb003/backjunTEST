import sys

stack = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
pop = []

for _ in range(n) :
    c = sys.stdin.readline()
    if c[0] == "L" and stack :
        pop.append(stack.pop())
    elif c[0] == "D" and pop :
        stack.append(pop.pop())
    elif c[0] == "B" and stack :
        stack.pop()
    elif c[0] == "P" :
        stack.append(c[2])
       
print(''.join(stack)+''.join(pop[::-1]))

# for _ in range(n) :
#     c = sys.stdin.readline()
#     if c[0] == "L" :
#         if curser > 0 : curser -= 1
#     elif c[0] == "D" :
#         if curser < len(line) : curser += 1
#     elif c[0] == "B" :
#         if curser > 0 :
#             del line[curser-1]
#             curser -= 1
#     else :
#         if curser == 0 : 
#             line.insert(0,c[2])
#         else : 
#             line.insert(curser,c[2])
#         curser += 1

# print(''.join(line))

