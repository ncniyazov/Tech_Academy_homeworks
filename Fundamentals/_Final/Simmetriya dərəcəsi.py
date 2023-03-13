n = input()
count = 0
for i in range(0, len(n)//2):
    if n[i] == n[-(i + 1)]:
        count += 1
if len(n) % 2 != 0:
    count += 1
print(count)