def abbr(phrase):
    abbreviation = ""
    for current_word in phrase.split(): #разбиваем фразу, которую ввели, на каждое отдельное слово
        if current_word[0].isalpha(): # проверка, что слово начинается с буквы
            abbreviation += current_word[0].upper() #если начинается с буквы, то первую букву длеаем заглавной и добавляем к результату
    return abbreviation


# Пример
phrase = "Kva-kva meow gav"
print(abbr(phrase))
