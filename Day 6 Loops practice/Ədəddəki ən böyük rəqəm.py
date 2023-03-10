n = abs(int(input()))
reqemler = []
str_n = str(n)
for item in range(len(str_n)):
    num = int(str_n[item])
    reqemler.append(num)
    
print(max(reqemler))