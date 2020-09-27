#######################################################
# 1.35
# 思路：
#######################################################

import random


def random_birthday(n: int):
    return [random.randint(1, 365) for _ in range(n)]


def birthday_paradox(n: int):
    sample_num = 10000
    count = 0
    for _ in range(sample_num):
        if len(set(random_birthday(n))) < n:
            count += 1
    return count/sample_num


def test():
    for i in range(5, 101, 5):
        p = birthday_paradox(i)
        print('n={}, p={:2f}%'.format(i, p))


if __name__ == '__main__':
    test()
