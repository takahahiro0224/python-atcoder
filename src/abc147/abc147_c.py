# https://atcoder.jp/contests/abc147/tasks/abc147_c
from typing import List, Tuple

# 参考回答
# https://atcoder.jp/contests/abc147/submissions/14837598
# そんなにわかってない



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
    if cnt <= ans: continue
    for j in range(len(infos)):
        # 1を左シフト
        if i & (1 << j):
            for x, y in infos[j]:
                if y == 1 and i % (1 << x-1): continue
                if y == 0 and i % (1 << x-1) == 0: continue
                break
            else:
                continue
            break
    else:
        ans = cnt

print(ans)

