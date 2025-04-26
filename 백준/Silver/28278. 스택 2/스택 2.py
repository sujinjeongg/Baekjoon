from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
    
s = deque() # 스택
output = [] # 출력 값 저장

def solve(num):
    if num[0] == '1':
        x = int(num[1])
        s.append(x)
    elif num[0] == '2':
        if s:
            output.append(s.pop())
        else:
            output.append(-1)
    elif num[0] == '3':
        output.append(len(s))
    elif num[0] == '4':
        if s:
            output.append(0)
        else:
            output.append(1)
    elif num[0] == '5':
        if s:        
            output.append(s[-1])
        else:
            output.append(-1)
    
for _ in range(N):
    num = input().split()
    solve(num)

print('\n'.join(map(str, output)))