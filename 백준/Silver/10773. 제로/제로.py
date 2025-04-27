from collections import deque

K = int(input())
    
s = deque()
    
def solve(num):
    if num[0] != '0':
        s.append(int(num[0]))
    else:
        s.pop()
            
for _ in range(K):
    num = input().split()
    solve(num)
        
print(sum(s))      