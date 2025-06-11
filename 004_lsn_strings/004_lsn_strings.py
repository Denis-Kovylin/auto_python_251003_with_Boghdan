gap: str = "\n"
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer_task_1: str = adwentures_of_tom_sawer
adwentures_of_tom_sawer_task_1: str = adwentures_of_tom_sawer_task_1.replace("\n", " ")
print(adwentures_of_tom_sawer_task_1, gap)
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer_task_2: str = adwentures_of_tom_sawer_task_1
adwentures_of_tom_sawer_task_2: str = adwentures_of_tom_sawer_task_2.replace("....", " ")
print(adwentures_of_tom_sawer_task_2, gap)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_task_3: str = adwentures_of_tom_sawer_task_2
adwentures_of_tom_sawer_task_3: str = adwentures_of_tom_sawer_task_3.replace("   ", " ")
print(adwentures_of_tom_sawer_task_3, gap)
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
adwentures_of_tom_sawer_task_4: str = adwentures_of_tom_sawer_task_3
print(adwentures_of_tom_sawer_task_4.count("h"), gap)
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
adwentures_of_tom_sawer_task_5: str = adwentures_of_tom_sawer_task_4
cap_counter: int = 0
punct = ",.!?\"()“”‘’—…"
cleaned_words = []
for word in adwentures_of_tom_sawer_task_5:
    cleaned = word.strip(punct)
    cleaned_words.append(cleaned)

for elem in cleaned_words:
    if elem and elem[0].istitle():
        cap_counter += 1
print(f"Слов, що починаються з великої літери: {cap_counter}{gap}")
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
adwentures_of_tom_sawer_task_6: str = adwentures_of_tom_sawer_task_5
f_index = adwentures_of_tom_sawer_task_6.find("Tom")
print(
    f"Вдруге строка 'Том' зустрічається починаючи з: {adwentures_of_tom_sawer_task_6.find("Tom", f_index + 1)} символа.{gap}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_task_7: str = adwentures_of_tom_sawer_task_6
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_task_7.split(". ")
print(adwentures_of_tom_sawer_sentences, gap)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_task_8: str = adwentures_of_tom_sawer_sentences
print(adwentures_of_tom_sawer_sentences[3].lower(), gap)
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
adwentures_of_tom_sawer_task_9: str = adwentures_of_tom_sawer_task_8
for index, sentence in enumerate(adwentures_of_tom_sawer_task_9):
    clean_sent = sentence.strip()
    if clean_sent.startswith("By the time"):
        print(f"Речення, яке починається з 'By the time', має індекс: {index}{gap}")
        break
    else:
        pass
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_task_10: str = adwentures_of_tom_sawer_sentences
print(f"Останнє речення складаеться з {len(adwentures_of_tom_sawer_task_10[-2].strip().split(" "))} слів.")

# UPD
