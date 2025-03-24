n = int(input())
words = set()
for _ in range(n):
    line = input()
    words.update(line.split())
print(len(words))

