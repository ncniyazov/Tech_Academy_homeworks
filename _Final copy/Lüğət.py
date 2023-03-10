n = abs(int(input()))
vocabulary = []
for i in range(n):
    vocabulary.append(input())
vocabulary.sort()  
for word in vocabulary:
    print(word)