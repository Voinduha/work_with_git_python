

# Циклы! В питоне 2 основных цикла

# While

i = 0
while i < 10:
   print("something " + str(i))
   i += 1 # инкремент


#For # цикл for часто применяется в списках

l = ["first", "second", "third"]

for element in l:
    print(element)

# итерация по каждому символу
for element in "way to paython":
    print(element)

# распечатает каждую букву в строке
for element in "what the fuck":
    print(element, end="")

from primitives.dicts import  d

print("\n=========================")

for key, items in d.items():
    print(key, items, sep=" | ")

#  классический способ итерации

l = ["first", "second", "third"] 

for i in range(10):
    print(i)
