count = 0
s = input().strip()
for i in range(1, len(s)):
    if s[i] == '+' or s[i] == '*' or s[i] == '-':
        count += 1
print(count)
