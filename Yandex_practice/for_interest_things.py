bands = ['Пикник', 'Ария', 'Блестящие', 'Блестящие']
unique_band_names = set(bands)
print(unique_band_names)
s = set('сервер')
print(s)
songs1 = {'Три белых коня', 'Happy new year', 'Снежинка'}
songs2 = {'Last christmas', 'Снежинка', 'Happy new year'}

print(songs1.union(songs2))

#example of using function difference
my_songs = {'Наше лето', 'Голубой вагон', 'Облака'}
friends_songs = {'Голубой вагон', 'Облака', 'Yesterday', 'Наше лето'}

print(friends_songs.difference(my_songs))


def print_shopping_list(pizza, salad):
    dish = set(pizza)

    dish = dish.union(salad)
    print(dish)

    for i in dish:
        weight = 0
        if i in pizza.keys(): weight += pizza[i]
        if i in salad.keys(): weight += salad[i]
        print(i, ': ', weight, sep='')


pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

print_shopping_list(pizza, salad)

