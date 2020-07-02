# https://atcoder.jp/contests/abc143/tasks/abc143_b
import itertools

n = int(input())
d = list(map(int, input().split()))
res = sum(map(lambda x: x[0] * x[1], itertools.combinations(d, 2)))
print(res)