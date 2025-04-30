import sys
input = sys.stdin.readline 
from collections import deque

q = deque()
output = [] # 출력 값 저장

def solve(order):
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        if q: output.append(q.popleft())
        else: output.append(-1)
    elif order[0] == 'size':
        output.append(len(q))
    elif order[0] == 'empty':
        if not q: output.append(1)
        else: output.append(0)
    elif order[0] == 'front':
        if q: output.append(q[0])
        else: output.append(-1)
    elif order[0] == 'back':
        if q: output.append(q[-1])
        else: output.append(-1)

N = int(input())

for _ in range(N):
    order = input().split()
    solve(order)

print('\n'.join(map(str, output)))