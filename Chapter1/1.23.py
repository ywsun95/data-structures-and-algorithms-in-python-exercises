#######################################################
# 1.23
# 思路：使用raise抛出异常
#######################################################


class MyList:
    def __init__(self, n):
        """n is list length"""
        self.n = n
        self.data = []

    def append(self, obj):
        if len(self.data) < self.n:
            self.data.append(obj)
        else:
            raise IndexError("Don't try buffer overflow attacks in Python!")

    def __str__(self):
        return str(self.data)


def test():
    li = MyList(5)

    for i in range(9):
        li.append(i)
        print(li)


if __name__ == '__main__':
    test()
