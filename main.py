from math import gcd
import re

# task 1
def count_non_coprime_even_numbers(n: int) -> int:
    return sum(1 for i in range(2, n + 1, 2) if gcd(n, i) != 1)

def max_digit_not_divisible_by_three(n: int) -> int:
    return max((int(d) for d in str(n) if int(d) % 3 != 0), default=-1)

def product_of_max_non_coprime_and_digit(n: int) -> int:
    non_coprimes = [i for i in range(2, n) if gcd(n, i) != 1]
    if not non_coprimes:
        return 0
    max_non_coprime = max(non_coprimes)
    max_digit = max_digit_not_divisible_by_three(n)
    return max_non_coprime * max_digit if max_digit != -1 else 0

n = 36
print('Кол-во четных чисел, не взаимно простых с 36:', count_non_coprime_even_numbers(n))
print('Максимальная цифра числа, не делящаяся на 3:', max_digit_not_divisible_by_three(n))
print('Произведение максимального невзаимно простого числа и цифры: ', product_of_max_non_coprime_and_digit(n))

# task 2
def is_palindrome(s: str) -> bool:
    s_clean = s.replace(" ", "").lower()
    return s_clean == s_clean[::-1]

def count_words(s: str) -> int:
    return len(s.split())

def count_unique_digits(n: int) -> int:
    return len(set(str(n)))

test_string = "А роза упала на лапу Азора"
print(f"Строка '{test_string}' является палиндромом: {is_palindrome(test_string)}")

test_sentence = "Слово   тест    пример   "
print(f"Количество слов в строке: {count_words(test_sentence)}")

test_number = 123321
print(f"Количество различных цифр в числе {test_number}: {count_unique_digits(test_number)}")

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

# task 6

def sort_strings_by_word_count():
    strings = []
    print("Введите строки (для завершения введите пустую строку):")
    while True:
        s = input().strip()
        if not s:
            break
        strings.append(s)

    sorted_strings = sorted(strings, key=lambda x: len(x.split()))

    print("Отсортированный список строк по количеству слов:")
    for s in sorted_strings:
        print(s)

print("Упорядочивание строк по количеству слов:")
sort_strings_by_word_count()