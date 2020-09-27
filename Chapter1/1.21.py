#######################################################
# 1.21
# 思路：把输入的值存入列表中
#######################################################


def read_line():
    lines = []
    while True:
        try:
            lines.insert(0, input("input:").strip())
        except EOFError:
            for i in lines:
                print(i)
            break


if __name__ == '__main__':
    read_line()
