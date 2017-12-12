#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import sys
import os

# Этот кусок кода нам нужен пока мы не прошли тему Модули, потом будем прописывать свои модули по-человечески
import settings
import search_in_directory as sid

try:
    # предполагается что на данном этапе наше приложение получает один аргумент коммандной строки
    # протестировано: python3.6 main.py /Users/MacUser/Music
    # В результате выдает список всех mp3 файлов в заданной директории с версиями и тегами
    
    if os.path.exists(os.path.dirname(sys.argv[1])):
        my_mp3 = sid.find_all_mp3_in_current_dir(sys.argv[1])
        
        for mp3_file in my_mp3:
            print('mp3 version {}: {}'.format(mp3_file.meta_data['version'], mp3_file.full_path))

    else:
        print("Path [{}] does not exist".format(sys.argv[1]))

# если файл будет запускаться не с коммандной строки и/или без параметров
except IndexError:
    print('Path parameter is empty, please restart the application and set the Path to directory with music')
