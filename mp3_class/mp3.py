import os

class MP3Format:
    """ Class-description of mp3 file
        - file name
        - file path
        - ID3-tags
    """
    
    def __init__(self, path):
        # self.name = name + '.mp3'
        self.path = path

    version = ['ID3v1', 'ID3v2']


# Path to current directory
# https://docs.python.org/3/library/os.html#module-os
