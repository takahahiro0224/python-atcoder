# https://atcoder.jp/contests/abc142/tasks/abc142_c

n = int(input())
a = list(map(int, input().split()))
d = {}
for i, _a in enumerate(a):
    d[i+1] = _a

# return tuple
sortedNum = sorted(d.items(), key=lambda x:x[1])
print(*[s[0] for s in sortedNum])