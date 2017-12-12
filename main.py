#!/usr/bin/env python3.6

import sys

import search.search_in_directory as sid

try:
    # предполагается что на данном этапе наше приложение получает один аргумент коммандной строки
    # протестировано: python3.6 main.py /Users/MacUser/Music
    # В результате выдает список всех mp3 файлов в заданной директории с версиями и тегами
    
    my_mp3 = sid.find_all_mp3_in_current_dir(sys.argv[1])
        
    for mp3_file in my_mp3:
        print('mp3 version {}: {}'.format(mp3_file.meta_data['version'], mp3_file.full_path))


# если файл будет запускаться не с коммандной строки и/или без параметров
except IndexError:
    print('Path parameter is empty, please restart the application and set the Path to directory with music')

except FileNotFoundError:
    print("Path [{}] does not exist".format(sys.argv[1]))
