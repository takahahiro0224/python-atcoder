"""
C - 1111gal password
動的計画法
https://atcoder.jp/contests/abc242/tasks/abc242_c
pypyならOK, cpythonだとTLE
"""

N = int(input())
MOD = 998244353

d = [1]*11
d[0] = d[10] = 0

for i in range(N-1):
    e = d.copy()

    for x in range(1, 10):
        d[x] += e[x-1]
        d[x] += e[x+1]
        d[x] %= MOD

print(sum(d)%MOD)


