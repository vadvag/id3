#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import os
import sys
import struct


class MP3Format:
    """ Class-description of mp3 file
        - file name
        - file path
        - ID3-tags
    """
    
    def __init__(self, path):
        self.full_path = path
        self.meta_data = {}

        # define variables for File Name and Path to directory that contains this file
        if sys.platform == 'darwin' or sys.platform == 'linux':
            self.name = self.full_path.rsplit('/')[-1]
            self.path = self.full_path.rsplit('/')[0]
        else:
            # o_O do U use Windows? :-)
            self.name = self.full_path.rsplit('\\')[-1]
            self.path = self.full_path.rsplit('\\')[0]

        self.parse_id3_tags()

    def parse_id3_tags(self):
        with open(self.full_path, 'rb') as fd:
            # Check if our file version is ID3v2
            # 3 bytes: v2 header is "ID3"
            __ID3v = fd.read(3)
            __ID3v = __ID3v.decode()  # перекодируем из байтов в строку
            
            # Возникали проблемы со считыванием в строку
            if  __ID3v == 'ID3':
                # 2 bytes: the minor and revision versions.
                __m_and_r_versions = struct.unpack("h", fd.read(2))
    
                if len(__m_and_r_versions) == 1:
                    self.meta_data["version"] = '{}v{}.0'.format(__ID3v, __m_and_r_versions[0])
                else:
                    self.meta_data["version"] = '{}v{}.{}'.format(__ID3v, 
                                                                __m_and_r_versions[0], 
                                                                __m_and_r_versions[1])

                # 1 byte (first 4 bits): flags
                # здесь возможно пригодится bytearray 
                self.meta_data["flags"] = '{0:08b}'.format(ord(fd.read(1)))
                """
                http://id3.org/id3v2.4.0-structure
                flags
                a - Unsynchronisation
                b - Extended header
                c - Experimental indicator
                d - Footer present
                """
                
                # 4 bytes: The size of the extended header (if any), frames, and padding
                # afer unsynchronization. This is a sync safe integer, so only the
                # bottom 7 bits of each byte are used.
                self.meta_data["extended_header"] = fd.read(4)

                # self.meta_data['frame_1_header'] = fd.read(256)
                # self.meta_data['frame_1_size'] = fd.read(2)
            else:
                # temporary empty, will be used for handle formats < 2 version
                pass
