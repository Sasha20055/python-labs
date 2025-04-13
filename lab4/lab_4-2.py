import os

def process_series(input_file='numbers.txt', output_file='series_lengths.txt', create_example=False):

    if not os.path.exists(input_file):
        with open(input_file, 'w') as f:
            if create_example:
                f.write("1 5 5 5 4 4 5")  # Пример данных
        print(f"Файл {input_file} не найден. Создан новый файл.")


    try:
        with open(input_file, 'r') as f:
            data = f.read().strip()
    except FileNotFoundError:
        print("Ошибка: Файл не найден, даже после попытки создания.")
        return


    if not data:
        with open(output_file, 'w') as f:
            pass
        print(f"Файл {input_file} пуст. Создан пустой {output_file}.")
        return


    try:
        numbers = list(map(int, data.split()))
    except ValueError:
        print("Ошибка: Файл содержит нечисловые данные.")
        return


    series = []
    if numbers:
        current_num = numbers[0]
        count = 1
        for num in numbers[1:]:
            if num == current_num:
                count += 1
            else:
                series.append(count)
                current_num = num
                count = 1
        series.append(count)


    with open(output_file, 'w') as f:
        if series:
            f.write(', '.join(map(str, series)))
        else:
            pass

    print(f"Результат записан в {output_file}")

process_series(create_example=True)