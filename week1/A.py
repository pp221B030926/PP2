n = int(input())
l = list()
d = dict()

for i in range(n):
    l += input().split()
letters = 0
words = 0
symbols = 0
for i in l:
    words += 1
    for j in i:
        if (j >= 'a' and j <= 'z') or (j >= 'A' and j <= 'Z'):
            letters += 1
        else:
            symbols += 1
print("File contains:")
print(letters, "letters")
print(words, "words")
print(symbols, "symbols")