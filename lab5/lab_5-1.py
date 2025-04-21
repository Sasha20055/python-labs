import re

def is_credit_card(card_number):
    pattern = r'^(\d{4}([- ])\d{4}\2\d{4}\2\d{4}|\d{16})$'
    return re.fullmatch(pattern, card_number) is not None

def validate_credit_card(card_number):
    if not isinstance(card_number, str):
        raise TypeError("Аргумент должен быть строкой")
    if not is_credit_card(card_number):
        raise ValueError("Неверный формат номера кредитной карты")
    return card_number

def main():
    print("Проверка номера кредитной карты")
    print("Допустимые форматы:")
    print("- 16 цифр подряд (например, 1234567812345678)")
    print("- 4 группы по 4 цифры, разделённые дефисами или пробелами (например, 1234-5678-9012-3456 или 1234 5678 9012 3456)")

    while True:
        user_input = input("\nВведите номер карты (или 'exit' для выхода): ").strip()

        if user_input.lower() == 'exit':
            print("Выход из программы.")
            break

        try:
            validated_card = validate_credit_card(user_input)
            print(f"✅ Валидный номер карты: {validated_card}")
            print(f"Результат is_credit_card(): {is_credit_card(user_input)}")
        except ValueError as e:
            print(f"❌ Ошибка: {e}")
        except TypeError as e:
            print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()