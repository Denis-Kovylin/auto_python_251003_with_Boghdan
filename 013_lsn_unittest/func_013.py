# --------------------------------------------------------------------

def sum_two_num(a: int | float, b: int | float) -> float:
    """
    Функція обчислює суму двох чисел.

    :param a: Перше число (ціле або дробове)
    :param b: Друге число (ціле або дробове)
    :return: Сума a і b
    """
    return a + b

# --------------------------------------------------------------------

def list_arithmetic_average(numbers: list[float]) -> float:
    """
    Функція обчислює середнє арифметичне списку чисел.

    :param numbers: Список чисел (float або int)
    :return: Середнє арифметичне чисел
    """
    if not numbers:
        raise ValueError("Список не повинен бути порожнім")
    return sum(numbers) / len(numbers)

# --------------------------------------------------------------------

def reverse_string_writer(string_to_reverse: str) -> str:
    """
    Функція повертає рядок у зворотному порядку.

    :param string_to_reverse: Рядок, який потрібно перевернути
    :return: Перевернутий рядок
    """
    return string_to_reverse[::-1]

# --------------------------------------------------------------------

def even_sum(num_list: list[int]) -> int:
    """
    Функція обчислює суму парних чисел у списку.

    :param num_list: Список цілих чисел
    :return: Сума парних чисел
    """
    return sum(num for num in num_list if num % 2 == 0)

# --------------------------------------------------------------------

def is_palindrome(dirty_str: str) -> bool:
    """
    Функція перевіряє, чи є рядок паліндромом,
    ігноруючи пробіли, спецсимволи та регістр.

    :param dirty_str: Вхідний рядок для перевірки
    :return: True, якщо рядок паліндром, інакше False
    """
    cleaned_str = ''.join(char.lower() for char in dirty_str if char.isalnum())
    return cleaned_str == cleaned_str[::-1]

# --------------------------------------------------------------------

