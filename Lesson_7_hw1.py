print("задача №1")

import os
my_list = ['setting','mainapp','adminapp','authapp']
Root = os.path.dirname(__file__)
print(Root)
if not os.path.isdir("my_project"):
     os.mkdir("my_project")
os.chdir("my_project")
print(os.getcwd())
for el in my_list:
    os.mkdir(el)
os.chdir(Root)
print(os.getcwd())
