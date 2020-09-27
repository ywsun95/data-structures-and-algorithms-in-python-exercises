#######################################################
# 1.24
# 思路：
#######################################################


def vowels_num(s: str):
    count = 0
    for i in s:
        if i in 'aeiou':
            count += 1
    return count


def test():
    s = 'fire the hole'
    print(f'In string "{s}", the numbers of vowels is {vowels_num(s)}')


if __name__ == '__main__':
    test()