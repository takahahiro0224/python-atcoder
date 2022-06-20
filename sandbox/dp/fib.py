"""
ref: https://www.momoyama-usagi.com/entry/info-algo-dp
動的計画法によるフィナボッチ数列の計算
"""

def fib(n):
    a = [1] * (n+1) # a[0] = 1, a[1] = 1

    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]
