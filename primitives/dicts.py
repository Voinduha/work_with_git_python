# Словари - это набор элементов представляющих собой ключ и значение

# Заводим словари

d = {"key": "value",
     123: "another",
     10: {"another": "first"},
    }

print(d["key"])
# выводит список ключей
print(list(d["key"]))

print(d.values())
# выводит список значений
print(list(d.values()))


# Функции словарей

print(d.items())
# выведет набор пар из словарика

d["first"] = "some string"
print(d)

value = d.pop("first")
# способ избавится от элементов в словаре

print(d.clear())
# удалит все значения в словаре