# https://atcoder.jp/contests/abc142/tasks/abc142_b

n, k = map(int, input().split())
h = list(map(int, input().split()))
res = len(list(filter(lambda x: x >= k, h)))
print(res)