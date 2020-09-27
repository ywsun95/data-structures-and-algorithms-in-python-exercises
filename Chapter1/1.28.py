#######################################################
# 1.28
# 思路：
#######################################################


def norm(v, p=2):
    return pow(sum(pow(i, p) for i in v), 1/p)


def test():
    test_list = [4, 3]
    print(f'p=2,v={tuple(test_list)}, ||v||={norm(test_list)}')
    print(f'p=3,v={tuple(test_list)}, ||v||={norm(test_list, p=3)}')
    print(f'p=4,v={tuple(test_list)}, ||v||={norm(test_list, p=4)}')


if __name__ == '__main__':
    test()