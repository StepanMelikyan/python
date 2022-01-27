

def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""

    for q in range(len(list_in)):
        list_in[q] = list_in[q].split()
        list_in[q] = f"Привет, {list[q][-1].title()}!"


    return list_in


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
results = convert_name_extract(list_in)
print(result)