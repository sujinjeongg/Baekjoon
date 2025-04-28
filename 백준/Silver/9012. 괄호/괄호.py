import sys
input = sys.stdin.readline

T = int(input())
    
output = [] # 출력값 저장

def yes_or_no(s):
    while '()' in s:
        s = s.replace('()', '', 1)
    
    # '()' 모두 지우고 다른게 남아있다면 NO, 안 남아있으면 YES
    if s: 
        output.append("NO")
    else:
        output.append("YES")
                           
for _ in range(T):
    s = input().strip()
    yes_or_no(s)
        
print('\n'.join(output))