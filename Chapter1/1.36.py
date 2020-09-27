#######################################################
# 1.36
# 思路：
#######################################################


def count(s: str):
    words = s.split()
    s_dict = {}.fromkeys(words, 0)
    for word in words:
        s_dict[word] += 1
    return s_dict


def test():
    s = input('Input the strings: ').strip()
    if s:
        print(count(s))


if __name__ == '__main__':
    test()
