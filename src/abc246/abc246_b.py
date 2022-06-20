# https://atcoder.jp/contests/abc246/tasks/abc246_b
a, b = map(int, input().split())

import math
d = math.sqrt(a*a + b*b)
print(a/d, b/d)
