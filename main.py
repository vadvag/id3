#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

# Этот кусок кода нам нужен пока мы не прошли тему Модули, потом будем прописывать свои модули по-человечески
module_dir = os.path.join(sys.path[0], "search") 
sys.path.append(module_dir)
module_dir = os.path.join(sys.path[0], "mp3_class") 
sys.path.append(module_dir)
import search_in_directory as sid
# ----

# Временная мера на тот случае если файл будет запускаться не с коммандной строки и без параметров
if len(sys.argv) == 1:
    exit(1)

# предполагается что на данном этапе наше приложение получает один аргумент коммандной строки
# протестировано:  python3.6 main.py /Users/MacUser/Music
# В результате выдает список всех mp3 файлов в заданной директории
if os.path.exists(os.path.dirname(sys.argv[1])):
    for mp3_file in sid.find_all_mp3_in_current_dir(sys.argv[1]):
        print(mp3_file.full_path)

else:
    print("Not OK")
