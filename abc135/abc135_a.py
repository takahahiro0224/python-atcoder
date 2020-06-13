# https://atcoder.jp/contests/abc135/tasks/abc135_a

a, b = map(int, input().split())
if abs(a-b) % 2 != 0:
    print("IMPOSSIBLE")
else:
    print(min(a,b) + abs(a-b) // 2)
