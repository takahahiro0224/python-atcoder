# https://atcoder.jp/contests/abc147/tasks/abc147_c
from typing import List, Tuple


'''
証言が以下の時
[[(2, 1), (3, 0)], [(3, 1), (1, 0)], [(1, 1), (2, 0)]]
1: 2は正直、3は不親切  
2: 1は不親切、3は正直   
3: 1は正直、2は不親切  この場合正直者は0人
Xiの人が正直者と仮定して、 他の証言と照らし合わせる

'''


def io_readline() -> List[List[Tuple[int, ...]]]:
    N = int(input())
    res = []
    for n in range(N):
        a_n = int(input())
        n_testimony = []
        for _ in range(a_n):
            testimony = tuple(map(int, input().split()))
            n_testimony.append(testimony)
        res.append(n_testimony)
    return res


infos = io_readline()
ans = 0
for i in range(2 ** len(infos)):
    cnt = bin(i).count("1")
    if cnt <= ans:
        continue

    for j in range(2 ** len(infos)):
        if i & (1 << j):

# 続きは後で



