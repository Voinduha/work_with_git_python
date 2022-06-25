

# Boolean - логический тип данных

t = True
f = False

# if/elif/else

if True:
    print("It's true!")

if not False:
    print("It's false!")

if True or False:
    print("something")

b = True or False
if b:
    print("something")

if 0:
    print("zero")

if "":
    print("zero")

if None: # еще один тип данных
    print("None")


# делаем рандомный выбор
import random

b = random.randint(0, 1)

if b:
    print("Got it")
else:
    print("Nope")

# делаем еще один спискок рандомных значений
b = random.randint(0, 2)

if b == 0: # == оператор сравнения
    print("Zero")
elif b == 1:
    print("One")
else:
    print("Something else")

# делаем еще один спискок рандомных значений
b = random.randint(0, 3)

if b == 0:
    print("Zero")
elif b == 1:
    print("One")
elif b == 2:
    print("Two")

else:
    print("Something else")




