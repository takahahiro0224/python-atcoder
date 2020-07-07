"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])

    if tmp != 1:
        arr.append([tmp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

print(factorization(50))


# 因数をlistで返す
def factorizationList(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1)) + 1):
        if tmp % i == 0:
            while tmp % i == 0:
                tmp //= i
                arr.append(i)

    if tmp != 1:
        arr.append(tmp)

    if arr == []:
        arr.append(n)

    return arr

print(factorizationList(50))

# alphabetを列挙
import string
ALPHABET = string.ascii_uppercase
print(ALPHABET) # ABCDEFGHIJKLMNOPQRSTUVWXYZ


# foldLeft
l = [1,2,3,4,5]
import functools
product_l = functools.reduce(lambda x, y: x * y, l, 1)
print(product_l) # 120
