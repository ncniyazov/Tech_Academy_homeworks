n = int(input())

herb = 0
eagle = 0

for i in range(n):
    monet = int(input())
    if monet == 1:
        eagle += 1
    else:
        herb += 1
print(min(herb, eagle))