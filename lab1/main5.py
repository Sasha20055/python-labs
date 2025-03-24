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

# task 11

def get_indices_sorted_desc(arr):
    indexed = sorted(enumerate(arr), key=lambda x: -x[1])
    return [i for i, _ in indexed]

arr = [3, 1, 4, 2]
indices = get_indices_sorted_desc(arr)
print("Индексы в порядке убывания элементов:", indices)  # [2, 0, 3, 1]