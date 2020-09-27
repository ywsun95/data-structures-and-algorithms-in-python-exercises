#######################################################
# 1.27
# 思路：把结果保存到列表内
#######################################################


def factors_original(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


def factors_modify(n):
    part = []
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            part.insert(0, n // k)
        k += 1
    if k * k == n:
        yield k
    for k in part:
        yield k


def test():
    n = 100
    print(f'original factors: {list(factors_original(n))}')
    print(f'after modify: {list(factors_modify(n))}')


if __name__ == '__main__':
    test()
