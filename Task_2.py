def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    result = 0
    for i in dataset:
        sum = 0

        while (i != 0):
            q = i % 10
            i = i // 10
            sum = sum + q

        if sum % 7 == 0:
            result = result + 1

    return result





def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    result = 0
    for g in dataset:
        sum = 0
        g = g + 17
        while (g != 0):
            q = g % 10
            g = g // 10
            sum = sum + g

        if sum % 7 == 0:
            result = result + sum

    return result



my_list = []
for x in range(1, 1001, 2):
    m = x ** 3
    my_list.append(m)

print(sum_list_1(my_list))
print(sum_list_2(my_list))