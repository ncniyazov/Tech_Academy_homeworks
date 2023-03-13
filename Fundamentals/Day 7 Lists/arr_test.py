n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if i % 2 == 0:
        arr.remove(i)
print(arr)