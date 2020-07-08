# https://atcoder.jp/contests/abc143/tasks/abc143_c

n = int(input())
S = input()
beforeChara = ""
cnt = 0
for s in S:
    if s != beforeChara:
        cnt += 1
    beforeChara = s
print(cnt)
