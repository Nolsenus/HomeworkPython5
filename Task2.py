def encode(string):
    if not string:
        return ''
    previous_char = string[0]
    sequence_length = 1
    res = ''
    for char in string[1:]:
        if char == previous_char:
            sequence_length += 1
        else:
            res += str(sequence_length) + previous_char
            sequence_length = 1
            previous_char = char
    res += str(sequence_length) + previous_char
    return res


def decode(string):
    res = ''
    reps = 0
    for char in string:
        if char.isdigit():
            reps *= 10
            reps += int(char)
        else:
            res += char * reps
            reps = 0
    return res


def main():
    string = ''
    with open('input.txt', 'r', encoding='utf-8') as file:
        string = file.read()
    print(string)
    encoded_string = encode(string)
    print(encoded_string)
    with open('encoded.txt', 'w') as file:
        file.write(encoded_string)
    decoded_string = decode(encoded_string)
    print(decoded_string)
    with open('decoded.txt', 'w') as file:
        file.write(decoded_string)
    if string == decoded_string:
        print('Сжатие и восстановление не изменили исходную строку.')
    else:
        print('Что-то пошло не по плану.')


if __name__ == '__main__':
    main()
