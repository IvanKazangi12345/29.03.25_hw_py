import time

def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                print(f"Функция {func.__name__} вызвана слишком много раз!")
                return
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limit_calls(3)
def test_function():
    print("Функция выполнена")

test_function()
test_function()
test_function()
test_function()
test_function()

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Время выполнения {func.__name__}: {time.time() - start_time:.4f} сек")
        return result
    return wrapper

@time_it
def slow_function():
    time.sleep(2)
    print("Функция завершила работу")

slow_function()

filename = input("Введите имя файла: ")
search_word = input("Введите слово для поиска: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        count = file.read().lower().split().count(search_word.lower())
    print(f"Слово '{search_word}' встречается {count} раз(а) в файле {filename}.")
except FileNotFoundError:
    print("Файл не найден.")

try:
    with open('unsorted.txt', 'r', encoding='utf-8') as infile:
        sorted_words = sorted(infile.read().splitlines())
    with open('sorted.txt', 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(sorted_words))
    print("Файл отсортирован и сохранён как sorted.txt")
except FileNotFoundError:
    print("Файл unsorted.txt не найден.")
