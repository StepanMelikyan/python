# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    my_list = []
    my_list.append(arg1)
    my_list.append(arg2)
    my_list.append(arg3)
    x = min(my_list, key=lambda i:int(i))
    my_list.remove(x)
    print(sum(my_list))
my_func(arg1=2, arg3=5, arg2=7)