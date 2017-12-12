#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import os
import sys
import fnmatch
import mp3


def find_all_mp3_in_current_dir(path):
    mp3_list = []
    
    for root, dirs, files in os.walk(path):
        if len(files) > 0:
            for file in files:
                if fnmatch.fnmatch(file, '*.mp3'):
                    # Creat the list of objects MP3Format class
                    mp3_list.append(mp3.MP3Format('{}{}{}'.format(root, os.sep, file)))
    
    return mp3_list


# Функция выводящая список Директорий/Папок из объекта mp3.MP3Format
# def get_folders_from_list():
