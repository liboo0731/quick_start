# 5. 最长回文子串
# 动态规划

def func(s):
    n = len(s)
    if n < 2:
        return s

    max_len = 1
    begin = 0

    dp = [[False] * n for _ in range(n)]
    # 对角线单个字母都为TRUE
    for i in range(n):
        dp[i][i] = True

    # 按列循环，如果当前首尾相同，由左下角状态确定当前状态
    for j in range(1, n):
        for i in range(0, j):
            # print(f'{i}:{j}-{s[i:j+1]}')
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = False

            if dp[i][j] and j - i + 1 > max_len:
                max_len = j - i + 1
                begin = i

    print(s[begin: begin+max_len])


if __name__ == '__main__':
    s1 = 'babcdba'
    func(s1)
