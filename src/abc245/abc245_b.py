n = int(input())
a_list = set(map(int, input().split()))
n_list = set(range(0,2001))
diff = n_list - a_list
print(min(diff)) #差集合の最小値

