import sys
input = sys.stdin.readline 

output = [] # 출력값 저장

def solve(s):
    while '()' in s or '[]' in s:
        if '()' in s:
            s = s.replace('()', '', 1)
        if '[]' in s:
            s = s.replace('[]', '', 1)

    if s:
        output.append("no")
    else:
        output.append("yes")

while True:
    s = input().rstrip('\n')
    if s == '.':
        break
    s = ''.join(c for c in s if c in '()[]')
    solve(s)

print('\n'.join(output))