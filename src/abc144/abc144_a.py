# https://atcoder.jp/contests/abc144/tasks/abc144_a

a, b = map(int, input().split())
res = a * b if (a < 10 and b < 10) else '-1'
print(res)