#######################################################
# 1.30
# 思路：1. 使用while循环；
#      2. 规律：2的3次方<15<2的4次方，结果是3
#######################################################


def divide_times_1(n):
    times = 0
    while n >= 2:
        n = n / 2
        times += 1
    return times


def divide_times_2(n):
    times = 0
    while 2**times <= n:
        times += 1
    return times - 1


def test():
    n = 18
    print(f'first result: {divide_times_1(n)}')
    print(f'second result: {divide_times_2(n)}')


if __name__ == '__main__':
    test()