#######################################################
# 1.26
# 思路：使用内置函数eval执行字符串命令
#######################################################


def formula(a: int, b: int, c: int):
    for operator in '+-*/':
        expresses = [
            f'{a} {operator} {b} == {c}',
            f'{a} == {b} {operator} {c}'
        ]
        for express in expresses:
            if eval(express):
                return express.replace("==", '=')


def test():
    test_list = [
        (1, 2, 3), (2, 3, 4), (6, 3, 2)
    ]

    for a, b, c in test_list:
        if formula(a, b, c):
            print(f"{a, b, c} result: True, {formula(a, b, c)}")
        else:
            print(f"{a, b, c} result: False")


if __name__ == '__main__':
    test()
