#######################################################
# 1.32
# 思路：只计算两位数加减乘除
#######################################################


def calculator():
    """operator: +, -, *, / """
    items = []
    operators = '+-*/'
    print('Input a number or an operator on a separate line.')
    while True:
        item = input('>>: ').strip()
        if not item:
            continue

        # determine whether the input is legal
        if len(items) % 2 == 0:
            try:
                items.append(float(item))
                print('Expression:', ' '.join(str(i) for i in items))
            except ValueError:
                print('The input is not legal, please input number.')
        else:
            if item in operators:
                items.append(item)
                print('Expression: ', ' '.join(str(i) for i in items))
            else:
                print('The input is not legal, please input operator.')

        if len(items) == 3:
            result = eval(' '.join(str(i) for i in items))
            print('The result: {}'.format(result))
            break


if __name__ == '__main__':
    calculator()
