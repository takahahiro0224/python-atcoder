# https://atcoder.jp/contests/abc145/tasks/abc145_c

import itertools

'''
Example:
    n = 3
    p = [(0, 0), (1, 0), (0, 1)] 座標
    routes = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]　経路順の組み合わせ
'''

n = int(input())
p = [tuple(map(int, input().split())) for n_ in range(n)]
routes = [i for i in itertools.permutations(range(0,n), n)]
distances = 0
for route in routes:
    for i in range(len(route)-1):
        distances += ((p[route[i]][0] - p[route[i+1]][0])**2 + (p[route[i]][1] - p[route[i+1]][1])**2) ** 0.5

print(distances / len(routes))