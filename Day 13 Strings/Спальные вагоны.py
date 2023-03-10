s = input()
max_sleeping = current_sleeping = 0

for i in s:
    if i == 'k':
        current_sleeping += 1
    else:
        
        max_sleeping = max(max_sleeping, current_sleeping)
        current_sleeping = 0

print(max(max_sleeping, current_sleeping))
