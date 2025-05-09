N = int(input())
    
def solution(N):
    output = []

    def recursion(N, start, end, via):
        if N==1:
            output.append((start, end))
            return
        recursion(N-1, start, via, end)
        output.append((start, end))
        recursion(N-1, via, end, start)

    recursion(N, 1, 3, 2)
    print(2**N - 1)
    for start, end in output:
        print(f"{start} {end}")

solution(N)
        