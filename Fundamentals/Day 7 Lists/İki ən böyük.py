n = abs(int(input()))
l = list(int(i) for i in input().split())
sum = 0
en_boyuk1 = max(l)
l.remove(max(l))
en_boyuk2 = max(l)
print(en_boyuk1 + en_boyuk2)
