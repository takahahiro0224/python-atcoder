# https://atcoder.jp/contests/abc143/tasks/abc143_a
a, b = map(int, input().split())
res = a-2*b if (a-2*b >= 0) else 0
print(res)