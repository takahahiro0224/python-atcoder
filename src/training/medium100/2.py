# https://atcoder.jp/contests/agc029/tasks/agc029_a

s = input()
# c = 0
# def exec(s, c):
#     n = len(s)
#     for i in range(n-1):
#         if s[i] == 'B' and s[i+1] == 'W':
#             s[i], s[i+1] = s[i+1], s[i]
#             c += 1
#             print(s)
#     return (s,c)

# c_diff = 100
# for _ in range(10*10):
    
#     c_old = c
#     s, c = exec(s, c)
#     if c - c_old == 0:
#         break

# print(c)
first_sum = 0
for i in range(s):
    if i == 'B':
        first_sum += i

