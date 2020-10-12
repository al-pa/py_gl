
class MyClass:
    def __new__(cls, *args, **kwargs):
        arguments = list(args)
        if 'A' in arguments:
            arguments.remove('A')
        if 'B' in arguments:
            arguments.remove('B')

        if len(arguments):
            return object()
        else:
            return object.__new__(cls)


mc1 = MyClass("A")   # --> MyClass obj
mc2 = MyClass("A", "B")       # --> MyClass obj
not_mc1 = MyClass("C")    # --> object
not_mc2 = MyClass("B", "C")    # --> object

"""
Нужно написать класс который будет создавать объект этого же класса если в конструкторе будет присутствовать
 str ""А"" или ""В"" но не что либо другое. 
Если в конструктор передается "С" или с "В" также передается "С" то должен быть создан простой базовый обьект (object).

Пример выполнения:
mc1 = MyClass("A")   --> MyClass obj
mc2 = MyClass("A","B")        --> MyClass obj
not_mc1 = MyClass("C")     --> object
not_mc2 = MyClass("B","C")     --> object
"""