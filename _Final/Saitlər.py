n = (input())
count = 0
saitler = ["A", "E", "I", "O", "U", "Y"]
for char in n:
    if char in saitler:
        count += 1
print(count)
