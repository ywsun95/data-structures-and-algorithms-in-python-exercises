################################################
# 1.8
# 思路：有个规律，同一个位置的正索引减去负索引等于总长度
################################################


def test():
    s = "abcde"
    s_len = len(s)
    for i in range(s_len):
        print(f's[{i}]={s[i]}, s[{i-s_len}]={s[i-s_len]}')


if __name__ == '__main__':
    test()