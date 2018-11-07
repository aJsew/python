import random
import sys

rules = '''
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны.
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Если ответите "y", когда у вас в карточке отсутствует число, 
выпавшее в ходе игры - вы покинете игру.
Если вы ответите "n", когда число присутствует в вашей карточке вы также покинете игру.
Выигрывает тот, кто первый вычеркнет все числа из своей карточки.

--  Удачи!  --
'''

print(rules)


ballsleft = 90
user = 15
computer = 15


pouch = random.sample(range(90), 90)
game_set = random.sample(range(90), 30)
user_set = random.sample(game_set, 15)


computer_set = [_ for _ in game_set if not _ in user_set]
user_card = [user_set[:5], user_set[5:10], user_set[10:]]
computer_card = [computer_set[:5], computer_set[5:10], computer_set[10:]]


for userline in user_card:
    userline.sort()
    userline.insert(random.randint(0, 4), ' ')
    userline.insert(random.randint(0, 5), ' ')
    userline.insert(random.randint(0, 6), ' ')
    userline.insert(random.randint(0, 7), ' ')

for computerline in computer_card:
    computerline.sort()
    computerline.insert(random.randint(0, 4), ' ')
    computerline.insert(random.randint(0, 5), ' ')
    computerline.insert(random.randint(0, 6), ' ')
    computerline.insert(random.randint(0, 7), ' ')


def card(p):
    if p == 0:
        print('{:-^26}'.format(' Ваша карточка '))
        for line_u in user_card:
            for num_1 in line_u:
                print('{0:>2}'.format(num_1), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
    if p == 1:
        print('{:-^26}'.format(' Карточка компьютера '))
        for line_c in computer_card:
            for num_2 in line_c:
                print('{0:>2}'.format(num_2), end=' ')
            print()
        print('{:-^26}\n'.format('-'))


def player_turn():
    a = input('Зачеркнуть цифру? (y/n): ')
    if a == 'y':
        if ball in user_set:
            for l in user_card:
                try:
                    l.insert(l.index(ball), '--')
                    l.pop(l.index(ball))
                except ValueError:
                    continue
            print('\nSUCCESS')
            return 1
        else:
            print('\nYou left the game')
            sys.exit()
    if a == 'n':
        if ball in user_set:
            print('\nYou left the game')
            sys.exit()
        else:
            print('\nSUCCESS')


def computer_turn():
    if ball in computer_set:
        for i in computer_card:
            try:
                i.insert(i.index(ball), '--')
                i.pop(i.index(ball))
            except ValueError:
                continue
        return 1


for ball in pouch:
    ballsleft -= 1
    print('\nНовый бочонок: {} (осталось: {})\n'.format(ball, ballsleft))
    card(0)
    card(1)
    if player_turn() == 1:
        user -= 1
    if computer_turn() == 1:
        computer -= 1
    if user == 0:
        print('\nYou win, congratulations!')
        sys.exit()
    if computer == 0:
        print('\nComputer wins')
        sys.exit()
    if ballsleft == 0:
        print('\nGAME OVER')
        sys.exit()