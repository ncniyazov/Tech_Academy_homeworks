n = int(input())
interesting_list = list(int(i) for i in input().split())
finaly_list = []
for i in interesting_list:
    if i not in finaly_list:
        finaly_list.append(i)
    else:
        finaly_list.remove(i)
print(len(finaly_list))
