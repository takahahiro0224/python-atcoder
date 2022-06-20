"""
https://atcoder.jp/contests/abc242/tasks/abc242_a

"""

a, b, c, x = map(int, input().split())

if x <= a:
    score = 1
elif x > b:
    score = 0
else:
    score = c / (b-a)

print(score)
