# https://atcoder.jp/contests/abc144/tasks/abc144_b

n = int(input())
ansSet = set(x * y for x in range(1, 10) for y in range(1, 10))
res = 'Yes' if n in ansSet else 'No'
print(res)
