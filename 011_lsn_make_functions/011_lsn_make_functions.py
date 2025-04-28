# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_num(a: int | float, b: int | float) -> float:
    return a + b

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def list_arithmetic_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string_writer(string_to_reverse: str) -> str:
    return string_to_reverse[::-1]

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def string_length_checker(list_of_words: list[str]) -> str:
    list_of_words.sort(key=len)
    return list_of_words[-1]

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1: str, str2: str) -> int:
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""Функція підрахунку суми парних чисел з списку"""
def even_sum(num_list: list[int]) -> int:
    return sum(num for num in num_list if num % 2 == 0)

# task 8
"""Функція, яка відбирає з списку елементи типу стрінг і записує в новий список"""
def string_filter_for_list(list_any_type_elem: list[any]) -> list[str]:
    only_str_list: list[str] = []
    for elem in list_any_type_elem:
        if isinstance(elem, str):
            only_str_list.append(elem)
    return only_str_list

# task 9
"""Функція підрахунку унікальних символів в строці"""
def uniq_char_counter(any_string: str) -> int:
    return len(set(any_string))

# task 10
"""Функція, що "зачищає" строку від спецсимволів і перевіряє чи є вона поліндромом"""
def is_palindrome(dirty_str: str) -> bool:
    cleaned_str: str = ''.join(char.lower() for char in dirty_str if char.isalnum())
    return cleaned_str == cleaned_str[::-1]

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
"""upd26.04"""