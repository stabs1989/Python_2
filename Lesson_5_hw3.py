print('Задача №3')


def my_gen():


    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]
    n = 0
    for el in tutors:
        a = klasses[n]
        #print(a)
        my_tuple = (el,a)
        n += 1
        yield my_tuple


a = my_gen()
for el in a:
    print(el)


