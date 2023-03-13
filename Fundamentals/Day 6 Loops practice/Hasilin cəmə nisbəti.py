n = abs(int(input()))
cem = 0
hasil = 1
for item in range(len(str(n))):
    num = int(str(n)[item])
    #print(num)
    cem += num
    hasil *= num
print('%.3f' % (hasil/cem))