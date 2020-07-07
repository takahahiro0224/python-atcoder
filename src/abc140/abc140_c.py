# https://atcoder.jp/contests/abc140/tasks/abc140_c

'''
n = 3
B1, B2 = 2, 5
の場合

B1 = 2 より　A1 =< 2, A2 =< 2 であるから、　A1 = 2
B2 = 5 だが 上より A2 <= 2であるから A2 = 2 , よってA3 = 5

----------------------------------------

n = 6
B1, B2, B3, B4, B5, B6 = 0, 153, 10, 10, 23
の場合

B1 = 0 より A1 =< 0, A1 =< 0 であるから A1 = 0
B2 = 153 より A2,A3 <= 153 上から A2 = 0
B3 = 10 より A3,A4 <= 10,   上と合わせて A3 = 10
B4 = 10より A4,A5 <= 10, 上と合わせて A4 = 10
B5 = 23より 以下省略　..  A5 = 10, A6 = 23
'''

n = int(input())
B = list(map(int, input().split()))
cnt = 0
for i in range(len(B)):
    if i == 0:
       cnt += B[i]
    else:
        cnt += min(B[i-1], B[i])
# 最後にAnの要素を追加
cnt += B[len(B) - 1]
print(cnt)
