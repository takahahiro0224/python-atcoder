# https://atcoder.jp/contests/abc150/tasks/abc150_b

n = int(input())
s = input()
cnt = s.replace('ABC', 'a').count('a')
print(cnt)