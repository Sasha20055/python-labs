from math import gcd

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