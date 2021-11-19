print("задача №1")

my_file = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_text:
    for el in file_text:
        line = el.split()
        my_file.append((line[0], line[0].strip('"'), line[6]))
print(my_file)

