# https://atcoder.jp/contests/abc139/tasks/abc139_b

a, b = map(int, input().split())
if b == 1:
    print(0)
    exit(0)
for i in range(10000):
    if a + i * a - i >= b:
        print(1 + i)
        break

