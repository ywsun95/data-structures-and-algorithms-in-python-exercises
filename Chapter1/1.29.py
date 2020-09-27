#######################################################
# 1.29
# 思路：使用递归，循环从列表中取出一个，然后把剩下的递归到下一次
#      再循环取出每一个，以此类推。返回每次得到的列表
#######################################################

from functools import reduce


def combine(s: list):
    s_copy = s.copy()
    result = []
    for i in s:
        s_copy = s.copy()
        s_copy.remove(i)
        if s_copy:
            for res in combine(s_copy):
                result.append(i+res)
        else:
            result.append(i)
    return result


def test():
    test_list = ['c', 'a', 't', 'd', 'o', 'g']
    result_nums = reduce(lambda x, y: x*y, range(1, len(test_list)+1))
    print(f'sequence: {test_list}')
    print(f'the number of result: {len(test_list)}! = {result_nums}')
    print(f'the number of test result: {len(set(combine(test_list)))}')


if __name__ == '__main__':
    test()

