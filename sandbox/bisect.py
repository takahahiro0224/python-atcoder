
# 二分探索のサンプル
myList = list(range(1, 10**9))

def binary_search(list, item):
    low = 0
    high = len(list) -1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

print(binary_search(myList, 123412))