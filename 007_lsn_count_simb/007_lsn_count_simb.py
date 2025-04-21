"""Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()"""

user_input: str = input(f"Зробіть ввод, натисніть enter, чекайте обчислинь :) ")
unique_symbols: set = set(user_input)

if len(unique_symbols) > 10:
    print(f"Ваш ввод містив {len(unique_symbols)}. TRUE))")
elif len(unique_symbols) <= 10:
    print(f"Ваш ввод містив {len(unique_symbols)}. FALSE((")
elif not len(unique_symbols):
    print(f"Здаеться ввод відсутній")
else:
    print(f"unknown error")
