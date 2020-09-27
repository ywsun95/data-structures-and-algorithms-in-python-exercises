##################################
# 1.9
# 思路：
# 1.10
# 思路：
# 1.11
# 思路：规律是2的n次方
##################################


def r_19():
    return range(50, 81, 10)


def r_110():
    return range(8, -9, -2)


def r_111():
    return [2**i for i in range(9)]


def test():
    print(f'R_1.9 result {list(r_19())}')
    print(f'R_1.10 result {list(r_110())}')
    print(f'R_1.11 result {r_111()}')


if __name__ == '__main__':
    test()
