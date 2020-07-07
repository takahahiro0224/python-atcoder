# https://atcoder.jp/contests/abc138/tasks/abc138_c
'''
入力されたリストを昇順にソートし、左から畳み込む処理をすれば良い
'''
import functools

n = int(input())
V = sorted(map(int, input().split()))
# foldleftと同じ
ans = functools.reduce(lambda x, y: (x + y) / 2, V)
print(ans)


