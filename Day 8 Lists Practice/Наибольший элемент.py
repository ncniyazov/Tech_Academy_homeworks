n = abs(int(input()))
l = list(int(i) for i in input().split())

print(max(l), l.index(max(l))+1)