#################################################
# 1.13
# 思路：
# 1. 使用切片的方式data[::-1]，只能在列表和字符串中使用
# 2. 使用yield方式可以对任何迭代对象反转，返回一个生成器
# Python内置reversed函数也是可以对一切迭代器对象操作，
# 也返回一个迭代器
#################################################


def reverse(data):
    for i in range(len(data)):
        yield data[len(data)-1-i]


def test():
    test_list = [3, 5, -1, 8, 0]
    print(f'original sequence: {test_list}')
    print(f'own reverse function result: {reverse(test_list)}')
    print(f'own reverse result: {list(reverse(test_list))}')
    print(f'Python reversed function result: {reversed(test_list)}')


if __name__ == '__main__':
    test()

