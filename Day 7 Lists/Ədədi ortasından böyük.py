n = abs(int(input()))
l = list(int(i) for i in input().split())
sum = 0
sum_ededi_orta = 0
count = 0

for i in l:
    sum += i
ededi_orta = sum // len(l)     
#print(ededi_orta)   
for j in l:
    if j > ededi_orta:
        sum_ededi_orta += j
        count += 1
print(sum_ededi_orta, count)
