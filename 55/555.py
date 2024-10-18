import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time:.6f} секунд")
        return result

    return wrapper


# Функция с использованием декоратора: вычисление суммы двух чисел a и b
@timer_decorator
def sum_two_numbers(a, b):
    result = a + b
    print(f"Сумма чисел {a} и {b} равна: {result}")
    return result


# Функция с использованием декоратора: чтение двух чисел из файла и запись результата
@timer_decorator
def read_write_file():
    # Предполагается, что файл input.txt уже существует и содержит два целых числа
    with open('input.txt', 'r') as file:
        a, b = map(int, file.readline().split())

    result = a + b

    with open('output.txt', 'w') as file:
        file.write(str(result))

    print(f"Результат вычисления записан в файл output.txt")
    return result


# Тестирование функций
if __name__ == "__main__":
    # Тест функции sum_two_numbers
    sum_two_numbers(3, 5)

    # Тест функции read_write_file
    read_write_file()
