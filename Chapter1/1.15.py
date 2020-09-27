#################################################
# 1.15
# 思路：使用集合的元素不重复特性
# 或者循环比较
#################################################


def is_distinct_by_set(data):
    return len(set(data)) == len(data)


def is_distinct_by_for(data):
    length = len(data)
    for i in range(0, length):
        for j in range(i+1, length):
            if data[i] == data[j]:
                return False
    return True


def test():
    test_list = [4, 6, 8, 2]
    print(f'sequence: {test_list}')
    print(f'is_distinct_by_set result: {is_distinct_by_set(test_list)}')
    print(f'is_distinct_by_for result: {is_distinct_by_for(test_list)}')


if __name__ == '__main__':
    test()
