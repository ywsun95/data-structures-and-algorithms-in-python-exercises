##################################
# 1.4
# 思路：循环叠加
# 1.5
# 思路：使用生成器推导式
# 1.6-1.7
# 思路：range(1, n, 2)只输出奇数
##################################


def total_14(n: int):
    result = 0
    for i in range(n):
        result += i
    return result


def total_15(n: int):
    return sum(i for i in range(n))


def total_16(n: int):
    result = 0
    for i in range(1, n, 2):
        result += i
    return result


def total_17(n: int):
    return sum(i for i in range(1, n, 2))


def test():
    n = 10
    print(f'n={n}')
    print(f'1.4 result={total_14(n)}')
    print(f'1.5 result={total_15(n)}')
    print(f'1.6 result={total_16(n)}')
    print(f'1.7 result={total_17(n)}')


if __name__ == '__main__':
    test()
