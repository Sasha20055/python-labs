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