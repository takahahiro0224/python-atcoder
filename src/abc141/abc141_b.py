# https://atcoder.jp/contests/abc141/tasks/abc141_b

S = list(input())
odd = ['R', 'U', 'D']
even = ['L', 'U', 'D']
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] not in odd:
            print('No')
            exit()
    else:
        if S[i] not in even:
            print('No')
            exit()
print('Yes')

