################################################
# 1.12
# 思路：使用randrange来随机索引值，通过索引值来取值
################################################

import random


def own_choice(data):
    index = random.randrange(0, len(data))
    return data[index]


def test():
    test_list = [4, 7, 'abc', '8', -4]
    print(f'sequence: {test_list}')
    print(f'a random element: {own_choice(test_list)}')


if __name__ == '__main__':
    test()
