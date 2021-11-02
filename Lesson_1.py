#print('задача_№1')

#duration = input('введите время в секундах')


print('задача_№2')

my_list = [13, 121, 3, 7, 49]
for el in my_list:
    my_index = my_list.index(el)
    number = el**3
    my_list[my_index] = number
    #print(number)
#print(my_list)
full_sum = 0
for el in my_list:
    my_index = my_list.index(el)
    sum = 0
    while (el != 0):
        sum = sum + el % 10
        el = el // 10
    print("Сумма цифр числа равна: ", sum)
    if not sum % 7:
        print('делится')
        full_sum = full_sum + my_list[my_index]
print('сумма цифр, которые делятся на 7 =', full_sum)



print('задача_№3')

my_number = 1
while my_number <= 100:
    number = int(str(my_number)[-1])
    #print(number)
    if '1'in str(number):
        print(my_number,'процент')
    elif '2'in str(number) or '3'in str(number) or '4'in str(number):
        print(my_number, 'процента')
    else:
        print(my_number, 'процентов')
    my_number += 1
