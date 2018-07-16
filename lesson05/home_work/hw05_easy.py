# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

i = 1
while i < 10:
    dir_new = "dir_" + str(i)
    dir_path = os.path.join(os.getcwd(), dir_new)
    try:
        os.makedir(dir_path)
    except FileExistsError:
    print("File exists")
    i += 1

remove = os.listdir(path = ".")
for dir_new in remove:
    os.rmdir(dir_new)
#я его не проверяла, боюсь стереть себе весь диск =)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import sys
import os

dir_list = os.listdir(path=".")
print(dir_list)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

new_file = open('hw_5.py', 'w')
shutil.copy(r'hw_5.py', r'hw_5_copy.py')
new_file.close()

