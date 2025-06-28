def count_cifra(chislo):
    cifra_counts = {}  #создаём словарь, в котором хранится количество каждой цифпы

    for cifra in str(chislo):  # превращаем чсило в строку и проходимcя по каждой цифре/символу в строке
        if cifra in cifra_counts: # чекаем есть ли эта цифра уже в словаре
            cifra_counts[cifra] += 1  # если цифра есть, увеличиваем счётчик
        else:
            cifra_counts[cifra] = 1   # если нет, то добавляем с начальным значением один

    return cifra_counts
#Пример
number = 567890876567890
print(count_cifra(number))
