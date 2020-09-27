#################################################
# 1.14
# 思路：只有当两个数都是奇数时，结果才是奇数
#################################################


def is_product_odd(data):
    odd_set = set()
    for i in data:
        if i % 2 == 1:
            odd_set.add(i)
    return len(odd_set) > 1


def test():
    test_list = [3, 5, 4, 7, 6, 8]
    print(f'sequence: {test_list}')
    print(f'result: {is_product_odd(test_list)}')


if __name__ == '__main__':
    test()
