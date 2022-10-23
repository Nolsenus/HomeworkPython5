def remove_abv_words(text):
    return ' '.join(filter(lambda x: 'абв' not in x, text.split()))


def main():
    text = ''
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    print(text)
    print(remove_abv_words(text))


if __name__ == '__main__':
    main()
