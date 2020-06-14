# https://atcoder.jp/contests/abc137/tasks/abc137_b

k, x = map(int, input().split())
MAX = 1000000
MIN = -1000000
res = list(range(max(x-k+1, MIN), x)) + list(range(x, min(x+k, MAX)))
print(*res)