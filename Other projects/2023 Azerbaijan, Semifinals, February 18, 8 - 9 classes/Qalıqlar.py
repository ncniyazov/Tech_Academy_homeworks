n, m  = (int(i) for i in input().split())
divmod_sum = 0
for i in range(1, m+1):
    divmod_sum += n%i 
print(divmod_sum)