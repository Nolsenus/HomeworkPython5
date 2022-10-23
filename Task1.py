import random


def get_player_move(candies_left, max_turn, name=''):
    valid_move = False
    move = None
    while not valid_move:
        try:
            move = int(input(f'Ваш ход{name} (Осталось {candies_left} конфет): '))
            if not (0 < move <= max_turn and move <= candies_left):
                raise ValueError
            valid_move = True
        except ValueError:
            print('Нельзя сделать такой ход. Попробуйте снова.')
    return move


def play(against_bot, bot_smart=False, max_turn=28, starting_candies=2021):
    players_turn = random.randint(0, 100) % 2 == 0
    candies_left = starting_candies
    if against_bot and bot_smart:
        while candies_left != 0:
            if players_turn:
                move = get_player_move(candies_left, max_turn)
                candies_left -= move
                print(f'Вы взяли {move} конфет, осталось {candies_left}.')
                players_turn = not players_turn
            else:
                remainder = candies_left % (max_turn + 1)
                move = max_turn
                if remainder:
                    move = remainder
                candies_left -= move
                print(f'Бот взял {move} конфет, осталось {candies_left}.')
                players_turn = not players_turn
        if not players_turn:
            print('Вы победили.')
        else:
            print('Победил бот.')
    elif against_bot:
        while candies_left != 0:
            if players_turn:
                move = get_player_move(candies_left, max_turn)
                candies_left -= move
                print(f'Вы взяли {move} конфет, осталось {candies_left}.')
                players_turn = not players_turn
            else:
                move = random.randint(1, max_turn if max_turn <= candies_left else candies_left)
                candies_left -= move
                print(f'Бот взял {move} конфет, осталось {candies_left}.')
        if not players_turn:
            print('Вы победили.')
        else:
            print('Победил бот.')
    else:
        while candies_left != 0:
            if players_turn:
                move = get_player_move(candies_left, max_turn, ', первый игрок')
                candies_left -= move
                print(f'Вы взяли {move} конфет, осталось {candies_left}.')
                players_turn = not players_turn
            else:
                move = get_player_move(candies_left, max_turn, ', второй игрок')
                candies_left -= move
                print(f'Вы взяли {move} конфет, осталось {candies_left}.')
                players_turn = not players_turn
        if not players_turn:
            print('Победил первый игрок.')
        else:
            print('Победил второй игрок.')


def main():
    against_bot = input('Вы хотите играть против другого игрока("игрок") или бота(что-либо кроме "игрок"): ')
    if against_bot == 'игрок':
        play(False)
    else:
        bot_smart = input('Вы хотите чтобы бот играл оптимально?("Да"/Что-либо кроме "Да"): ')
        if bot_smart == 'Да':
            play(True, True)
        else:
            play(True)


def test():
    print(bool(2))


if __name__ == '__main__':
    main()
