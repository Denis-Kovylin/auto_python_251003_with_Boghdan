text_gap: str = "\n"
alice_in_wonderland: str = (
    "\"Would you tell me, please, which way I ought to go from here?\"\n"
    "\"That depends a good deal on where you want to get to,\" said the Cat.\n"
    "\"I don't much care where ——\" said Alice.\n"
    "\"Then it doesn't matter which way you go,\" said the Cat.\n"
    "\"—— so long as I get somewhere,\" Alice added as an explanation.\n"
    "\"Oh, you're sure to do that,\" said the Cat, \"if you only walk long enough.\""
)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
print(f"TASK #1: {alice_in_wonderland}{text_gap}")

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
alice_in_wonderland_2: str = alice_in_wonderland
single_quotes: list = [item for item in alice_in_wonderland_2 if item == "'"]
print(f"TASK #2: Знайдено: {len(single_quotes)} символів одинарної лапки ('){text_gap}")

# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland_3: str = alice_in_wonderland_2
print(alice_in_wonderland_3, text_gap)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
sea_unit: str = "км2"
back_sea: int = 436402
azov_sea: int = 37800
sum_seas: int = back_sea + azov_sea
print(
    f"Тут треба скласти площу Черного Моря: {back_sea}{sea_unit} + площу Азовського Моря: {azov_sea}{sea_unit} = {sum_seas}{sea_unit}{text_gap}"
            )


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
good_unit: str = "товарив"
total_goods: int = 375291
warehouse_1: int = total_goods - 222950
warehouse_3: int = total_goods - 250449
warehouse_2: int = total_goods - (warehouse_1 + warehouse_3)
print(
    f"Якщо ми віднімимо від загальної кількості товарів: {total_goods} кількість товарів, що зберігаються 1му + 2му = {warehouse_3}: {good_unit} на складі #3{text_gap}"
    f"А якщо ми віднімимо від загальної кількості товарів: {total_goods} кількість товарів, що зберігаються 2му + 3му ={warehouse_1}: {good_unit} на складі #1{text_gap}"
    f"Тепер порахуемо скільки товарів на складі #2: віднімимо від загальної кількості товарів: {total_goods} кількість товарів, що зберігаються 1му + 3му = {warehouse_2}: {good_unit} на складі #2{text_gap}"
    f"Підсумовуемо!{text_gap}"
    f"На першому складі: {warehouse_1} {good_unit};{text_gap}"
    f"На другому складі: {warehouse_2} {good_unit};{text_gap}"
    f"На третьому складі: {warehouse_3} {good_unit};{text_gap}"
)
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_payment: int = 1179
time_interval: int = 18
total_price: int = time_interval * month_payment
print(
    f"Пропоную одразу порахувати який саме час хлопцю з бати ками деведеться платати за комп'ютер. Півтора року це: {time_interval} місяців.{text_gap}"
    f"Весь цей час, {time_interval} місяців треба платити. Тож помножимо щомісячний платіж {month_payment}грн на {time_interval} місяців строку кредутивання.{text_gap}"
    f"1179 * 18 = {total_price}грн.{text_gap}"
)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("Залишок від ділення  8019 на 8 =", 8019 % 8)
print("Залишок від ділення  9907 на 9 =", 9907 % 9)
print("Залишок від ділення  2789 на 5 =", 2789 % 5)
print("Залишок від ділення  7248 на 6 =", 7248 % 6)
print("Залишок від ділення  7128 на 5 =", 7128 % 5)
print("Залишок від ділення 19224 на 9 =", 19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big: int = 274 * 4
pizza_mid: int = 218 * 2
juice: int = 35 * 4
cake: int = 350 * 1
water: int = 21 * 3
total_paty_price: int = pizza_big + pizza_mid + juice + cake + water
print(
    f"Іринка замовляє:{text_gap}"
    f"— Велику піцу 4 шт по 274 грн = {pizza_big} грн{text_gap}"
    f"— Середню піцу 2 шт по 218 грн = {pizza_mid} грн{text_gap}"
    f"— Сік 4 шт по 35 грн = {juice} грн{text_gap}"
    f"— Торт 1 шт по 350 грн = {cake} грн{text_gap}"
    f"— Вода 3 шт по 21 грн = {water} грн{text_gap}"
    f"Всього потрібно: {total_paty_price} грн{text_gap}"
)
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos_total: int = 232
photos_per_page: int = 8
pages_needed: int = (photos_total + photos_per_page - 1) // photos_per_page
print(
    f"Ігор має {photos_total} фото, а на одну сторінку вміщується максимум {photos_per_page} фото.{text_gap}"
    f"Тому йому знадобиться {pages_needed} сторінок, щоб вклеїти всі фотографії{text_gap}"
)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance_km: int = 1600
fuel_per_100km: float = 9
tank_capacity: int = 48
fuel_needed: float = (distance_km / 100) * fuel_per_100km
refuels_needed: int = int(fuel_needed // tank_capacity)
if fuel_needed % tank_capacity != 0:
    refuels_needed += 1

print(
    f"Відстань Харків–Будапешт = {distance_km} км{text_gap}"
    f"Витрата пального = {fuel_per_100km} л на 100 км{text_gap}"
    f"Загальна кількість пального: {fuel_needed} літрів{text_gap}"
    f"Місткість баку = {tank_capacity} літрів{text_gap}"
    f"Щонайменше потрібно заправок: {refuels_needed}{text_gap}"
)