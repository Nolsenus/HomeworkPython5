import re


def input_polynomial(param):
    polynomial = re.compile('(([1-9][0-9]*\\*?)?x?(\\^-?[1-9][0-9]*)?[+-])*([1-9][0-9]*\\*?)?x?(\\^-?[1-9][0-9]*)?')
    is_polynomial = False
    res = ''
    while not is_polynomial:
        res = input(f'Введите {param} многочлен: ').lower().replace(' ', '')
        if polynomial.fullmatch(res):
            is_polynomial = True
        else:
            print('Это не многолчен. Попробуйте ещё раз.')
    return res


def get_coeffs(polynomial):
    if not polynomial:
        return dict({})
    result = {}
    current_coef = 0
    current_pow = 0
    is_negative = False
    before_x = True
    is_pow = False
    for char in polynomial:
        if char.isdigit():
            if is_pow:
                is_pow = False
            if before_x:
                current_coef *= 10
                current_coef += int(char)
            else:
                current_pow *= 10
                current_pow += int(char)
        elif char == 'x':
            before_x = False
            if current_coef == 0:
                current_coef = 1
            if is_negative:
                current_coef = -current_coef
            is_negative = False
        elif char == '+' or char == '-':
            if not is_pow and not(current_coef == 0 and current_pow == 0):
                if current_pow == 0:
                    if not before_x:
                        current_pow = 1
                    elif is_negative:
                        current_coef = -current_coef
                if is_negative:
                    current_pow = -current_pow
                if current_pow in result.keys():
                    result[current_pow] += current_coef
                else:
                    result[current_pow] = current_coef
                current_pow = 0
                current_coef = 0
                before_x = True
            if char == '+':
                is_negative = False
            else:
                is_negative = True
        else:
            is_pow = True
    if not before_x:
        if current_pow == 0:
            current_pow = 1
        if is_negative:
            current_pow = -current_pow
    else:
        if current_coef == 0:
            current_coef = 1
        if is_negative:
            current_coef = -current_coef
    if current_pow in result.keys():
        result[current_pow] += current_coef
    else:
        result[current_pow] = current_coef
    return result


def add_polynomials(first, second):
    first_rfw = first.replace('*', '').lower()
    second_rfw = second.replace('*', '').lower()
    first_coefs = get_coeffs(first_rfw)
    second_coefs = get_coeffs(second_rfw)
    result_coeffs = {}
    for pol_pow in first_coefs.keys():
        if pol_pow in second_coefs.keys():
            result_coeffs[pol_pow] = first_coefs[pol_pow] + second_coefs[pol_pow]
        else:
            result_coeffs[pol_pow] = first_coefs[pol_pow]
    for pol_pow in second_coefs.keys():
        if pol_pow not in first_coefs.keys():
            result_coeffs[pol_pow] = second_coefs[pol_pow]
    keys = list(result_coeffs.keys())
    keys.sort(reverse=True)
    result = ''
    i = 0
    while i < len(keys) and result == '':
        pol_pow = keys[i]
        result = str(result_coeffs[pol_pow]) + '*x^' + str(pol_pow) if result_coeffs[pol_pow] != 0 else ''
        i += 1
    for pol_pow in keys[i:]:
        result += f' + {(str(result_coeffs[pol_pow]) + "*" if result_coeffs[pol_pow] != 1 else "")}x^{pol_pow}'
    return result


def main():
    first = input_polynomial('первый')
    second = input_polynomial('второй')
    print(first)
    print(second)
    print(add_polynomials(first, second))


if __name__ == '__main__':
    main()
