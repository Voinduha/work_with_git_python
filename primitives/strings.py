

# Учимся писать строки!
import logging

s = "I am 'teapot!'"
s = 'I am "teapot"!'
s = """'I am "teapot"!'"""
s = '''I am "teapot"!'''
multiline_string = """first 
second
third"""
# в одинарных кавычках мы пишем строки в одну строчку
# в двойных и тройных кавычках мы можем написать несколько строк
# удобно писать по умолчанию строки в двойных кавычках

print(multiline_string)

# \n помогает экранировать символ внутри строки (перевод каретки на новую строку)

a = "I am \"teapot!\""

multiline_string = "first\n" \
    "second\n" \
    "third"

print(multiline_string)

print(r"this is my stri\ng")
# r (raw) перед строкой экранирует всю строку


# Индексы!

s = "abcdefg"
print(s[0])
print(s[1])
print(s[2])


# в питоне индексация происходит с 0 (первый символ нулевой)


# И слайсы!


print(s[0:5])
# берем диапазон символов с 0 по 5й
print(s[0:-1])
print(s[:-1])
# строка всех символов, кроме последнего

print(s[0:-1:2])
# шаг с которым мы движемся по списку символов (мы будем брать каждый второй символ)

print(s[::-1])
# реверс строки (тоесть мы напечатаем строку с права на лево или наоборот

# Оперируем!

print("hello, world!".replace("hello", "bye"))
print("hello, world!".replace("o", "of"))
# заменяет  hello на by
# заменит все вхождения где буква о на Ноль

print("hello, world!".split())
# разделит строку на несколько объектов

assert "hello, world!".startswith("hello")

# вернет true либо false, проверит начало строки на правдивость

assert "hello, world!".endswith("world!")

# вернет true либо false, проверит конец строки на правдивость

print("hello, world!".capitalize())

# делает первый символ большим

print("HELLO, WORLD!".lower())

# делает всю строку маленькими буквами

print("HELLO, WORLD!".title())

# делает в обоих словах заглавные буквы


# Форматирование! (построение строк из других строк)

first = "first"
second = "second"
third = "third"

print(" fa " " fa " " fa ")


first = "first"
second = "second"
third = "third"

print(first + " " + second + " " + third)
# Склеивание трех переменных в одну строку

print(f"{first} {second} {third}")
# тоже склеивание через f

print(f"{first} {second} {third} {2 + 7}")
# тоже склеивание, но с формулой внутри строки

print(f"{first} {second} {third.title()} {2 + 7}")
# тоже склеивание, но с формулой внутри строки и третьей переменной с большой буквы

print("{} {} {}".format(first, second, third))
# тоже самое, но старый способ

print(f"{first} {second} {third} {100}")
# или так {0} в фигурных скобках индекс переменной, которую мы передаем

print("%s %s %s" % (first, second, third.title()))
# тоже самое, но еще один способ (%s означает что туда можно втсавить переменную) применяется редко

s = "100"
assert s.isdigit()
print(100 + int(s))
# проверяем, что в переменной число, а не текст например




