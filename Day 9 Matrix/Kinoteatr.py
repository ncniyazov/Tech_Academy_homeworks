places = [[0] * 1000 for i in range(1000)]
s1, s2, count = 1, 1, 0
n, m = (int(i) for i in input().split())
for i in range(n):
    for j in range(m):
        places[i][j] = s1
        s1 += 1

for j in range(m):
    for i in range(n):
        if places[i][j] == s2:
            count += 1
        s2 += 1
print(count)