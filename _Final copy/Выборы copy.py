n, k = (int(i) for i in input().split())
candidates = input().split(" ")
candidates_set = set(candidates)
result = "NO"
#print(set(candidates))
for i in candidates_set:
    #print(candidates.count(i), k)
    if candidates.count(i) > n/2:
        result = "YES"
        break
print(result)
