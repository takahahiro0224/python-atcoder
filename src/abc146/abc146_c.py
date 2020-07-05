# https://atcoder.jp/contests/abc146/tasks/abc146_c

a, b, x = map(int, input().split())

def in_cost(num):
    return a * num + b * len(str(num)) <= x

# high - low = 1 になるまで探索、探索終了時のlowがコスト内で購入できる最大の整数となる
def bisect_search(low, high):
    while high - low > 1:
        mid = (high + low) // 2
        if in_cost(mid):
            low = mid
        else:
            high = mid
    return low

print(bisect_search(0, 10**9+1))

