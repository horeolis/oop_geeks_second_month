# # декораторы и venv 
# def greeting_decorator(func):
#     def wrapper(name):
#         print(f"ку {name} ")
#         func(name)

#     return wrapper

# # @greeting_decorator
# def hello(name):
#     print(f"Приветствую тебя, {name}!")


# hello("Петя")

# отличие обычного декоратора от декоратора с аргументами в том, что декоратор с аргументами принимает дополнительные параметры, которые могут быть использованы внутри функции-обертки.

# def class_decorator(clc):
#     class Wrapper:
#         print("я обернул класс")
#     return Wrapper

# @class_decorator
# class MyClass:    

#     def __init__(self):
#         print("я класс")


# test = MyClass()


