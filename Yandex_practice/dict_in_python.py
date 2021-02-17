friends =  {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск', 'Нур Султан': 'Нур-Султан', 'Guðrún':'Рейкьявик'}
for name, city in friends.items():
    print (name, 'живёт в городе', city)


favorite_songs = {
    'Серёга': ["Unforgiven", "Holiday", "Highway to hell"],
    'Соня': ["Shake it out", "Don't stop me now", "Наше лето"],
    'Дима': ["Владимирский централ", "Мурка", "Третье сентября"]
}

# напишите код, который напечатает на экран, сколько у Димы любимых песен

# здесь напишите код, который напечатает
# все любимые песни Сони через запятую и пробел ', '
print (len (favorite_songs['Дима']))
# здесь напишите код, который напечатает
print (', '.join (favorite_songs['Соня']))

import datetime as dt


moment_in_time = dt.datetime(1961, 4, 12, 9, 7, 0)  # снова старт Гагарина

now = moment_in_time.utcnow()
print(now)