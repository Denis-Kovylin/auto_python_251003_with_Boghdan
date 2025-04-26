# todo Develop a unittests [ python -m unittest discover -v *автоподхват тестов*  python -m unittest discover -s 013_lsn_unittest -p "test_*.py" -v ]


import unittest
from func_013 import sum_two_num, list_arithmetic_average, reverse_string_writer, even_sum, is_palindrome


class TestFunctions013(unittest.TestCase):
    """Клас для тестування функцій."""

    def test_sum_two_positive_number(self):
        """Тестуємо додавання двох додатних чисел."""
        self.assertEqual(sum_two_num(2, 3), 5)

    def test_sum_two_negative_numbers(self):
        """Тестуємо додавання двох від’ємних чисел."""
        self.assertEqual(sum_two_num(-5, -7), -12)

    def test_sum_two_float_numbers(self):
        """Тестуємо додавання дробових чисел."""
        self.assertEqual(sum_two_num(2.5, 3.1), 5.6)

    def test_list_average_normal(self):
        """Тестуємо середнє арифметичне звичайного списку."""
        self.assertAlmostEqual(list_arithmetic_average([1, 2, 3, 4]), 2.5)

    def test_list_average_empty(self):
        """Перевірка: порожній список викликає ValueError."""
        with self.assertRaises(ValueError):
            list_arithmetic_average([])

    def test_reverse_string_writer_positive(self):
        """Переворот звичайного рядка"""
        self.assertEqual(reverse_string_writer("hello"), "olleh")

    def test_revers_string_writer_empty(self):
        """Перевіряєм порожній рядок"""
        self.assertEqual(reverse_string_writer(""), "")

    def test_reverse_string_writer_space(self):
        """Перевіряєм символи і пробіли"""
        self.assertEqual(reverse_string_writer("a b!"), "!b a")

    def test_reverse_string_writer_unicod(self):
        """Перевіряєм кирилічні символи"""

    def test_even_sum_even(self):
        """Перевіряєм чьотні числа"""
        self.assertEqual(even_sum([2, 4, 6]), 12)

    def test_even_sum_odd(self):
        """Перевіряжм не чьотні"""
        self.assertEqual(even_sum([1, 3, 5]), 0)

    def test_even_sum_blend(self):
        """Перевіряєм змішаний набір чисел"""
        self.assertEqual(even_sum([1, 2, 3, 4, 5]), 6)

    def test_even_sum_empty(self):
        """Перевіряєм порожній список"""
        self.assertEqual(even_sum([]), 0)

    def test_even_sum_pos_and_nag(self):
        """Перевіряємо від'ємні і додатні числа"""
        self.assertEqual(even_sum([-2, -3, 4]), 2)

    def test_is_palindrome_positive(self):
        """Перевіряємо базовий поліндром"""
        self.assertEqual(is_palindrome("radar"), True)

    def test_is_palindrome_dirty(self):
        """Перевіряємо реакцію на пунктуацію"""
        self.assertEqual(is_palindrome("A man, a plan, a canal: Panama"), True)

    def test_is_palindrome_not(self):
        """Перевіряємо негативний кейс"""
        self.assertEqual(is_palindrome("hello"), False)

    def test_is_palindrome_spec_char(self):
        """Перевіряємо тільки спецсимволи"""
        self.assertEqual(is_palindrome("!!!"), True)

    def test_is_palindrome_empty(self):
        """Перевіряємо порожній рядок"""
        self.assertEqual(is_palindrome(""), True)


if __name__ == "__main__":
    unittest.main()
