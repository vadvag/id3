#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import sys
import os

# please set here the names of directories that contains your modules
id3_modules = ( 'search',
            'mp3_class'
            )

def set_path_vars():
    for item in id3_modules:
        sys.path.append(os.path.join(sys.path[0], item))
