# https://atcoder.jp/contests/abc246/tasks/abc246_d
# a,bは10**6が上限
def f(a,b):
    return a**3 + (a**2)*b + a*(b**2) + b**3

n = int(input())


j = 10**6
x = 10**22 # 無限大の数
for i in range(10**6):
    while f(i, j)>=n and j>=0:
        x = min(x, f(i,j))
        j -= 1

print(x)
