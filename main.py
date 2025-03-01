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

# task 7

def count_consonants_vowels_diff(s):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    v = sum(1 for c in s if c in vowels)
    c = sum(1 for c in s if c in consonants)
    return c - v

def sort_by_consonant_vowel_diff(strings):
    return sorted(strings, key=lambda x: count_consonants_vowels_diff(x))

strings = ["hello", "world", "python", "ai"]
sorted_strings = sort_by_consonant_vowel_diff(strings)
print("Сортировка по разнице согласных-гласных:")
for s in sorted_strings:
    print(s)

# task 8

reference_freq = {
    'e': 0.127, 't': 0.091, 'a': 0.082, 'o': 0.075, 'i': 0.070,
    'n': 0.067, 's': 0.063, 'h': 0.061, 'r': 0.060, 'd': 0.043
}

def calculate_squared_deviation(s):
    from collections import Counter
    cnt = Counter(s.lower())
    if not cnt:
        return 0
    most_common = cnt.most_common(1)[0]
    char = most_common[0]
    str_freq = most_common[1] / len(s)
    ref_freq = reference_freq.get(char.lower(), 0)
    return (str_freq - ref_freq) ** 2

def sort_by_freq_deviation(strings):
    return sorted(strings, key=lambda x: calculate_squared_deviation(x))

strings = ["hello", "world", "python", "ai"]
sorted_strings = sort_by_freq_deviation(strings)
print("Сортировка по отклонению частоты символа:")
for s in sorted_strings:
    print(s)

# task 9

def count_vc_cv_diff(s):
    vowels = set("aeiouAEIOU")
    vc, cv = 0, 0
    for i in range(len(s)-1):
        pair = s[i:i+2]
        first_vowel = pair[0] in vowels
        second_vowel = pair[1] in vowels
        if first_vowel and not second_vowel:
            vc += 1
        elif not first_vowel and second_vowel:
            cv += 1
    return vc - cv

def sort_by_vc_cv_diff(strings):
    return sorted(strings, key=lambda x: count_vc_cv_diff(x))

strings = ["hello", "world", "python", "ai"]
sorted_strings = sort_by_vc_cv_diff(strings)
print("Сортировка по разнице VC-CV:")
for s in sorted_strings:
    print(s)

# task 10

def max_triple_avg(s):
    max_avg = 0
    for i in range(len(s)-2):
        triplet = s[i:i+3]
        avg = sum(ord(c) for c in triplet) / 3
        if avg > max_avg:
            max_avg = avg
    return max_avg

def sort_by_triple_avg_deviation(strings):
    if not strings:
        return []
    first_avg = max_triple_avg(strings[0])
    return sorted(strings, key=lambda x: (max_triple_avg(x) - first_avg)**2)

strings = ["hello", "world", "python", "ai"]
sorted_strings = sort_by_triple_avg_deviation(strings)
print("Сортировка по отклонению тройного ASCII:")
for s in sorted_strings:
    print(s)