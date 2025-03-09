# task 17
def elements_between_first_last_max(arr):
    if not arr:
        return []

    max_val = max(arr)
    first_idx = arr.index(max_val)
    last_idx = len(arr) - 1 - arr[::-1].index(max_val)

    return arr[first_idx + 1:last_idx] if first_idx < last_idx else []

arr = [5, 8, 3, 8, 4]
result = elements_between_first_last_max(arr)
print("Элементы между первым и последним максимумами:", result)

# task 18

def min_even_element(arr):
    even_elements = [x for x in arr if x % 2 == 0]
    return min(even_elements) if even_elements else None

arr = [5, 3, 8, 2, 7]
result = min_even_element(arr)
print("Минимальный четный элемент:", result)

# task 19

def prime_factors(n: int) -> list:
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

    return factors

n = int(input("Введите число: "))
result = prime_factors(n)
print(f"Простые делители числа {n}:", result)

