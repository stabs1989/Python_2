print("задача_№1")
# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
def num_translate(el):
    my_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': "пять", 'six': "шесть", 'seven': "семь",
         'eight': "восемь", 'nine': "девять", 'ten': "десять"}
    return my_dict.get(el)

#word = input("введите число на английском")
word = 'six'
print(num_translate(word))



print("задача_№2")
#(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
#начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
#>>> num_translate_adv("One")
#"Один"
#>>> num_translate_adv("two")
#"два"
#el_t = 'two'
#print(el_t.istitle())
def num_translate(el):
    my_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': "пять", 'six': "шесть",
               'seven': "семь",
               'eight': "восемь", 'nine': "девять", 'ten': "десять"}
    if el.istitle():
        print('с большой буквы')
        ele = el.lower()
        print(el)
        word_title = my_dict[ele]
        return word_title.title()
    else:
        print('с маленькой буквы')
        return my_dict[el]
word = 'Two'
#word = input("введите число на английском")
print(num_translate(word))



print("задача_№3")
#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в
# котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
#>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
#{
#    "И": ["Иван", "Илья"],
#    "М": ["Мария"], "П": ["Петр"]
#}
#Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?
from pprint import pprint
def thesaurus(*args):
    my_dict = {}
    my_list = list(args)
    my_list.sort()
    for el in my_list:
        number_one = el[0]
        if number_one in my_dict:
            #print(number_one)
            my_dict = {key: [value] for key, value in my_dict.items()}
            my_dict[number_one].append(el)
        else:
            my_dict[number_one] = el

    print("{" "\n" + "\n".join("{!r}: {!r},".format(k, v) for k, v in my_dict.items()) + "\n" "}")
    #(my_list)
thesaurus("Иван", "Мария", "Петр", "Илья")
#thesaurus("Афанасий", "Валерий", "Виктор", "Юрий")



print("задача_№4")

def et_jokes(number):
    import random
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_elements = len(nouns)
    #print(list_elements)
    list_elements = list_elements - 1
    n = 0
    my_list = []
    while n < number:
        my_list.append(nouns[random.randint(0, list_elements)] + ' ' + adverbs[random.randint(0, list_elements)]+ ' ' + adjectives[random.randint(0, list_elements)])
        n += 1
    print(my_list)
et_jokes(3)

