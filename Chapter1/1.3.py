##################################
# 1.3
# 思路：逐个比较
##################################


def minmax(data):
    min_num, max_num = data[0], data[0]
    for i in data:
        if i < min_num:
            min_num = i
        elif i > max_num:
            max_num = i
    return min_num, max_num


def test():
    test_list = [4, 9, -3, 13, -4, -9, 8]
    min_num, max_num = minmax(test_list)
    print(f'list: {test_list}')
    print(f"min={min_num}, max={max_num}")


if __name__ == '__main__':
    test()
