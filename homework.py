# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
import inspect


def open_browser(safari, firefox):
    pass


def go_to_companyname_homepage(google, apple):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


def description_of_actions(func):
    arguments = str(inspect.signature(func)).replace("(", "").replace(")", "")
    description = func.__name__.replace("_", " ").capitalize(), arguments
    if len(arguments) > 0:
        print(*description, sep=': ')
    else:
        print(*description)


functions = open_browser, go_to_companyname_homepage, find_registration_button_on_login_page

for i in functions:
    description_of_actions(i)



