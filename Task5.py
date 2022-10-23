def find_longest_rising_sequence(array):
    if len(array) < 2:
        return False
    max_length = 0
    max_start = None
    while array:
        current_start = min(array)
        current = current_start
        current_length = 0
        while current in array:
            current_length += 1
            current += 1
        if current_length > max_length:
            max_length = current_length
            max_start = current_start
        array = list(filter(lambda x: x > current, array))
    if max_length > 1:
        return max_start, max_start + max_length - 1
    return False


def main():
    sequence = input('Введите список целых чисел через запятую: ').replace(' ', '')
    sequence = sequence.split(',')
    nums = []
    for element in sequence:
        try:
            nums.append(int(element))
        except ValueError:
            sequence.remove(element)
            print(f'Элемент {element} не является целым числом и будет пропущен.')
    result = find_longest_rising_sequence(nums)
    print(f'{nums} -> {result if result else "В заданном списке нет возрастающих последовательностей."}')


if __name__ == '__main__':
    main()
