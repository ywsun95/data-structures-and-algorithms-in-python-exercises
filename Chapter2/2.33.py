import re


def polynomial_derivative(p: str):
    """Return the first derivative of the polynomial.

    p    a polynomial in standard algebraic notation
    """
    # use `re` module, matching method as the follow:
    # sign         [-+]?
    # factor       \d*\.*\d*
    # variable     x?\^?
    # power        \d*
    items = re.findall(r'[-+]?\d*\.*\d*x?\^?\d*', p.replace(' ', ''))

    result_list = []
    for item in items:            # type: str
        if not item:
            continue
        elif 'x' not in item:     # constant
            continue
        elif '^' not in item:     # the power is 1
            result_list.append(item.replace("x", ''))
        else:
            factor, power = item.split('x^')
            new_factor = float(factor) * int(power)
            if new_factor.is_integer():
                new_factor = int(new_factor)
            new_power = int(power) - 1
            if new_power == 1:
                res = [str(new_factor), 'x']
            else:
                res = [str(new_factor), 'x^', str(int(power) - 1)]
            result_list.append(''.join(res))
    return ''.join(result_list)


if __name__ == '__main__':
    p = "3.14x^4-9x^3 - 4x^2 + 1.2x + 4"
    print('original polynomial:', p)
    print('the first derivative of polynomial:', polynomial_derivative(p))
