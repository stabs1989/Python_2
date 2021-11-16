print('Задача №1')
#Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:


def my_generator(i):


    for el in range (i):
        if el % 2 != 0:
            yield el

n = int(input('введите число'))
a = my_generator(n)
for el in a:
    print(el)
print(type(my_generator(n)))


