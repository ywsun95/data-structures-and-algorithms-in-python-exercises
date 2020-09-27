##############################
# 1.1
# 思路：for循环从-|n/2|到|n/2|
##############################


def is_multiple(n, m):
    half_n = int(abs(n)/2)
    for i in range(-half_n, half_n+1):
        if m*i == n:
            return True
    return False


def test():
    test_list = [
        (3, 5), (4, 2), (-2, 4), (-4, 2), (6, -3), (3, -6), (-4, -8), (-8, -4)
    ]
    for n, m in test_list:
        print(f"n={n}, m={m}, is_multiple -> {is_multiple(n, m)}")


if __name__ == '__main__':
    test()

