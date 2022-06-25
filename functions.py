# Объявляем функции!

def func():
    print(1)


func()


# еще одна функция

def func_arg(arg1, arg2, arg3="third"):
    print(arg1, arg2, arg3)


func_arg("hello!", 123, "321")


# функции могут возвращать значения

def upper_string(string: str):
    return string.upper()


s = (upper_string("some lowercase"))

print((upper_string("some lowercase")))


# Переменное количество аргументов

def print_all_arguments(end, *args):
    for arg in args:
        print(arg, end=end)


print_all_arguments("", 2, 3, 4, 5, 6, 7, 8)


def print_pairs(**kwargs):
    pass


print_pairs(1234, key="value", some="another", etc=123)