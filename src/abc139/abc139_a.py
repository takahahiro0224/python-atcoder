# https://atcoder.jp/contests/abc139/tasks/abc139_a
s = input()
t = input()
res = list(map(lambda x: x[0] == x[1], zip(s, t)))
print(res.count(True))

