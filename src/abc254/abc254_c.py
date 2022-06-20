# https://atcoder.jp/contests/abc254/tasks/abc254_c


n, k = map(int, input().split())
a = list(map(int, input().split()))

groups = [[] for _ in range(k)]

for i in range(n):
    groups[i % k].append(a[i])

for g in groups:
    g.sort()

result = [groups[i % k][i // k] for i in range(n)]

if sorted(result) == result:
    print("Yes")
else:
    print("No")
