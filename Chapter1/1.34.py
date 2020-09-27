#######################################################
# 1.34
# 思路：只有单个字母拼写错误，在8个不同的句子产生不同错误
#######################################################

import random


def random_typo(statement: str):
    char_list = list(statement)
    while True:
        random_index = random.randint(0, len(char_list) - 1)
        if char_list[random_index] not in ' .':
            char_list[random_index] = chr(random.randint(97, 122))
            return ''.join(char_list)


def write(statement: str, times=100, wrong_times=8):
    # eight different statement
    wrong_order_list = []
    while len(wrong_order_list) < wrong_times:
        order = random.randint(1, times)
        if order not in wrong_order_list:
            wrong_order_list.append(order)

    # eight different typos
    for i in range(1, times+1):
        if i in wrong_order_list:
            result = random_typo(statement) + '(wrong)'
        else:
            result = statement
        print(f'{i}. {result}')


def test():
    statement = 'I will never spam my friends again.'
    write(statement)


if __name__ == '__main__':
    test()
