# https://atcoder.jp/contests/abc139/tasks/abc139_c
'''
計算量に余裕があるので愚直に全探索で良い
(一度見た部分はスキップすれば良い)
'''

n = int(input())
H = list(map(int, input().split()))

c = 0
max_c = 0
for i in range(n - 1):
   if H[i] >= H[i+1]:
      c += 1
   else:
      c = 0
   if c > max_c:
      max_c = c

print(max_c)
