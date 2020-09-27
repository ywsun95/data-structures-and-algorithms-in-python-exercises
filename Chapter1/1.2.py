##################################
# 1.2
# 思路：把数字变成字符串，判断最后一位
##################################


def is_even(k):
    str_k = str(k)
    if str_k[-1] in ['0', '2', '4', '6', '8']:
        return True
    return False


def test():
    for i in range(-5, 5):
        print(f"{i} {'is' if is_even(i) else 'is not'} even")


if __name__ == '__main__':
    test()
