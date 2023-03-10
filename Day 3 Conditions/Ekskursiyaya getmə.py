n, m, k = (int(i) for i in input().split())
say_O = n % k
say_Q = m % k
if say_O == 0:
    o = n / k
else:
    o = n // k + 1
    
if say_Q == 0:
    q = m / k
else:
    q = m // k + 1
print(int(o+q))