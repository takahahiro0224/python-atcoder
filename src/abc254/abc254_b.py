# https://atcoder.jp/contests/abc254/tasks/abc254_b

n = int(input())

n_array = []

def calc_particle(i, j) -> int:
    if (j == 0) or (i == j):
        return 1
    else:
        return n_array[i-1][j-1] + n_array[i-1][j]

for i in range(n):
    this_array = []
    for j in range(i+1):
        this_array.append(calc_particle(i, j))
    n_array.append(this_array)
    print(*this_array)


    
