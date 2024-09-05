N, M = map(int,input().split())

nonheards = set(input().strip() for _ in range(N))
nonseens = set(input().strip() for _ in range(M))

nonheardseens = sorted(nonheards & nonseens)

print(len(nonheardseens))
print("\n".join(nonheardseens))