# https://atcoder.jp/contests/abc147/tasks/abc147_b
'''
入力文字列とそれを逆順にしたものをそれぞれ等しいか判定し、
違っていた数/2 をすれば良い
'''
s = input()
s_reversed = list(reversed(s))
ans = len([(a,b) for a, b in zip(s, s_reversed) if a !=b]) // 2
print(ans)