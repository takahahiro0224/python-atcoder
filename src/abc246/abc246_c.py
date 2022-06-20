# https://atcoder.jp/contests/abc246/tasks/abc246_c

n, k, x = map(int, input().split())
a_itr = map(int, input().split())
a_list = sorted(a_itr, reverse=True)
k_count = k
for i in range(n):
    if k_count < 1:
        break
    if a_list[i] < x:
        break
    c = min(a_list[i] // x, k_count)
    a_list[i] = a_list[i] - c * x
    k_count -= c


a_list = sorted(a_list, reverse=True)
for i in range(n):
    if k_count < 1:
        break
    a_list[i] = 0
    k_count -= 1
print(sum(a_list))


