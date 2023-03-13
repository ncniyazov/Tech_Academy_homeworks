s = input()
s1 = s[len(s)-1:0:-1]
cf = s.find(" ")
cl = len(s) - s1.find(" ")-1
if cf != -1:
    print(cf, cl)
else:
    print(-1)