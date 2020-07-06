# https://atcoder.jp/contests/abc137/tasks/abc137_c

'''
与えられた文字列をソートしたリストを作成する、
同じの文字の数から2つ選ぶ組合せの数を合計すれば良い。
計算量の都合でcounterやitertools.combinationsは使えないので
このような実装になる。
'''

n = int(input())
S = [''.join(sorted(input())) for _ in range(n)]
cnt = 0
dic = {}
for s in S:
    if s in dic.keys():
        cnt += dic[s]
        dic[s] += 1
    else:
        dic[s] = 1
print(cnt)