n = int(input())
votes = {}

for _ in range(n):
    parts = input().split()
    i = 0
    while i < len(parts):
        candidate = parts[i]
        count = int(parts[i + 1])
        votes[candidate] = votes.get(candidate, 0) + count
        i += 2

for candidate in sorted(votes):
    print(f"{candidate} {votes[candidate]}")