n, k = (int(i) for i in input().split())
candidates = input().split(" ")
result = "NO"
for i in candidates:
    print(candidates.count(i), k)
    if candidates.count(i) > n/2:
        result = "YES"
        break
print(result)
