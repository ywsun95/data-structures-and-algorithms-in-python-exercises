#######################################################
# 1.16
# 解释：对于容器类型作为实参传入函数中，只是传入只是指向容器的地
#      址，相当于起个别名，所以形参和实参指向内容是同一个，所以当
#      函数中容器类型被修改时，函数外实参所执行的内容也被修改了
# 1.17
# 解释：这种方式不能实现所要求的功能，因为每次for循环只是把data
#      的一个元素起个别名var，在var *= factor之后，var被赋予
#      新的值，而data的元素则取消了别名，不受影响，所以data的
#      值并没有变，对应的实参没变
#######################################################


def scale_116(data, factor):
    for j in range(len(data)):
        data[j] *= factor


def scale_117(data, factor):
    for val in data:
        val *= factor


def test():
    test_list = [4, 5, 2, 8, 1]
    factor = 3
    print(f'original list: {test_list}')
    scale_116(test_list, factor)
    print(f'C-1.16 result: {test_list}')
    scale_117(test_list, factor)
    print(f'C-1.17 result: {test_list}')


if __name__ == '__main__':
    test()
