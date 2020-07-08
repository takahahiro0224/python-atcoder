from typing import List
# bit全探索のサンプル

# bit全探索でn回試行した時のコインの表裏の全パターンを返す パターン数 2 ** n
def bit_search_coins(n: int) -> List:
    res_all = []
    for i in range(2 ** n):
        res = []
        for j in range(n):
            if ((i >> j) & 1):
                res.append('オモテ')
            else:
                res.append('ウラ')
        res_all.append(res)

    return res_all

print(bit_search_coins(3))
