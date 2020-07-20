import math

# 最大公約数
print(math.gcd(12312, 128))


# 最小公倍数
def lcm(a, b):
    return int(a * b/ math.gcd(a, b))
