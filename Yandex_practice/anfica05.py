FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']


def process_query(query):
    print("Привет, я Анфиса!")
    count = len(FRIENDS)

    if query == 'Сколько у меня друзей?':
        print('У тебя', str(count), 'друзей')
    elif query == 'Кто все мои друзья?':
        print('Твои друзья:', *FRIENDS)
    else:
        print('<неизвестный запрос>')


def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')


process_query('Сколько у меня друзей?')
process_query('Как меня зовут?')
process_query('Кто все мои друзья?')