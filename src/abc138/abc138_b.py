# https://atcoder.jp/contests/abc138/tasks/abc138_b

n = int(input())
a = list(map(int, input().split()))
res = 1 / sum(map(lambda x: 1 / x, a))
print(res)