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