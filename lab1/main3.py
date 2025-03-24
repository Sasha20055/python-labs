from math import gcd
import re

# task 3

text = "31 февраля 2007, 12 марта 2020, 29 февраля 2016"
dates = re.findall(r"\b\d{1,2} (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря) \d{4}\b", text)
print(dates)

# task 4

def count_numbers_less_than_five(s: str) -> int:
    current = ''
    count = 0
    for char in s:
        if char.isdigit():
            current += char
        else:
            if current:
                num = int(current)
                if num < 5:
                    count += 1
                current = ''
    if current:
        num = int(current)
        if num < 5:
            count += 1
    return count

def find_unused_latin_chars(s: str) -> list:
    used = set(s.lower())
    all_latin = set('abcdefghijklmnopqrstuvwxyz')
    unused = sorted(all_latin - used)
    return unused

def count_digits_greater_than_five(s: str) -> int:
    return sum(1 for char in s if char.isdigit() and int(char) > 5)

test_str1 = "a1b22c003d9e40"
print(f"Количество чисел < 5: {count_numbers_less_than_five(test_str1)}")

test_str2 = "Hello Python!"
print(f"Неиспользуемые символы: {find_unused_latin_chars(test_str2)}")

test_str3 = "abc6 78x5y9"
print(f"Цифр > 5: {count_digits_greater_than_five(test_str3)}")

# task 5

def read_and_sort_strings():
    strings = []
    print("Введите строки (для завершения введите пустую строку):")
    while True:
        s = input().strip()
        if not s:
            break
        strings.append(s)

    sorted_strings = sorted(strings, key=lambda x: len(x))

    print("Отсортированный список строк по длине:")
    for s in sorted_strings:
        print(s)

print("Сортировка строк по длине")
read_and_sort_strings()