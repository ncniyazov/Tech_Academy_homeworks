s = str(abs(int(input())))
cem = 0
for i in range(0, len(s)):
    num = int(s[i])
    cem += num
print(cem)