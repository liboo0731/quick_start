# 1. 两数之和
# 哈希表

def func(nums, target):
    hashtable = dict()

    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[num] = i
    return []


if __name__ == '__main__':
    n = [2, 4, 6, 9, 12, 0]
    tg = 12
    print(func(n, tg))
