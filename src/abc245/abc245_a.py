a, b, c, d = map(int, input().split())


takahasi = a * 3600 + b * 60
aoki = c * 3600 + d * 60 + 1

if takahasi < aoki:
    print("Takahasi")
else:
    print("Aoki")


