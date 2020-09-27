#######################################################
# 1.31
# 思路：
#######################################################


def make_change():
    prompt = "Please input the amount charged and the amount given,\n"
    prompt += "and separated by whitespace:"
    try:
        charged, given = input(prompt).split()
    except ValueError:
        print("must be input 2 values.")
        exit(1)

    if not (charged.isdigit() and given.isdigit()):
        print('the amount must be positive integer.')
        exit(1)

    change_sum = int(charged) - int(given)
    if change_sum < 0:
        print('the amount charged must be greater than or equal to the amount given.')
        exit(1)
    elif change_sum == 0:
        print("the amount charged is equal to the amount given. Don't make change.")
        exit(0)

    bill_and_coins = [100, 50, 20, 10, 5, 2, 1]
    print('make change')
    for i in bill_and_coins:
        num, remain = divmod(change_sum, i)
        if num != 0:
            print(f'{i} ￥ nums: {num}')
        change_sum = remain


if __name__ == '__main__':
    make_change()
