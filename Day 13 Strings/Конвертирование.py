s = input().strip()
i, j = (int(i) for i in input().split())
cut_rev = s[i - 1:j][::-1]
start = s[:i-1]
end = s[j:]
print(start + cut_rev + end)
