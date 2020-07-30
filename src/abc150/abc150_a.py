# https://atcoder.jp/contests/abc150/tasks/abc150_a

k, x = map(int, input().split())
res = 'Yes' if 500 * k >= x else 'No'
print(res)