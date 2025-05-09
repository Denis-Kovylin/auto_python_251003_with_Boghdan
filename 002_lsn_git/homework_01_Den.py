# task 01 == Виправте синтаксичні помилки
text_gap = "\n"
print("Hello", end = " ")
print("world!", text_gap)

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!{text_gap}")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)
print(text_gap)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery, text_gap)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
sum_of_trees = apple_trees + pear_trees + plum_trees

print(
    f"Давай сразу считать сколько каких деревьев у нас есть. То, что яблок {apple_trees}шт. мы знаем сразу.{text_gap}"
    f"Груш у нас - (количество яблок + 5). То есть 4 + 5 = {pear_trees}шт. Слив у нас - (количество яблок -2).{text_gap}"
    f"То есть 4 - 2 = {plum_trees}. Теперь считаем общую сумму деревьев - {apple_trees} + {pear_trees} + {pear_trees} = {sum_of_trees} деревьев.{text_gap * 3}"

)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
basic_temp = 0
morning_temp = basic_temp + 5
day_temp = morning_temp - 10
evening_temp = day_temp + 4

print(
    f"Давай двигаться пошагово. Нам известно, что до до обеда температура было {basic_temp} + 5, то есть {morning_temp} градусов{text_gap}"
    f"Но уже после обеда похолодало на 10 градусов. Отнимаем от утрений температуры 10: {morning_temp} - 10 = {day_temp} градусов{text_gap}"
    f"А вечером температура поднялась на 4 градуса. Прибавим эти 4 градуса к дневной температуре: {day_temp} + 4 = {evening_temp}.{text_gap}"
    f" Ответ: вечерняя температура составляет {evening_temp} градусов{text_gap * 3}"
)
# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
print(" TASKA #9 ")
all_boys = 24
all_girls = all_boys // 2
all_children = all_girls + all_boys
absent_boys = 1
absent_girls = 2
absent_children = absent_boys + absent_girls
present_children = all_children - absent_children

print(
    f"Для начало подсчитаем сколько же в секцию ходит девочек всего. Это половина от мальчиков, чье количество нам известно.{text_gap}"
    f"Нужно подилить количество мальчиков на 2: {all_boys} / 2 = {int(all_girls)} девочек в секции. Если сложим количества мальчиков и девочек{text_gap}"
    f"то узнаем сколько всего детей посещает секцию танцев: {all_boys} мальчиков + {int(all_girls)} девочек = {int(all_children)} детей{text_gap}"
    f"Теперь нам нужно посчитать детей, которые сегодня не пришли: {absent_boys} мальчик + {absent_girls} девочки = {absent_children} ребенка{text_gap}"
    f"Дальше нам нужно просто отнять от общего числа детей, что ходят на танцы, общее число детей, которое сегодня не пришли. {int(all_children)} - {absent_children} = {int(present_children)}.{text_gap}"
    f" Ответ: сегодня на танцевальную секцию пришли {int(present_children)} ребенка.{text_gap * 3}"
)
# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1 = 8
book_2 = book_1 - 2
book_3 = int((book_1 + book_2) // 2)
sum_of_books = int(book_1 + book_2 + book_3)

print(
    f"Нужно последовательно вычислить стоимость 2й и 3й книги ( стоимость первой нам уже известна ) и сложить их.{text_gap}"
    f"Что б узнать стоимость 2й нам от стоимости 1й нужно отнять 2грн: {book_1}грн - 2грн = {book_2}грн. Стоимость 3й вычислить немного сложнее.{text_gap}"
    f"Не не очень сложна) Нам нужно сначало сложить стоимость 1й и 2й, и только потом разделить на 2: ({book_1}грн + {book_2}грн) / 2 = {book_3}грн.{text_gap}"
    f"Ну и все, складываем стоимости всех 3-х книг и дело в шляпе: {book_1}грн + {book_2}грн + {book_3}грн = {sum_of_books}грн.{text_gap * 3}"
)
