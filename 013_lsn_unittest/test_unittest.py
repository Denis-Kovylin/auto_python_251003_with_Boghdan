# todo Develop a unittests [ python -m unittest discover -v *автоподхват тестов*  python -m unittest discover -s 013_lsn_unittest -p "test_*.py" -v ]


import unittest
from func_013 import sum_two_num, list_arithmetic_average, reverse_string_writer, even_sum, is_palindrome


class TestSumTwoNum(unittest.TestCase):
    """Тести для функції sum_two_num"""

    def test_two_positive(self):
        """Перевірка: сума двох додатних чисел"""
        self.assertEqual(sum_two_num(2, 3), 5)

    def test_two_negative(self):
        """Перевірка: сума двох від’ємних чисел"""
        self.assertEqual(sum_two_num(-5, -7), -12)

    def test_two_floats(self):
        """Перевірка: сума двох дробових чисел"""
        self.assertAlmostEqual(sum_two_num(2.5, 3.1), 5.6)


class TestListArithmeticAverage(unittest.TestCase):
    """Тести для функції list_arithmetic_average"""

    def test_average_normal(self):
        """Перевірка: середнє арифметичне звичайного списку"""
        self.assertAlmostEqual(list_arithmetic_average([1, 2, 3, 4]), 2.5)

    def test_average_empty(self):
        """Перевірка: виклик ValueError для порожнього списку"""
        with self.assertRaises(ValueError):
            list_arithmetic_average([])


class TestReverseStringWriter(unittest.TestCase):
    """Тести для функції reverse_string_writer"""

    def test_reverse_normal(self):
        """Перевірка: звичайний рядок перевертається"""
        self.assertEqual(reverse_string_writer("hello"), "olleh")

    def test_reverse_empty(self):
        """Перевірка: порожній рядок повертає порожній рядок"""
        self.assertEqual(reverse_string_writer(""), "")

    def test_reverse_space(self):
        """Перевірка: рядок зі спецсимволами та пробілами"""
        self.assertEqual(reverse_string_writer("a b!"), "!b a")

    def test_reverse_unicode(self):
        """Перевірка: кириличні символи перевертаються"""
        self.assertEqual(reverse_string_writer("абвг"), "гвба")


class TestEvenSum(unittest.TestCase):
    """Тести для функції even_sum"""

    def test_even_numbers(self):
        """Перевірка: сума лише парних чисел"""
        self.assertEqual(even_sum([2, 4, 6]), 12)

    def test_odd_numbers(self):
        """Перевірка: список лише з непарних чисел повертає 0"""
        self.assertEqual(even_sum([1, 3, 5]), 0)

    def test_mixed(self):
        """Перевірка: змішаний список парних та непарних чисел"""
        self.assertEqual(even_sum([1, 2, 3, 4, 5]), 6)

    def test_empty(self):
        """Перевірка: порожній список повертає 0"""
        self.assertEqual(even_sum([]), 0)

    def test_negative_and_positive(self):
        """Перевірка: сума парних серед від’ємних і додатних чисел"""
        self.assertEqual(even_sum([-2, -3, 4]), 2)


class TestIsPalindrome(unittest.TestCase):
    """Тести для функції is_palindrome"""

    def test_plain(self):
        """Перевірка: простий паліндром"""
        self.assertTrue(is_palindrome("radar"))

    def test_dirty(self):
        """Перевірка: паліндром з пробілами та пунктуацією"""
        self.assertTrue(
            is_palindrome("A man, a plan, a canal: Panama")
        )

    def test_not_palindrome(self):
        """Перевірка: непаліндром повертає False"""
        self.assertFalse(is_palindrome("hello"))

    def test_only_special(self):
        """Перевірка: рядок тільки зі спецсимволів вважається паліндромом"""
        self.assertTrue(is_palindrome("!!!"))

    def test_empty_string(self):
        """Перевірка: порожній рядок вважається паліндромом"""
        self.assertTrue(is_palindrome(""))


if __name__ == "__main__":
    unittest.main()
