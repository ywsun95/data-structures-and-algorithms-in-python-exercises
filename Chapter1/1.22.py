#######################################################
# 1.22
# 思路：使用索引进行遍历
#######################################################


def dot_product(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c


def test():
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4, 5, 6]
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={dot_product(a, b)}")


if __name__ == '__main__':
    test()
