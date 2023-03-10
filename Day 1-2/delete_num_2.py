num = int(input())
qaliq = (num // 1000) * 1000
n = num % 1000
yuzluk = n // 100
onluq = n % 100 // 10
teklik = n % 10
print(qaliq + teklik * 100 + onluq * 10 + yuzluk)
