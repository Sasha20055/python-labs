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