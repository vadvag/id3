#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import fnmatch

# Этот кусок кода нам нужен пока мы не прошли тему Модули, потом будем прописывать свои модули по-человечески
import sys
path = os.path.normpath(sys.path[0])
class_dir = sys.path[0].replace(path.split(os.sep)[-1], "mp3_class") 
sys.path.append(class_dir)
import mp3
# ----

def find_all_mp3_in_current_dir(path):
    mp3_list = []

    for root, dirs, files in os.walk(path):
        if len(files) > 0:
            for file in files:
                if fnmatch.fnmatch(file, '*.mp3'): 
                    # Creat the list of objects MP3Format class
                    mp3_list.append(mp3.MP3Format(os.path.join(root, file))) 
    
    return mp3_list

""" How to use
import search_in_directory as sid
import os

for mp3_file in sid.find_all_mp3_in_current_dir('/Users/MacUser/Music'):
    print(mp3_file.full_path)
"""