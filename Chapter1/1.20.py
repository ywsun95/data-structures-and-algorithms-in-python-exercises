#######################################################
# 1.20
# 思路：遍历让每个元素和任意一个随机元素交换
#######################################################
import random


def shuffle(data):
    length = len(data)
    for i in range(length):
        j = random.randint(0, length-1)
        data[i], data[j] = data[j], data[i]


def test():
    test_list = [4, 5, 2, 8, 1]
    print(f'sequence: {test_list}')
    shuffle(test_list)
    print(f'shuffle sequence: {test_list}')


if __name__ == '__main__':
    test()
