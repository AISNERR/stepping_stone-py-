def is_anyone_in(collection, city):
    if city in collection.values():
        for name in collection.keys():
            if collection[name] == city:
                print('В городе ' + city + ' живёт ' + name + '.')
    else:
        print('Пока никого.')
friends = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Хабаровск',
    'Егор': 'Пермь'
}

is_anyone_in(friends, 'Хабаровск')