# 2. 两数相加
import math


def func(l1, l2):
    l1_sum = 0
    for i, l in enumerate(l1):
        l1_sum += l*10**i
    print(l1_sum)

    l2_sum = 0
    for i, l in enumerate(l2):
        l2_sum += l*10**i
    print(l2_sum)

    l_add = l1_sum + l2_sum
    res = list(map(int, str(l_add)[::-1]))
    print(res)


if __name__ == '__main__':
    il1 = [2, 4]
    il2 = [2, 4, 6]
    func(il1, il2)
