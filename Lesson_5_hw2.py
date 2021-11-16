


print('Задача №1')
#2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

def my_gen(i):

    mylist = []
    b = i
    for el in range (b):
        if el % 2 != 0:
            mylist.append(el)
    #print(mylist)
    return mylist
number = int(input("ввведите число"))
a = my_gen(number)

for el in a:
    print(el)
