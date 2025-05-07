def solution(N):
    length = int(3**N)

    s = ['-'] * length

    def recursion(start, length, s):
        mid = length // 3

        if length == 1:
            return 
        
        for i in range(start + mid, start + mid*2):
            s[i] = ' '

        recursion(start, mid, s) # 3등분의 왼쪽
        recursion(start + mid*2, mid, s) # 3등분의 오른쪽 

    recursion(0, length, s)

    return ''.join(s) 

output = []
try:
    while True:
        N = input()
        if N == '':
            break 
        output.append(solution(int(N)))
except EOFError:
    pass

print('\n'.join(output))