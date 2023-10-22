n = [int(s) for s in input().split()]
q = set()
for num in n:
    if num in q:
        print('YES')
    else:
        print('NO')
        q.add(num)