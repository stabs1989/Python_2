
print('задача_№1')

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

#d = 5
#b='{:0=2}'.format(d)
#print(b)




print('задача_№2')
my_list =['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#number_of_elements = len(my_list)
print('исходный список', my_list)

#print(number_of_elements)
#print(my_list[0].isdigit())
for el in my_list:
    if "1" in el or "2" in el or "3" in el or "4" in el or "5" in el or "6" in el or "7" in el or "8" in el or "9" in el or "0" in el:
        my_index =my_list.index(el)
        my_list.insert(my_index+1, '"')
    #if el.isdigit():
       # print(el)
#print(my_list)
new_list = my_list[::-1]
for el in new_list:
    if "1" in el or "2" in el or "3" in el or "4" in el or "5" in el or "6" in el or "7" in el or "8" in el or "9" in el or "0" in el:
        my_index =new_list.index(el)
        new_list.insert(my_index+1, '"')
        #print(my_index)
        #print(el)
my_list = new_list[::-1]
#print(my_list)
for el in my_list:
    if "+" in el:
        my_index_plus = my_list.index(el)
for el in my_list:
    if "1" in el or "2" in el or "3" in el or "4" in el or "5" in el or "6" in el or "7" in el or "8" in el or "9" in el or "0" in el:
        my_index = my_list.index(el)
        b = int(el)
        my_list[my_index] = '{:0=2}'.format(b)
my_list[my_index] = '+' + my_list[my_index]
print('получившийся список', my_list)



