# https://atcoder.jp/contests/abc142/tasks/abc142_a

n = int(input())
oddCount = len(list(filter(lambda x: x % 2 == 1, range(1,n + 1))))
print(oddCount / n)