# task 12

def elements_between_first_second_max(arr):
    if len(arr) < 2:
        return []
    max1 = max(arr)
    idx1 = arr.index(max1)
    max2 = -float('inf')
    for i, num in enumerate(arr):
        if num > max2 and (i != idx1 or num != max1):
            max2 = num
    if max2 == max1:
        return []
    idx2 = arr.index(max2, idx1 + 1) if max2 in arr[idx1 + 1:] else arr.index(max2)
    start = min(idx1, idx2) + 1
    end = max(idx1, idx2)
    return arr[start:end]

arr = [5, 2, 8, 3, 8, 4]
result = elements_between_first_second_max(arr)
print("Элементы между первым и вторым максимумами:", result)

# task 13
def elements_between_first_last_max(arr):
    if not arr:
        return []
    max_val = max(arr)
    first_idx = arr.index(max_val)
    last_idx = len(arr) - 1 - arr[::-1].index(max_val)
    return arr[first_idx + 1 : last_idx]

arr = [5, 8, 3, 8, 4]
result = elements_between_first_last_max(arr)
print("Элементы между первым и последним максимумами:", result)

# task 15

def indices_descending(arr):
    return sorted(range(len(arr)), key=lambda i: arr[i], reverse=True)

arr = [10, 3, 5, 8, 2]
result = indices_descending(arr)
print("Индексы элементов в порядке убывания значений:", result)

# task 14

def min_even_element(arr):
    even_elements = [x for x in arr if x % 2 == 0]
    return min(even_elements) if even_elements else None

arr = [5, 3, 8, 2, 7]
result = min_even_element(arr)
print("Минимальный четный элемент:", result)

# task 16

def prime_factors(n):
    factors = []
    if n < 2:
        return factors
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 1:
        factors.append(n)
    return sorted(factors)

n = 28
factors = prime_factors(n)
print(f"Простые делители числа {n}:", factors)

