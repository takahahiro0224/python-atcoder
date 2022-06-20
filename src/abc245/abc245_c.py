y = "Yes"
no = "No"

n, k = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# # 差分がK以内か判定
# a_diff, b_diff = [], []
# for i in range(n-1):
#     a_diff.append((abs(a_list[i+1] - a_list[i]) <= k, abs(b_list[i+1] - a_list[i]) <= k))
#     b_diff.append((abs(a_list[i+1] - b_list[i]) <= k, abs(b_list[i+1] - b_list[i]) <= k))

# print(a_diff)
# print(b_diff)
# for i in range(n-2):
#     print(f"index: {i}")
#     if ((a_diff[i][0] or b_diff[i][0]) and (a_diff[i+1][0] or a_diff[i+1][1])) or ((a_diff[i][1] or b_diff[i][1]) and (b_diff[i+1][0] or b_diff[i+1][1])):
#         continue
#     else:
#         print(no)
#         exit(0)
        
# print(y)

dp, ep = [False] * n, [False] * n

# 初期値
dp[0], ep[0] = True, True

for i in range(1, n):
    if dp[i-1]:
        if abs(a_list[i-1] - a_list[i]) <= k:
            dp[i] = True
        if abs(a_list[i-1] - b_list[i]) <= k:
            ep[i] = True
    
    if ep[i-1]:
        if abs(b_list[i-1] - a_list[i]) <= k:
            dp[i] = True
        if abs(b_list[i-1] - b_list[i]) <= k:
            ep[i] = True

    if dp[i] or ep[i]:
        continue
    else:
        print(no)
        exit(0)

print(y)

