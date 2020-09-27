#######################################################
# 1.25
# 思路：
#######################################################


def remove_punctuation(s):
    punctuation = ".,?!\"'-:;()[]/"
    new_s = ''
    for i in s:
        if i not in punctuation:
            new_s += i
    return new_s


def test():
    test_list = "Let's try, Mike."
    print(f'original string: {test_list}')
    print(f'after removing punctuation: {remove_punctuation(test_list)}')


if __name__ == '__main__':
    test()
