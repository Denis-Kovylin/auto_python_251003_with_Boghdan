import random
"""Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті"""

test_num_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_sum: int = 0
#
# for num in test_num_list:
#     if num % 2 == 0:
#         even_sum += num
# print(even_sum)

random_uniq_num_list: list[int] = random.sample(range(1, 101), 20)
print(f"За допомогою библиотеки 'random' був сворений лист: {random_uniq_num_list}")
even_sum: int = sum(num for num in random_uniq_num_list if num % 2 == 0)
print(f"Сума парних чисел вхідного списку дорівнює: {even_sum}")