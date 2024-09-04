n = int(input())

names = set()
for i in range(n):
    name, state = input().split()
    if state == "enter":
        names.add(name)
    elif state == "leave":
        names.remove(name)
    
sorted_names = sorted(names, reverse=True)
    
for name in sorted_names:
    print(name)