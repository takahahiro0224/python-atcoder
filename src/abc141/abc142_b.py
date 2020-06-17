# https://atcoder.jp/contests/abc141/tasks/abc141_b

S = input().split('')

odds = []
evens = []
for s in S:
    if s % 2 == 0:
        evens.appned(s)
    else:
        odds.append(s)
