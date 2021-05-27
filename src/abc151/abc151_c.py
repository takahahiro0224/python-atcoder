# https://atcoder.jp/contests/abc151/tasks/abc151_c

n, m = map(int, input().split())
wa = [0 for i in range(100005)]
ac = [False for i in range(100005)]
for _ in range(m):
	p, s = input().split()
	p = int(p)
	if s == "WA":
		if not ac[p]:
			wa[p] += 1
	else:
		ac[p] = True

w = 0
c = 0
for i in range(n+5):
	if ac[i]:
		w += wa[i]
		c += 1
print(c, w)

