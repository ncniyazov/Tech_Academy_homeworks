n = int(input())
tip = n + n*0.1
if tip % 1 > 0:
    tip = tip //1 +1
print(int(tip))