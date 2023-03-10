n = abs(int(input()))
cem = 0
str_n = str(n)
for item in range(len(str_n)):
    num = int(str_n[item])
    #print(num)
    if num %2 != 0:
        #print(num, cem)
        cem += 1
print(cem)