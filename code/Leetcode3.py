# 3. 无重复字符的最长子串
# 滑动窗口

def func():
    input_s = input().strip()

    max_len = 0
    temp = ""
    for x in input_s:
        if x in temp:
            index = temp.index(x)
            temp = temp[index+1:]
        temp += x
        max_len = max(max_len, len(temp))

    print(max_len)


if __name__ == '__main__':
    func()
