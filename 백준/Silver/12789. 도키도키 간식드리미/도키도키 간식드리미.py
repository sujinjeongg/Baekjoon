import sys
input = sys.stdin.readline 

stack = [] # 대기열 

def solve(N, line):
    line = list(map(int, line))

    current = 1
    while line or stack:
        if line and current == line[0]:
            line.pop(0)
            current += 1
        elif stack and current == stack[-1]:
            stack.pop() 
            current += 1
        elif line:
            stack.append(line.pop(0))
        else:
            return "Sad"
      
    return "Nice"

N = int(input()) # 승환 앞의 학생 수
line = input().split() # 현재 줄 서 있는 번호표

print(solve(N, line))